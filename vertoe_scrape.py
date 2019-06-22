## TODO make it run dynamically from input args, make it a little more user friendly, cleanup

import requests
import argparse
import bs4
import re
import json

# parser = argparse.ArgumentParser(
#     description='Options for scraping vertoe information'
# )

# parser.add_argument(
#     '--location',
#     '-l',
#     type=str,
#     default=None,
#     help='The location to scrape data from'
# )
# parser.add_argument(
#     '--output',
#     '-o',
#     type=str,
#     default=None,
#     help='File to output results to'
# )

# args = parser.parse_args()


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# url = 'https://vertoe.com/search?locality=la&lat=34.0522342&lng=-118.2436849&is_auto_location=0&drop=Jun+19%2C+2019+++++-+++++10%3A00+AM&pickup=&num_bags=1&is_search=1&cur_site=' ## la
url = 'https://vertoe.com/search?cur_site=search&cur_view=list&is_search=1&locality=san+diego&is_auto_location=0&lat=32.715738&lng=-117.1610838&drop=Jun+19%2C+2019+++++-+++++11%3A00+AM&pickup=&num_bags=1&final_listing_count=21' ## san diego
response = requests.get(url)
print(response.status_code)
soup = bs4.BeautifulSoup(response.content, features="html.parser")
# for script in soup.find_all("script", {"src":False}):
# pattern = re.compile(r"var markers = '(.*?)';$", re.MULTILINE | re.DOTALL)
# pattern = re.compile(r"var markers =", re.MULTILINE | re.DOTALL)
# pattern = re.compile(r"var markers = '(.*?)';$", re.MULTILINE | re.DOTALL)
pattern = re.compile(r"var markers = '(.*?)';$")
script = soup.find("script", text=pattern)
# print(response.content)
# x = re.search(pattern, str(script.text))
# print(script)
# print(type(script.text))
# print(x.string)
# print(response.content)
# with open('text.txt', wb) as save:
text = str(response.content)
m = re.search('var markers(.+?)new_markers', text)
# m = re.search("var markers = '(.*?)';$", text)
if m:
    found = m.group(1)
# print(found)
latlongs = []
regex_results = re.findall(r'(?:lat")(?:[^\.]*)(?:\.)(?:[^\.]*)(?:\.)[0123456789]+', found)
# print(regex_results.group(0))
for latlong in regex_results:
    print(latlong)


# p = re.compile('var markers = (.*);')        
# for script in soup.find_all("script", {"src":False}):
#     if script:
        
#         m = p.search(script.string)
#         print(m.group(1))


# import urllib3
# # import json
# # import re
# # from bs4 import BeautifulSoup

# web = urllib3.urlopen("https://vertoe.com/search?locality=la&lat=34.0522342&lng=-118.2436849&is_auto_location=0&drop=Jun+19%2C+2019+++++-+++++10%3A00+AM&pickup=&num_bags=1&is_search=1&cur_site=")
# soup = bs4.BeautifulSoup(web.read(), 'lxml')
# data  = soup.find_all("script")[19].string
# p = re.compile('var table_body = (.*?);')
# m = p.match(data)
# stocks = json.loads(m.groups()[0])

# for stock in stocks:
#     print(stock)


# from bs4 import BeautifulSoup
# from slimit import ast
# from slimit.parser import Parser
# from slimit.visitors import nodevisitor
# import requests


# url = 'https://vertoe.com/search?locality=la&lat=34.0522342&lng=-118.2436849&is_auto_location=0&drop=Jun+19%2C+2019+++++-+++++10%3A00+AM&pickup=&num_bags=1&is_search=1&cur_site='
# response = requests.get(url)
# print(response.status_code)

# data = """
# <script>
# var my = 'hello';
# var name = 'hi';
# var is = 'halo';
# </script>
# """

# soup = BeautifulSoup(response.content, "html.parser")

# script = soup.find("script", text=lambda text: text and "var markers" in text)

# # parse js
# parser = Parser()
# tree = parser.parse(script.text)
# for node in nodevisitor.visit(tree):
#     if isinstance(node, ast.VarDecl) and node.identifier.value == 'my':
#         print(node.initializer.value)

# from bs4 import BeautifulSoup
# from slimit import ast
# from slimit.parser import Parser
# from slimit.visitors import nodevisitor
# import requests


# url = 'https://vertoe.com/search?locality=la&lat=34.0522342&lng=-118.2436849&is_auto_location=0&drop=Jun+19%2C+2019+++++-+++++10%3A00+AM&pickup=&num_bags=1&is_search=1&cur_site='
# response = requests.get(url)

# data = """
# <script>
# var someVar = new something.Something({
#     content: 'This text has to be found<br /><table></table>',
#     size: 230
# });
# </script>
# """
# text_to_find = 'var marker'

# soup = BeautifulSoup(response.content)

# for script in soup.find_all('script'):
#     parser = Parser()
#     tree = parser.parse(script.text)
#     for node in nodevisitor.visit(tree):
#         if isinstance(node, ast.Assign):
#             value = getattr(node.right, 'value', '')
#             if text_to_find in value:
#                 print(value)