from PIL import Image
import argparse
import sys

parser = argparse.ArgumentParser('ansi-generator')
parser.add_argument('path', type=str)
parser.add_argument('--resize', required=False, type=bool, default=False, const=True, nargs='?')
parser.add_argument('--reduce', required=False, type=bool, default=False, const=True, nargs='?')
print('<path> [--resize] [--reduce]')
args = input('\033[38;2;0;120;255m$ \033[0m ')
args = parser.parse_args(args.split())
path = args.path
reduce = args.reduce
resize = args.resize

image = Image.open(path)
image = image.convert('RGBA')
if resize:
    image = image.resize((300, 300))
if reduce:
    image=image.reduce(3)
if image.mode == 'RGBA':
    s=''
    for y in range(image.height):
        for x in range(image.width):
            color = image.getpixel((x, y))
            s += f"\033[48;2;{';'.join(str(i) for i in color)}m   " # images may be a bit stretched, change this accordingly
        s +='\033[0mㅤ\n'
    sys.stdout.write(s)
