from lxml import etree
import lxml.html
from io import StringIO,BytesIO

broken_html = '<html><head><title>test<body><h1>page title</h1><a href="hupu">aa</a>'
parser = etree.HTMLParser()
tree = etree.parse(StringIO(broken_html), parser)
#tree = lxml.html.fromstring(broken_html)
#ele = tree.xpath('.//div[@class="AfficheAccessory"]')
#for  child in ele:
#    child.set("class","sun")

print(etree.tostring(tree,encoding='utf-8'))