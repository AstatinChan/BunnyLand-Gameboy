import json
import sys
import os

filename = sys.argv[1]

label = "_map_" + os.path.basename(filename)[:-5].replace(".", " ").title().replace(" ", "_")

print(label+":")
file = open(filename, "r")

ldtk = json.loads(file.read())

intgridLayer = [i for i in ldtk['levels'][0]['layerInstances'] if i['__type'] == 'IntGrid'][0]['intGridCsv']
autoLayer = [i for i in ldtk['levels'][0]['layerInstances'] if i['__type'] == 'AutoLayer'][0]['autoLayerTiles']

collision_map = []
for y in range(0, 32):
    for x in range(0,4):
        collision_u8 = 0
        for i in range(0,8):
            if intgridLayer[y*32+(31-(x*8+i))] == 2:
                collision_u8 |= 1 << (7-i)
        collision_map.append(collision_u8 ^ 0xff)

for i in range(0, int(len(collision_map) / 16)):
    print("\t.DB ", end="")
    for j in range(0, 15):
        print("${:02x}, ".format(collision_map[i*16+j]), end="")
    print("${:02x}".format(collision_map[i*16+15]))

# print("============================")
# print(autoLayer)
