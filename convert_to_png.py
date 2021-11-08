from PIL import Image


def convert_to_png(filename):
    im = Image.open(f"images\{filename}.png")
    im.save(f"images\{filename}.png", "PNG")
    return 0
