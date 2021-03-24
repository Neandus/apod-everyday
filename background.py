import subprocess

class Background:
    def __init__(self, directory):
        self.directory = directory
        self.gsettings_bin = "/usr/bin/gsettings"
        self.schema = "org.gnome.desktop.background"
        self.key = "picture-uri"

    def get_current(self):
        cmd = [self.gsettings_bin, "get", self.schema, self.key]
        #text=True is output as text not as bytes
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    def set_new(self, filename):
        file = "file://" + self.directory + "/" + filename
        cmd = [self.gsettings_bin, "set", self.schema, self.key, file]
        result = subprocess.run(cmd, capture_output=True)
        return result.returncode

if __name__ == '__main__':
    #Default Ubuntu wallpapers
    hardy_background = "hardy_wallpaper_uhd.png"
    warty_background = "warty-final-ubuntu.png"
    
    bg = Background("/usr/share/backgrounds")

    # Tests
    assert(0 == bg.set_new(hardy_background))
    assert(hardy_background in bg.get_current())

    assert(0 == bg.set_new(warty_background))
    assert(warty_background in bg.get_current())
