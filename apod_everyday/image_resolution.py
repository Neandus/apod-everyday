import sys
from PIL import Image


def get_image_resolution(filename):
    im = Image.open(filename)
    width, height = im.size
    return (width, height)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        get_image_resolution(sys.argv[1])