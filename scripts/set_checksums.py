import sys

if len(sys.argv) != 2:
    raise ValueError("Rom file must be specified as first argument")

rom_filename = sys.argv[1]

rom_file = open(rom_filename, 'r+b')

rom_file.seek(0x0134)

header = rom_file.read(0x19)

header_checksum = 0
for b in header:
    header_checksum = (header_checksum - int(b) - 1) & 0xff

print("HEADER CHECKSUM =", hex(header_checksum), file=sys.stderr)

rom_file.seek(0x014d)

rom_file.write(bytes(bytearray([header_checksum])))

rom_file.close()
