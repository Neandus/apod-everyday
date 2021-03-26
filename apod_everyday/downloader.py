import requests

class downloader:
    def __init__(self, download_directory):
        self.download_directory = download_directory

    def download(self, url, output_name):

        r = requests.get(url, stream=True)

        #Check status code, 200 for OK
        if 200 == r.status_code:
            try: 
                with open(self.download_directory + output_name, 'wb') as f:
                    f.write(r.content)
                    return True

            except OSError as err:
                print(f"OS error: {err}")
                return False

if __name__ == "__main__":
    pass
