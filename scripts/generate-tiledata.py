import subprocess
import parse_sprite_png

sprite_idx = 0x0

def get_sprite_png_parse_output(png, tallmode=False, sprite_1bpp_mode=False, sprite_8x8=False):
    global sprite_idx
    result = parse_sprite_png.parseSprite(png, sprite_8x16=tallmode, sprite_8x8=sprite_8x8, sprite_1bpp=sprite_1bpp_mode).split("\n")
    for r in result:
        if r.startswith(".DB"):
            print("\t{} ; 0x{:02x}".format(r, sprite_idx))
            sprite_idx += 1

sprite_idx = 0x10
print("GUI_Border_Data:")
get_sprite_png_parse_output("./sprites/gui/borders.png")
print("GUI_Border_Data.end:")

sprite_idx = 0x20
print("BG_Tile_Image_Data:")
print("\n\t; Trees")
get_sprite_png_parse_output("./sprites/bg/tree-tileset.png", sprite_8x8=True)
print("\n\t; Campfire")
get_sprite_png_parse_output("./sprites/bg/firecamp1.png")
get_sprite_png_parse_output("./sprites/bg/firecamp2.png")
print("\n\t; Logs")
get_sprite_png_parse_output("./sprites/bg/log1.png")
get_sprite_png_parse_output("./sprites/bg/log2.png")
print("\n\t; Arrow up")
get_sprite_png_parse_output("./sprites/bg/arrow-up.png", sprite_8x8=True)
print("\n\t; Tree Entrance")
get_sprite_png_parse_output("./sprites/bg/forest-entrance.png", sprite_8x8=True)
print("BG_Tile_Image_Data.end:")

sprite_idx = 0x60
print("OBJ_Tile_Image_Data:")
print("\n\t; Stairs")
get_sprite_png_parse_output("./sprites/bg/stairs.png")
print("\n\t; Carrot")
get_sprite_png_parse_output("./sprites/bg/carrot.png")
print("\n\t; Leaf")
get_sprite_png_parse_output("./sprites/bg/leaf.png")
print("\n\t; Box")
get_sprite_png_parse_output("./sprites/bg/box.png")
print("OBJ_Tile_Image_Data.end:")

sprite_idx = 0xf0
print("Small_sprites:")
print("\n\t; Heart")
get_sprite_png_parse_output("./sprites/gui/heart.png")
print("\n\t; Energy")
get_sprite_png_parse_output("./sprites/gui/energy-points.png")
print("\n\t; Cursor")
get_sprite_png_parse_output("./sprites/gui/cursor.png")
print("\n\t; Disabled Cursor")
get_sprite_png_parse_output("./sprites/gui/disabled-cursor.png")
print("\n\t; Floor")
get_sprite_png_parse_output("./sprites/gui/floor.png")
print("\n\t; Freeze status")
get_sprite_png_parse_output("./sprites/gui/status-frozen.png")
print("\n\t; Poison status")
get_sprite_png_parse_output("./sprites/gui/status-poison.png")
print("Small_sprites.end:")

sprite_idx = 0x80
print("\nFont_Data:")
get_sprite_png_parse_output("./sprites/font.png")
print("\nFont_Data.end:")

sprite_idx = 0x02
print("\nEntity_Tile_Image_Data:")
print("\n.Bunny:")
print("\n\t; Bunny side")
get_sprite_png_parse_output("./sprites/bunny/bunny-side.png", tallmode=True)
print("\n\t; Bunny back")
get_sprite_png_parse_output("./sprites/bunny/bunny-back.png", tallmode=True)
print("\n\t; Bunny front")
get_sprite_png_parse_output("./sprites/bunny/bunny-front.png", tallmode=True)
print("\n.Bunny.end:")

print("\n.Fox:")
print("\n\t; Fox side")
get_sprite_png_parse_output("./sprites/fox/fox-side1.png", tallmode=True)
print("\n\t; Fox back")
get_sprite_png_parse_output("./sprites/fox/fox-back.png", tallmode=True)
print("\n\t; Fox front")
get_sprite_png_parse_output("./sprites/fox/fox-front.png", tallmode=True)
print("\n.Fox.end:")

print("\n.Cat:")
print("\n\t; Cat side")
get_sprite_png_parse_output("./sprites/cat/side.png", tallmode=True)
print("\n\t; Cat back")
get_sprite_png_parse_output("./sprites/cat/back.png", tallmode=True)
print("\n\t; Cat front")
get_sprite_png_parse_output("./sprites/cat/front.png", tallmode=True)
print("\n.Cat.end:")

print("\n.Owl:")
print("\n\t; Owl side")
get_sprite_png_parse_output("./sprites/owl/side.png", tallmode=True)
print("\n\t; Owl back")
get_sprite_png_parse_output("./sprites/owl/back.png", tallmode=True)
print("\n\t; Owl front")
get_sprite_png_parse_output("./sprites/owl/front.png", tallmode=True)
print("\n.Owl.end:")

print("\n.Bug:")
print("\n\t; Bug side")
get_sprite_png_parse_output("./sprites/bug/side.png", tallmode=True)
print("\n\t; Bug back")
get_sprite_png_parse_output("./sprites/bug/back.png", tallmode=True)
print("\n\t; Bug front")
get_sprite_png_parse_output("./sprites/bug/front.png", tallmode=True)
print("\n.Bug.end:")

print("\n.Mouse:")
print("\n\t; Mouse side")
get_sprite_png_parse_output("./sprites/mouse/side.png", tallmode=True)
print("\n\t; Mouse back")
get_sprite_png_parse_output("./sprites/mouse/back.png", tallmode=True)
print("\n\t; Mouse front")
get_sprite_png_parse_output("./sprites/mouse/front.png", tallmode=True)
print("\n.Mouse.end:")

print("\n.Fimsh:")
print("\n\t; Fimsh side")
get_sprite_png_parse_output("./sprites/fimsh/side.png", tallmode=True)
print("\n\t; Fimsh back")
get_sprite_png_parse_output("./sprites/fimsh/back.png", tallmode=True)
print("\n\t; Fimsh front")
get_sprite_png_parse_output("./sprites/fimsh/front.png", tallmode=True)
print("\n.Fimsh.end:")

print("\n.Penguin:")
print("\n\t; Penguin side")
get_sprite_png_parse_output("./sprites/penguin/side.png", tallmode=True)
print("\n\t; Penguin back")
get_sprite_png_parse_output("./sprites/penguin/back.png", tallmode=True)
print("\n\t; Penguin front")
get_sprite_png_parse_output("./sprites/penguin/front.png", tallmode=True)
print("\n.Penguin.end:")

print("\n.Frog:")
print("\n\t; Frog side")
get_sprite_png_parse_output("./sprites/frog/side.png", tallmode=True)
print("\n\t; Frog back")
get_sprite_png_parse_output("./sprites/frog/back.png", tallmode=True)
print("\n\t; Frog front")
get_sprite_png_parse_output("./sprites/frog/front.png", tallmode=True)
print("\n.Frog.end:")
print("\nEntity_Tile_Image_Data.end:")

sprite_idx = 0x60
print("\nAnimation_Sprites_Data:")
print("\n\t; Sparkles")
get_sprite_png_parse_output("./sprites/animations/sparkle1.png", tallmode=True)
get_sprite_png_parse_output("./sprites/animations/sparkle2.png", tallmode=True)
get_sprite_png_parse_output("./sprites/animations/ball.png", tallmode=True)
get_sprite_png_parse_output("./sprites/animations/bubble1.png", tallmode=True)
get_sprite_png_parse_output("./sprites/animations/bubble2.png", tallmode=True)
print("\nAnimation_Sprites_Data.end:")

sprite_idx = 0x01
print("\nTitle_Screen_Sprite_Data:")
get_sprite_png_parse_output("./sprites/gui/title-screen.png", sprite_8x8=True)
print("\nTitle_Screen_Sprite_Data.end:")
