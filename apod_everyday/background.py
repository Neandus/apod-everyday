import subprocess
import os

def determine_desktop_environment():
    ret = None
    desktop_env = os.environ.get('XDG_CURRENT_DESKTOP')
    print(f"You are using: {desktop_env.lower()}" )

    if 'gnome' in desktop_env.lower():
        ret = gnome()
    elif 'xfce' in desktop_env.lower():
        ret = xfce()
    elif 'kde' in desktop_env.lower():
        ret = kde()
    elif 'mate' in desktop_env.lower():
        ret = mate()
    elif 'cinnamon' in desktop_env.lower():
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
        file = self.directory + "/" + filename
        cmd = self.desktop_env.set_cmd + file
        result = subprocess.run(cmd, capture_output=True, shell=True)
        return result.returncode


# Possible desktop environments:
#Gnome
class gnome:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.gnome.desktop.background picture-uri '
        self.set_cmd = '/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://'

class xfce:
    def __init__(self):
        #For now assume one monitor is connected
        result = subprocess.run('xrandr --listmonitors | grep \'+\' | awk {\'print $4\'}', capture_output=True, shell=True, text=True)
        connected = result.stdout.rstrip()
        self.get_cmd = f'/usr/bin/xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor{connected}/workspace0/last-image '
        self.set_cmd = f'/usr/bin/xfconf-query --channel xfce4-desktop --property /backdrop/screen0/monitor{connected}/workspace0/last-image --set '

class kde:
    def __init__(self):
        self.get_cmd = None
        self.set_cmd = None

class mate:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.mate.background picture-filename '
        self.set_cmd = '/usr/bin/gsettings set org.mate.background picture-filename file://'

class cinnamon:
    def __init__(self):
        self.get_cmd = '/usr/bin/gsettings get org.cinnamon.desktop.background picture-uri '
        self.set_cmd = '/usr/bin/gsettings set org.cinnamon.desktop.background picture-uri file://'



if __name__ == '__main__':
    determine_desktop_environment()

