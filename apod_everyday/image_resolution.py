import sys
from PIL import Image


def get_image_resolution(filename):
    im = Image.open(filename)
    width, height = im.size
    return (width, height)

def is_image_good_resolution(screen_res, image_res):
    acceptable_ratio = 0.7

    screen_w, screen_h = screen_res
    image_w, image_h = image_res

    if((image_w < acceptable_ratio * screen_w) or (image_h < acceptable_ratio * screen_h)):
        return False

    return True


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 2:
        print(get_image_resolution(sys.argv[1]))
    if len(sys.argv) == 3:
        screen_res = tuple(map(int, sys.argv[1].split(',')))
        image_res = tuple(map(int, sys.argv[2].split(',')))
        print(is_image_good_resolution(screen_res, image_res))