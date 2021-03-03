from lxml import etree
import lxml.html
from .. import cleaner

def zhejiangzfcg_modifier(response):
    content = cleaner.clean_html(response)
    body = lxml.html.fromstring(content)
    try:
        etree.strip_elements(body,"script","style","title")
        content = etree.tostring(body,encoding='utf-8')
        data = content.decode('utf-8')
    except Exception as e:
        raise e
    return data