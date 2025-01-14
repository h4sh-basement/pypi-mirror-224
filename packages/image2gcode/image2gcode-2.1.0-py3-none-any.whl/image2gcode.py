#!/usr/bin/env python3
"""
image2gcode: convert an image to gcode.
"""
__version__ = "2.1.0"

import sys
import math
import argparse
from argparse import Namespace
from datetime import datetime
from PIL import Image
import numpy as np

GCODE2IMAGE = True
try:
    from gcode2image import gcode2image
except ImportError:
    GCODE2IMAGE = False

def loadImage(imagefile: str = None, showimage: bool = True):
    """
    loadimage: load an image and convert it to b&w with white background
    """

    if imagefile:
        # add alpha channel
        img = Image.open(imagefile).convert("RGBA")

        # create a white background and add it to the image
        img_background = Image.new(mode = "RGBA", size = img.size, color = (255,255,255))
        img = Image.alpha_composite(img_background, img)

        # convert image to black&white (same size)
        img = img.resize(img.size, Image.Resampling.LANCZOS).convert("L")
        if showimage:
            img.show()

        # return np array of image
        return np.array(img)

    return None

def distance(A: (float,float),B: (float,float)):
    """
    Does Pythagoras
    """
    # |Ax - Bx|^2 + |Ay - By|^2 = C^2
    # distance = √C^2
    return math.sqrt(abs(A[0] - B[0])**2 + abs(A[1] - B[1])**2)

def boundingbox(bbox:dict[str,float], XY: (float,float)) -> dict[str,float]:
    """
    boundingbox: update bounding box
    """
    if bbox is not None:
        bbox["minX"] = XY[0] if XY[0] < bbox["minX"] else bbox["minX"]
        bbox["minY"] = XY[1] if XY[1] < bbox["minY"] else bbox["minY"]
        bbox["maxX"] = XY[0] if XY[0] > bbox["maxX"] else bbox["maxX"]
        bbox["maxY"] = XY[1] if XY[1] > bbox["maxY"] else bbox["maxY"]

    return bbox

def image2gcode(img, args) -> str:
    """
    image2gcode: convert image to gcode
    """

    # args settings:
    # pixelsize:        pixel size in mm (all dimensions)
    # speed:            laser head print speed
    # power:            maximum power of laser

    invert_intensity = True		# black == white

    # set X/Y-axis precision to number of digits after
    XY_prec = len(str(args.pixelsize).split('.')[1])

    # on the safe side: laser stop, fan on, laser on while moving
    gcode_header = ["M5","M8", 'M3' if args.constantburn else 'M4']
    # laser off, fan off, program stop
    gcode_footer = ["M5","M9","M2"]

    # header comment
    gcode = [f";    {sys.argv[0]} {__version__} ({str(datetime.now()).split('.')[0]})\n"
             f';    Area: {str(round(img.shape[1] * args.pixelsize,2))}mm X {str(round(img.shape[0] * args.pixelsize,2))}mm (XY)\n'
             f';    > pixelsize {str(args.pixelsize)}mm^2, speed {str(args.speed)}mm/min, maxpower {str(args.maxpower)},\n'
             f";      speedmoves {args.speedmoves}, noise level {args.noise}, offset {args.offset}, burn mode {'M3' if args.constantburn else 'M4'}\n;\n"]

    # init gcode
    gcode += ["G00 G17 G40 G21 G54","G90"]
    # on the safe side: laser stop, fan on, laser on while moving only
    gcode += gcode_header

    # set printer start coordinates
    X = round(args.offset[0], XY_prec)
    Y = round(args.offset[1], XY_prec)

    # go to start
    gcode += [f"G0X{X}Y{Y}"]

    # initiate boundingbox
    bbox = {'minX':X,'minY':Y,'maxX':X,'maxY':Y}

    # set write speed and G1 move mode
    # (note that this stays into effect until another G code is executed,
    #  so we do not have to repeat this for all coordinates emitted below)
    gcode += [f"G1F{args.speed}"]

    # Print left to right, shift one scan line down, then right to left,
    # one scanline down (repeat)
    #
    # Optimized gcode:
    # - draw pixels in one go until change of power
    # - emit X/Y coordinates only when they change
    # - emit linear move 'G1/G0' code minimally
    # - does not emit zero power (or below cutoff) pixels
    #
    # General optimizations:
    # - laser head has defered and sparse moves.
    #   (XY locations are virtual, head does not always follow)
    # - moves at high speed (G0) over 10mm (default) or more zero pixels
    # - low burn levels (noise pixels) can be suppressed (default off)
    #
    left2right = True

    # current location of laser head
    head = (X,Y)

    # start print
    for line in img:

        if not left2right:
            # reverse line when printing right to left
            line = np.flip(line)

        # add line terminator (makes this algorithm regular)
        line = np.append(line,0)

        # Note that (laser) drawing from a point to a point differs from setting a point (within an image):
        #              0   1   2   3   4   5   6     <-- gcode drawing points
        # one line:    |[0]|[1]|[2]|[3]|[4]|[5]|     <-- image pixels
        #
        # For example: drawing from X0 to X2 with value S10 corresponds to setting [0] = S10 and [1] = S10
        # Note also that drawing form left to right differs subtly from the reverse

        # draw this pixel line
        for count, pixel in enumerate(line):
            laserpow = round((1.0 - float(pixel/255)) * args.maxpower) if invert_intensity else round(float(pixel/255) * args.maxpower)

            if count == 0:
                # delay emit first pixel (so all same power pixels can be emitted in one sweep)
                prev_pow = laserpow
                # set last head loaction on start of the line
                lastloc = (X,Y)

            # draw pixels until change of power
            if laserpow != prev_pow or count == line.size-1:
                #if prev_pow != 0:
                if prev_pow > args.noise:
                    code = ""
                    if lastloc:
                        # head is not at correct location, go there
                        if args.speedmoves and (distance(head,(X,Y)) > args.speedmoves):
                            # fast
                            code = f"G0 X{lastloc[0]}Y{lastloc[1]}\n"
                            code += f"G1\n"
                        else:
                            # normal speed
                            code = f"X{lastloc[0]}Y{lastloc[1]} S0\n"

                    # emit point
                    code += f"X{X}S{prev_pow}"
                    gcode += [code]

                    # update boundingbox
                    bbox = boundingbox(bbox, (X,Y))

                    # head at this location
                    head = (X,Y)
                    lastloc = None
                else:
                    # didn't move head to location, save it
                    lastloc = (X,Y)

                if count == line.size-1:
                    continue
                prev_pow = laserpow # if laserpow != prev_pow

            # next point
            X = round(X + (args.pixelsize if left2right else -args.pixelsize), XY_prec)

        # next scan line (defer head movement)
        Y = round(Y + args.pixelsize, XY_prec)

        # change print direction
        left2right = not left2right

    # emit bounding box
    gcode = [f';\n;    Boundingbox: (X{bbox["minX"]},Y{bbox["minY"]}):(X{bbox["maxX"]},Y{bbox["maxY"]})\n;\n'] + gcode

    # laser off, fan off, program stop
    gcode += gcode_footer

    return '\n'.join(gcode)

def main() -> int:
    """
    main
    """
    # defaults
    pixelsize_default = 0.1
    speed_default = 800
    power_default = 300
    speedmoves_default = 10
    noise_default = 0

    # Define command line argument interface
    parser = argparse.ArgumentParser(description='Convert an image to gcode for GRBL v1.1 compatible diode laser engravers.')
    parser.add_argument('image', type=argparse.FileType('r'), help='image file to be converted to gcode')
    parser.add_argument('gcode', type=argparse.FileType('w'), nargs='?', default = sys.stdout, help='gcode output')
    parser.add_argument('--showimage', action='store_true', default=False, help='show b&w converted image' )
    parser.add_argument('--pixelsize', default=pixelsize_default, metavar="<default:" + str(pixelsize_default)+">",
        type=float, help="pixel size in mm (XY-axis): each image pixel is drawn this size")
    parser.add_argument('--speed', default=speed_default, metavar="<default:" + str(speed_default)+">",
        type=int, help='draw speed in mm/min')
    parser.add_argument('--maxpower', default=power_default, metavar="<default:" +str(power_default)+ ">",
        type=int, help="maximum laser power while drawing (as a rule of thumb set to 1/3 of the maximum of a machine having a 5W laser)")
    parser.add_argument('--offset', default=[10.0, 10.0], nargs=2, metavar=('X-off', 'Y-off'),
        type=float, help="laser drawing starts at offset (default: X10.0 Y10.0)")
    parser.add_argument('--speedmoves', default=speedmoves_default, metavar="<default:" + str(speedmoves_default)+">",
        type=float, help="length of zero burn zones in mm (0 sets no speedmoves): issue speed (G0) moves when skipping space of given length (or more)")
    parser.add_argument('--noise', default=noise_default, metavar="<default:" +str(noise_default)+ ">",
        type=int, help="noise power level, do not burn pixels below this power level")
    parser.add_argument('--constantburn', action='store_true', default=False, help='select constant burn mode M3 (a bit more dangerous!), instead of dynamic burn mode M4')
    parser.add_argument('--validate', action='store_true', default=False, help='validate gcode file, do inverse and show image result' )
    parser.add_argument('-V', '--version', action='version', version='%(prog)s ' + __version__, help="show version number and exit")

    args = parser.parse_args()

    if args.validate and (args.gcode.name == "<stdout>" or not GCODE2IMAGE):
        if not GCODE2IMAGE:
            print("For validation package gcode2image.py must be installed (in $PATH or python install path)")
        else:
            print("For validation a 'gcode filename' argument must be set.")
            parser.print_usage(sys.stderr)
        sys.exit(1)

    # load and convert image to B&W
    # flip image updown because Gcode and raster image coordinate system differ
    narr = np.flipud(loadImage(args.image.name,args.showimage))

    print(f'Area: {str(round(narr.shape[1] * args.pixelsize,2))}mm X {str(round(narr.shape[0] * args.pixelsize,2))}mm (XY)\n'
          f'    > pixelsize {args.pixelsize}mm^2, speed {args.speed}mm/min, maxpower {str(args.maxpower)},\n'
          f"      speedmoves {args.speedmoves}, noise level {args.noise}, offset {args.offset}, burn mode {'M3' if args.constantburn else 'M4'}")

    # emit gcode for image
    print(image2gcode(narr, args), file=args.gcode)

    if args.validate:
        args.gcode.close()
        with open(args.gcode.name, "r") as fgcode:
            # flip to raster image coordinate system
            img = np.flipud(gcode2image(Namespace(gcode = fgcode, offset = False, showG0 = True, grid = False)))

            # convert to image
            img = Image.fromarray(img)

            # show image
            img.show()
            # write image file (png)
            #pic.save(args.gcode.name.split('.')[0] + '_' + sys.argv[0].split('.')[0] + '.png')

    return 0

if __name__ == '__main__':
    sys.exit(main())
