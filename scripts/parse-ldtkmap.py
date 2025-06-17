import json
import sys
import os

filename = sys.argv[1]

label = "_map_" + os.path.basename(filename)[:-5].replace(".", " ").title().replace(" ", "_")
check_same_bank = "_same_bank_check_"+label+""

print(label+":")

file = open(filename, "r")

ldtk = json.loads(file.read())

intgridLayer = [i for i in ldtk['levels'][0]['layerInstances'] if i['__type'] == 'IntGrid'][0]['intGridCsv']
autoLayer = [i for i in ldtk['levels'][0]['layerInstances'] if i['__type'] == 'AutoLayer'][0]['autoLayerTiles']
tiles = [i for i in ldtk['levels'][0]['layerInstances'] if i['__type'] == 'Tiles'][0]
tile_width = tiles['__cWid']
tile_height = tiles['__cHei']
grid_tiles = tiles['gridTiles']

tilemap = [0 for _ in range(0, tile_width*tile_height)]

for tile in autoLayer:
    x = int(tile['px'][0]/8)
    y = int(tile['px'][1]/8)
    t = tile['t']
    topleft = (((t & 0b100) >> 1) | (t & 0b1)) + 0x20
    topright = ((t & 0b110) >> 1) + 0x24
    bottomleft = (((t & 0b1000) >> 2) | (t & 0b1)) + 0x28
    bottomright = (((t & 0b1000) >> 2) | ((t & 0b10) >> 1)) + 0x2c

    tilemap[y * tile_width + x] = topleft
    tilemap[y * tile_width + x+1] = topright
    tilemap[(y+1) * tile_width + x] = bottomleft
    tilemap[(y+1) * tile_width + x+1] = bottomright

for tile in grid_tiles:
    tilemap[tile['d'][0]] = tile['t']

collision_map = []
for y in range(0, 32):
    for x in range(0,4):
        collision_u8 = 0
        for i in range(0,8):
            if intgridLayer[y*32+(31-(x*8+i))] == 2:
                collision_u8 |= 1 << (7-i)
        collision_map.append(collision_u8 ^ 0xff)

print("\t.collisons:")
for i in range(0, int(len(collision_map) / 16)):
    print("\t\t.DB ", end="")
    for j in range(0, 15):
        print("${:02x}, ".format(collision_map[i*16+j]), end="")
    print("${:02x}".format(collision_map[i*16+15]))

print("\t.tiles:")
for i in range(0, int(len(tilemap) / 16)):
    print("\t\t.DB ", end="")
    for j in range(0, 15):
        print("${:02x}, ".format(tilemap[i*16+j]), end="")
    print("${:02x}".format(tilemap[i*16+15]))

print(".ASSERT", "bank(="+label+")", "bank(.)")

# print("============================")
# print(autoLayer)
