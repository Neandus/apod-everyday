import datetime

# module gets date and translate it to url apod path
class apod_path:
    def __init__(self):
        self.prefix = 'ap'
        self.postfix = '.html'
    
    def parse_date(self, date):
        apod_date = None

        if type(date) == str:
            apod_date = date.replace("/", "")
        else:
            apod_date = datetime.datetime.now().strftime("%y%m%d")

        url_path = self.prefix + apod_date + self.postfix

        return url_path

if __name__ == "__main__":
    pass