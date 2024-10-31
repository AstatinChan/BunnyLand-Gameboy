import sys

if len(sys.argv) < 2:
    raise ValueError("Must have gbtxt file in first argument")

gbtxt_filename = sys.argv[1]

gbtxt_file = open(gbtxt_filename, 'r')


def ascii_to_gbtext_format(c):
    c = c.upper()
    match c:
        case c if c <= '9' and c >= '0':
            return ord(c) - ord('0') + 0x80
        case c if c <= 'Z' and c >= 'A':
            return ord(c) - ord('A') + 0x80 + 10
        case ':':
            return 0xaa
        case '"':
            return 0xa9
        case "'":
            return 0xa8
        case ',':
            return 0xa7
        case '?':
            return 0xa6
        case '!':
            return 0xa5
        case '.':
            return 0xa4
        case ' ':
            return 0x00
        case _:
            raise ValueError("Char \"" + c + "\" is not in the allowed charset")

for line in gbtxt_file:
    line = line.strip()

    if len(line) == 0:
        continue
    
    if line[0] == '#':
        continue

    if not ':' in line:
        raise ValueError("Text without label is not allowed")

    label = line[:line.index(':') + 1]
    text = line[line.index(':') + 1:].strip()

    print(label)

    print(".DB", ", ".join([hex(ascii_to_gbtext_format(c)) for c in text]) + ", 0xff")
