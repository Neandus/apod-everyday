from lxml import etree
from io import StringIO
import requests

class ImageLinkParser:

    def __init__(self, base_url, coding):
        self.base_url = base_url
        self.parser = etree.HTMLParser()
        self.coding = coding

    def get_html_tree(self, date):
        page = requests.get(self.base_url + date)

        # Decode the page in the right encoding
        html = page.content.decode(self.coding)

        # Create your etree with a StringIO object which functions similarly
        # to a fileHandler
        tree = etree.parse(StringIO(html), parser=self.parser)

        return tree

    # Call this function and pass in your tree
    def get_links(self, tree, validator):
        # This will get the anchor tags <a href...>
        refs = tree.xpath("//a")

        # Get the url from the ref
        links = [link.get('href', '') for link in refs]

        # Return a list that pass validator
        return [l for l in links if validator(l)]

    def parse(self, date, validator):
        tree = self.get_html_tree(date)
        return self.get_links(tree, validator)

if __name__ == "__main__":

    test_array = [
        {'date': 'ap201023.html', 'link': 'image/2010/STScI_NGC2525_1865x2000.jpg'},
        {'date': 'ap210216.html', 'link': ''},
        {'date': 'ap210201.html', 'link': 'image/2102/LunarHalo_Strand_1500.jpg'},
        {'date': 'ap210126.html', 'link': 'image/2101/NGC1316Center_HubbleNobre_2585.jpg'},
        {'date': 'ap201218.html', 'link': 'image/2012/2020Dec14TSE_Ribas_IMG_9291c.jpg'}
    ]

    ilp = ImageLinkParser(base_url='https://apod.nasa.gov/apod/', coding='utf-8-sig')
    validator = lambda l: l.startswith('image') and l.endswith('.jpg')

    for test_case in test_array:
        link = ilp.parse(test_case['date'], validator)
        if (0 < len(link)):
            assert(link[0] == test_case['link'])
            print(link[0] + " == " + test_case['link'])

