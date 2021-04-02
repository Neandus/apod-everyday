import os
import subprocess
from math import gcd

class screen:
    def __init__(self):
        pass

    def get_screen_resolution(self):
        cmd = "xrandr | grep \* | cut -d' ' -f4"

        result = subprocess.run(cmd, capture_output=True, shell=True, text=True)

        if result.returncode == 0:
            resolution = result.stdout.strip()
            w, h = resolution.split('x')
            return (int(w), int(h))
        else:
            return None

    #From: https://gist.github.com/Integralist/4ca9ff94ea82b0e407f540540f1d8c6c
    def get_screen_ratio(self, width: int, height: int):
        temp = 0

        if width == height:
            return (1, 1)

        if width < height:
            temp = width
            width = height
            height = temp

        divisor = gcd(width, height)
        if divisor != 0:
            x = int(width / divisor) if not temp else int(height / divisor)
            y = int(height / divisor) if not temp else int(width / divisor)

        return (x, y)


if __name__ == "__main__":
    pass