from PIL import Image
import numpy as np
import sys

colours = [(0xe0, 0xf8, 0xd0), (0x88, 0xc0, 0x70), (0x34, 0x68, 0x56), (0x08, 0x18, 0x20)]

if len(sys.argv) != 3:
    print("Usage: ./extract-vram-tileset.py [vram_dump_file] [output_png]")
    sys.exit(-1)

filename = sys.argv[1]

output_filename = sys.argv[2]

file = open(filename, "r")

vram_text = file.read()

vram = [int(x, 16) for x in vram_text.split()]

def parse_tile(image, tile, offset):
    for y in range(0, 16, 2):
        for x in range(0, 8):
            colour_id = 0b00
            colour_id |= (tile[y] >> (7-x)) & 1
            colour_id |= ((tile[y+1] >> (7-x)) & 1) << 1
            image.putpixel((x+offset[0],int(y/2)+offset[1]), colours[colour_id])
    return image

image = Image.new("RGB", (128,128))

x = 0
y = 0
for tile_addr in range(0x1000, 0x1800, 0x10):
    parse_tile(image, vram[tile_addr:tile_addr + 0x10], (x * 8, y * 8))
    x += 1
    if x == 0x10:
        x = 0
        y += 1
for tile_addr in range(0x800, 0x1000, 0x10):
    parse_tile(image, vram[tile_addr:tile_addr + 0x10], (x * 8, y * 8))
    x += 1
    if x == 0x10:
        x = 0
        y += 1

image.save(output_filename)
