# -*- coding: utf-8 -*-

from xml.dom import minidom

import layout

xml_doc = minidom.parse('xml_prueba.xml')
window_board = xml_doc.firstChild

childs = window_board.childNodes

layout.erase_childs_end_of_line(childs)

dic = {}

for element in childs:
    tag = element.tagName
    attr = element.getAttribute('type')

    x = eval('layout.parse_' + tag + '_' + attr + '(element)')
    dic[element.getAttribute('name')] = x

print dic['board']['board_size']
