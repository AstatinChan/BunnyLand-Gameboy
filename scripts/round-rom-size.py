import sys
import os

if len(sys.argv) != 2:
    raise ValueError("Rom file must be specified as first argument")

rom_filename = sys.argv[1]
current_filesize = os.path.getsize(rom_filename)

i = 0
for n in range(0, 9):
    if current_filesize <= 32768 * (1 << n):
        break
    i += 1

missing = (32768 * (1 << i)) - current_filesize

print("Original file size =", current_filesize, "bytes")
print("ROM size =", hex(i), "({} bytes)".format(32768 * (1 << i)))

rom_file = open(rom_filename, 'r+b')

rom_file.seek(0x148)

rom_file.write(bytes(bytearray([i])))

rom_file.close()

rom_file = open(rom_filename, 'a+b')


rom_file.write(bytes(bytearray([0]*missing)))

rom_file.close()
