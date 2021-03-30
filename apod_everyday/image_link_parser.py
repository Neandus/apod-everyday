from lxml import etree
from io import StringIO
import requests

class image_link_parser:

    def __init__(self, base_url, coding):
        self.base_url = base_url
        self.parser = etree.HTMLParser()
        self.coding = coding

    def get_html_tree(self, date):
        page = requests.get(self.base_url + date)

        if 200 == page.status_code:

            # Decode the page in the right encoding
            html = page.content.decode(self.coding)

            # Create your etree with a StringIO object which functions similarly
            # to a fileHandler
            tree = etree.parse(StringIO(html), parser=self.parser)

            return tree
        else:

            print(f"The requested URL {self.base_url + date} was not found on this server.")

            return None

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

        if tree is not None:
            return self.get_links(tree, validator)
        else:
            return []

if __name__ == "__main__":
    pass
