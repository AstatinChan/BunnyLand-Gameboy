import subprocess

sprite_idx = 0x0

def get_sprite_png_parse_output(png, tallmode=False, sprite_1bpp_mode=False):
    global sprite_idx
    result = str(subprocess.check_output(["python", "./scripts/parse_sprite_png.py", png] + (["--8x16"] if tallmode else []) + (["--1bpp"] if sprite_1bpp_mode else []))).split("\\n")
    for r in result:
        if r.startswith(".DB"):
            print("\t{} ; 0x{:02x}".format(r, sprite_idx))
            sprite_idx += 1

sprite_idx = 0x10
print("GUI_Border_Data:")
get_sprite_png_parse_output("./sprites/gui/borders.png")

sprite_idx = 0x20
print("BG_Tile_Image_Data:")
print("\n\t; Trees")
get_sprite_png_parse_output("./sprites/bg/tree-tileset.png")
print("\n\t; Stairs")
get_sprite_png_parse_output("./sprites/bg/stairs.png")
print("\n\t; Carrot")
get_sprite_png_parse_output("./sprites/bg/carrot.png")

print("Small_sprites:")
print("\n\t; Heart")
get_sprite_png_parse_output("./sprites/gui/heart.png")
print("\n\t; Cursor")
get_sprite_png_parse_output("./sprites/gui/cursor.png")

sprite_idx = 0x80
print("\nFont_Data:")
get_sprite_png_parse_output("./sprites/font.png")

sprite_idx = 0x02
print("\nOBJ_Tile_Image_Data:")
print("\n\t; Bunny side")
get_sprite_png_parse_output("./sprites/bunny/bunny-side.png", tallmode=True)
print("\n\t; Bunny back")
get_sprite_png_parse_output("./sprites/bunny/bunny-back.png", tallmode=True)
print("\n\t; Bunny front")
get_sprite_png_parse_output("./sprites/bunny/bunny-front.png", tallmode=True)

print("\n\t; Fox side")
get_sprite_png_parse_output("./sprites/fox/fox-side1.png", tallmode=True)
print("\n\t; Fox back")
get_sprite_png_parse_output("./sprites/fox/fox-back.png", tallmode=True)
print("\n\t; Fox front")
get_sprite_png_parse_output("./sprites/fox/fox-front.png", tallmode=True)

sprite_idx = 0x60
print("\nAnimation_Sprites_Data:")
print("\n\t; Sparkles")
get_sprite_png_parse_output("./sprites/animations/sparkle1.png", tallmode=True)
get_sprite_png_parse_output("./sprites/animations/sparkle2.png", tallmode=True)
get_sprite_png_parse_output("./sprites/animations/ball.png", tallmode=True)
