import subprocess
import os

def determine_desktop_environment():
    ret = None
    desktop_env = os.environ.get('XDG_CURRENT_DESKTOP')

    if desktop_env in ('Unity', 'Gnome'):
        ret = gnome()
    elif desktop_env in ('Xfce'):
        ret = None #xfce()
    elif desktop_env in ('Kde'):
        ret = None #kde()
    elif desktop_env in ('Mate'):
        ret = mate()
    elif desktop_env in ('Cinnamon'):
        ret = cinnamon()
    else:
        pass

    return ret


#module responsible for setting and getting background for specific desktop environment
class background:

    def __init__(self, directory):
        self.directory = directory
        self.desktop_env = determine_desktop_environment()

    def get_current(self):
        cmd = self.desktop_env.get_cmd
        #text=True is output as text not as bytes
        result = subprocess.run(cmd, capture_output=True, shell=True, text=True)
        return result.stdout

    def set_new(self, filename):
        file = "file://" + self.directory + "/" + filename
        cmd = self.desktop_env.set_cmd + file
        result = subprocess.run(cmd, capture_output=True, shell=True)
        return result.returncode


# Possible desktop environments:
#Gnome
class gnome:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.gnome.desktop.background picture-uri '
        self.set_cmd = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri '

"""
To be done:
class xfce:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.gnome.desktop.background picture-uri '
        self.set_cmd = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri '

class kde:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.gnome.desktop.background picture-uri '
        self.set_cmd = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri '
"""
class mate:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.mate.background picture-filename '
        self.set_cmd = '/usr/bin/gsettings set org.mate.background picture-filename '

class cinnamon:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.cinnamon.desktop.background picture-uri '
        self.set_cmd = '/usr/bin/gsettings set org.cinnamon.desktop.background picture-uri '



if __name__ == '__main__':
    pass

