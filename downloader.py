import requests

class Downloader:
    def __init__(self, download_directory):
        self.download_directory = download_directory

    def download(self, url, output_name):
        r = requests.get(url)
        try: 
            with open(self.download_directory + output_name, 'wb') as f:
                f.write(r.content)
                return True

        except OSError as err:
            print(f"OS error: {err}")
            return False

if __name__ == "__main__":

    test_array = [
        {'url' : 'https://apod.nasa.gov/apod/image/2010/STScI_NGC2525_1865x2000.jpg', 'output_name': 'ap201023.jpg'},
        {'url' : 'https://apod.nasa.gov/apod/image/2102/LunarHalo_Strand_1500.jpg', 'output_name': '210201.jpg'},
        {'url' : 'https://apod.nasa.gov/apod/image/2101/NGC1316Center_HubbleNobre_2585.jpg', 'output_name': 'ap210126.jpg'},
        {'url' : 'https://apod.nasa.gov/apod/image/2012/2020Dec14TSE_Ribas_IMG_9291c.jpg', 'output_name': 'ap201218.jpg'}
    ]

    d = Downloader('/tmp/')

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