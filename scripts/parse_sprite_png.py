from PIL import Image
import numpy as np
import sys

sprite_8x16 = False

if len(sys.argv) >= 3 and sys.argv[2] == "--8x16":
    sprite_8x16 = True

file = Image.open(sys.argv[1]).convert("RGB")

px_array = np.asarray(file)

def getpx(sprite_nb, x, y):
    double_sprite_nb = int(sprite_nb / 4)
    sprite_double_line = int(double_sprite_nb / (file.width / 16))
    sprite_double_column = int(double_sprite_nb % (file.width / 16))
    sprite_tile_y = 1 if sprite_nb & 0b10 else 0
    sprite_tile_x = 1 if sprite_nb & 0b01 else 0

    if sprite_8x16:
        sprite_tile_x ^= sprite_tile_y
        sprite_tile_y ^= sprite_tile_x
        sprite_tile_x ^= sprite_tile_y

    sprite_line = sprite_double_line * 2 + sprite_tile_y
    sprite_column = sprite_double_column * 2 + sprite_tile_x

    return [int(x) for x in px_array[int(sprite_line * 8 + y)][int(sprite_column * 8 + x)]]


if file.width % 8 != 0 or file.height % 8 != 0:
    raise ValueError("Width and height must be multiples of 8px")

sprite_nb = int((file.width / 8) * (file.height / 8))

for nb in range(0, sprite_nb):
    result1 = [0,0,0,0,0,0,0,0]
    result2 = [0,0,0,0,0,0,0,0]
    for y in range(0, 8):
        for x in range(0, 8):
            px = getpx(nb, x, y)
            dw = px[0] - 0xe0 + px[1] - 0xf8 + px[2] - 0xd0
            dlg = px[0] - 0x88 + px[1] - 0xc0 + px[2] - 0x70
            ddg = px[0] - 0x34 + px[1] - 0x68 + px[2] - 0x56
            db = px[0] - 0x08 + px[1] - 0x18 + px[2] - 0x20
    
            if min(abs(db), abs(ddg)) < min(abs(dlg), abs(dw)):
                result2[y] |= 1 << (7-x)
            if min(abs(db), abs(dlg)) < min(abs(ddg), abs(dw)):
                result1[y] |= 1 << (7-x)
            
            if abs(db) < min(abs(dw), abs(dlg), abs(ddg)):
                print("#", end = '')
            if abs(ddg) < min(abs(dw), abs(dlg), abs(db)):
                print(";", end = '')
            if abs(dlg) < min(abs(dw), abs(ddg), abs(db)):
                print(".", end = '')
            else:
                print(" ", end = '')
        print("\n", end = '')
    print("\n")
    for i in range(0, 8):
        if i == 0:
            print(".DB $%02x, $%02x" % (result1[i], result2[i]), end='')
        else:
            print(", $%02x, $%02x" % (result1[i], result2[i]), end='')
    print("\n")
