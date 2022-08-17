from PIL import Image
import argparse
import sys
import datetime
import os
import pickle

parser = argparse.ArgumentParser('ansi-generator')
parser.add_argument('path', type=str)
parser.add_argument('--resize', required=False, type=int, default=False, nargs=2)
parser.add_argument('--reduce', required=False, type=int, default=False, nargs=1)
parser.add_argument('--pickle', required=False, type=bool, default=False, const=True, nargs='?')

print('<path> [--resize int int] [--reduce int] [--pickle]')
args = input('\033[38;2;0;120;255m$ \033[0m ')

args = parser.parse_args(args.split())
path = args.path
reduce = args.reduce
resize = args.resize
pickled = args.pickle

image = Image.open(path)
image = image.convert('RGBA')

if resize!=False:
    image = image.resize(resize)
if reduce!=False:
    image=image.reduce(reduce[0])
if image.mode == 'RGBA':
    s=''
    for y in range(image.height):
        for x in range(image.width):
            color = image.getpixel((x, y))
            s += f"\033[48;2;{';'.join(str(i) for i in color)}m   " # images may be a bit stretched, change this accordingly
        s +='\033[0mㅤ\n'
    name = f'{datetime.datetime.now().strftime("%Y-%m-%d %H %M-%S")} ANSI-str.pickle'
    if pickled:
        if not os.path.isfile(name):
            open(name, 'x')
        file = open(name, 'wb')
        pickle.dump(s, file)
    sys.stdout.write(s)
