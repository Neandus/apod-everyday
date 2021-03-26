from .context import apod_everyday

apod_base_url = 'https://apod.nasa.gov/apod/'

ap = apod_path.apod_path()
url_path = ap.parse_date('21/03/23')
print(apod_base_url)
print(url_path)
i = image_link_parser.image_link_parser(apod_base_url, 'utf-8-sig')
validator = lambda l: l.startswith('image') and l.endswith('.jpg')

link = i.parse(url_path, validator)
print(apod_base_url + link[0])

d = downloader.downloader('/tmp/')
d.download(apod_base_url + link[0], 'test.jpg')
print('got it, set background')

b = background.background('/tmp')
b.set_new('test.jpg')