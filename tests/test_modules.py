from context import apod_path
from context import background
from context import downloader
from context import image_link_parser
from context import arg_parser
from context import screen
from context import image_resolution
from context import database
from context import db_config

import datetime
import os


def test_apod_path():
    ad = apod_path.apod_path()
    today_apod_url_path = ad.parse_date(datetime.datetime.now())
    print(today_apod_url_path)

    other_date_url_path = ad.parse_date(datetime.datetime(2004, 3, 5))
    print(other_date_url_path)

def test_background():
    #Default Ubuntu wallpapers
    hardy_background = "hardy_wallpaper_uhd.png"
    warty_background = "warty-final-ubuntu.png"
    
    bg = background.background("/usr/share/backgrounds")

    # Tests
    assert(0 == bg.set_new(hardy_background))
    assert(hardy_background in bg.get_current())

    assert(0 == bg.set_new(warty_background))
    assert(warty_background in bg.get_current())

def test_downloader():
    test_array = [
        {'url' : 'https://apod.nasa.gov/apod/image/2010/STScI_NGC2525_1865x2000.jpg', 'output_name': 'ap201023.jpg'},
        {'url' : 'https://apod.nasa.gov/apod/image/2102/LunarHalo_Strand_1500.jpg', 'output_name': '210201.jpg'},
        {'url' : 'https://apod.nasa.gov/apod/image/2101/NGC1316Center_HubbleNobre_2585.jpg', 'output_name': 'ap210126.jpg'},
        {'url' : 'https://apod.nasa.gov/apod/image/2012/2020Dec14TSE_Ribas_IMG_9291c.jpg', 'output_name': 'ap201218.jpg'}
    ]

    d = downloader.downloader('/tmp/')

    def test_file_exists(file):
        try:
            f = open(file)
            return True
        except FileNotFoundError:
            return False
        finally:
            f.close()

    for test_case in test_array:
        assert(True == d.download(test_case['url'], test_case['output_name']))
        assert(True == test_file_exists('/tmp/' + test_case['output_name']))

def test_image_link_parser():
    test_array = [
        {'date': 'ap201023.html', 'link': 'image/2010/STScI_NGC2525_1865x2000.jpg'},
        {'date': 'ap210216.html', 'link': ''},
        {'date': 'ap210201.html', 'link': 'image/2102/LunarHalo_Strand_1500.jpg'},
        {'date': 'ap210126.html', 'link': 'image/2101/NGC1316Center_HubbleNobre_2585.jpg'},
        {'date': 'ap201218.html', 'link': 'image/2012/2020Dec14TSE_Ribas_IMG_9291c.jpg'},
        {'date': 'ap950617.html', 'link': ''},
    ]

    ilp = image_link_parser.image_link_parser(base_url='https://apod.nasa.gov/apod/', coding='utf-8-sig')
    validator = lambda l: l.startswith('image') and l.endswith('.jpg')

    for test_case in test_array:
        link = ilp.parse(test_case['date'], validator)
        if (0 < len(link)):
            assert(link[0] == test_case['link'])
            print(link[0] + " == " + test_case['link'])

def test_args_parser():

    arg_date = arg_parser.get_date_from_args('test_modules.py --date 2007-09-11'.split())

    assert(datetime.datetime(2007, 9, 11).year == arg_date.year)
    assert(datetime.datetime(2007, 9, 11).month == arg_date.month)
    assert(datetime.datetime(2007, 9, 11).day == arg_date.day)

    arg_date = arg_parser.get_date_from_args('test_modules.py --today'.split())

    today = datetime.datetime.now()
    assert(today.year == arg_date.year)
    assert(today.month == arg_date.month)
    assert(today.day == arg_date.day)

def test_image_resolution():
    test_img_resolution = (1710, 1312)
    test_img = os.path.abspath("tests/img/test_img.png")

    img_resolution = image_resolution.get_image_resolution(test_img)

    assert(test_img_resolution == img_resolution)

    test_screen_resolution = (2560, 1080)
    assert(False == image_resolution.is_image_good_resolution(test_screen_resolution, test_img_resolution))

    test_screen_resolution2 = (1680, 720)
    assert(True == image_resolution.is_image_good_resolution(test_screen_resolution2, test_img_resolution))

def test_screen():
    #Not sure how to test it :P
    s = screen.screen()
    screen_res = s.get_screen_resolution()
    print(screen_res)
    screen_ratio = s.get_screen_ratio(screen_res[0], screen_res[1])
    print(screen_ratio)

def test_database_config():
    db_info = db_config.config(filename='resources/database.ini')
    print(db_info)

def test_database():
    db = database.Postgres()


if __name__ == "__main__":
    test_args_parser()
    test_apod_path()
    test_background()
    test_downloader()
    test_image_link_parser()
    test_image_resolution()
    test_screen()
    test_database_config()
    test_database()