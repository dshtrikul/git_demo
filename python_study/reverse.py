import pprint
# import xml.dom.minidom
# from xml.dom.minidom import Node
#
# doc = xml.dom.minidom.parse('book.xml')
# mapping = {}
#
# for node in doc.getElementsByTagName('book'):
#     isbn = node.getAttribute('isbn')
#
#     L = node.getElementsByTagName('title')
#     for node2 in L:
#         title = ''
#         for node3 in node2.childNodes:
#             if node3.nodeType == Node.TEXT_NODE:
#                 title += node3.data
#         mapping[isbn] = title
#
# pprint.pprint(mapping)
# ___________________________________________________

from xml.etree.ElementTree import parse, Element

mapping = {}

tree = parse('book.xml')
# for item in tree.findall('book'):
#     isbn = item.attrib['isbn']
#     for item2 in item.findall('title'):
#         mapping[isbn] = item2.text

for item in tree.iter('book'):
    item.attrib['isbn'] += "-000"
    item.append(Element('newelement'))
    print(item.attrib['isbn'])

for item in tree.iter('book'):
    for item2 in item.findall('newelement'):
        item2.text = "99999"

tree.write('newbook.xml')




# pprint.pprint(mapping)