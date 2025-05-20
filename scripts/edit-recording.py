import sys

file = open(sys.argv[1], "rb")
output_file = open(sys.argv[2], "wb")

last_cycle_update = 0
offset = 0
while True:
    next_cycle_update_buf = file.read(16)
    if len(next_cycle_update_buf) < 16:
        break
    inputs = file.read(2)

    next_cycle_update = int.from_bytes(next_cycle_update_buf, byteorder="little", signed=False)
    print("CYCLES: %d, input1: %08x, input2: %08x" % (next_cycle_update, inputs[0], inputs[1]))


    next_cycle_update -= offset

    if last_cycle_update != 0:
        if next_cycle_update - last_cycle_update > 70224 * 256 * 8:
            new_offset = (next_cycle_update - last_cycle_update) - ((next_cycle_update - last_cycle_update) % (70224 * 256)) - (70224 * 256)
            print(new_offset)
            next_cycle_update -= new_offset
            offset += new_offset


    last_cycle_update = next_cycle_update
    output_file.write(next_cycle_update.to_bytes(16, byteorder="little", signed=False))
    output_file.write(inputs)
