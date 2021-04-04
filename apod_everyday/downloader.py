import requests
from tqdm import tqdm

class downloader:

    def __init__(self, download_directory):
        self.download_directory = download_directory

    def download(self, url, output_name):
        r = requests.get(url, stream=True)

        #Check status code, 200 for OK
        if 200 == r.status_code:

            bar_divisor = 100
            total_size = int(r.headers.get('content-length', 0))
            block_size = total_size // bar_divisor
            bar_format = '{l_bar}{bar:'+ f'{bar_divisor}' + '}{r_bar}{bar:-10b}'

            progress_bar = tqdm(total=total_size, bar_format=bar_format)

            try: 
                with open(self.download_directory + output_name, 'wb') as f:
                    for chunk in r.iter_content(block_size):
                        progress_bar.update(len(chunk))
                        f.write(chunk)
                    progress_bar.close()
                    return True

            except OSError as err:
                print(f"OS error: {err}")
                return False
        else:
            return False

if __name__ == "__main__":
    pass
