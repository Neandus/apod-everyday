import apod_path
import arg_parser
import image_link_parser
import downloader
import background
import sys

apod_base_url = 'https://apod.nasa.gov/apod/'

def main(args=None):

    apod_date = arg_parser.get_date_from_args(args)

    if apod_date is None:
        print("Could not parse date to continue.")
        exit(-1)

    url_path = apod_path.apod_path().parse_date(apod_date)

    link_parser = image_link_parser.image_link_parser(apod_base_url, 'utf-8-sig')
    validator = lambda l: l.startswith('image') and l.endswith('.jpg')

    link = link_parser.parse(url_path, validator)
    
    if len(link) <= 0:
        print("Could not parse link for specified date.")
        exit(-2)

    d = downloader.downloader('/tmp/')
    
    image_filename = url_path.replace('.html', '.jpg')

    print('Downloading, this may take some time...')
    if False == d.download(apod_base_url + link[0], image_filename):
        print("Could not download image for specified date.")
        exit(-3)

    b = background.background('/tmp')

    if 0 != b.set_new(image_filename):
        print("Could not set image as background.")
        exit(-4)


if __name__ == "__main__":
    main(sys.argv)