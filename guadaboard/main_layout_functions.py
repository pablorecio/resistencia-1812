# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# This file is part of Resistencia Cadiz 1812.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

import os
import sys
from xml.dom import minidom

from resistencia import xdg

def _parse_propierty_data_string(node):
    data = node.firstChild.data
    data = data.replace("\n",'')
    data = data.replace(' ' , '')

    return data

def _parse_childs(node):
    childs = node.childNodes

    erase_childs_end_of_line(childs)
    propierties = {}

    for propierty in childs:
        tag = propierty.tagName
        attr = propierty.getAttribute('type')
        function_call = 'parse_' + tag + '_' + attr
        function_call += '(propierty)'
        propierties[propierty.getAttribute('name')] = eval(function_call)

    return propierties

def erase_childs_end_of_line(node):
    for child in node:
        if child.nodeType == 3: #TextType
            node.remove(child)

def parse_propierty_image(node):
    return xdg.get_data_path(_parse_propierty_data_string(node))

def parse_propierty_font(node):
    return xdg.get_data_path(_parse_propierty_data_string(node))

def parse_propierty_string(node):
    return _parse_propierty_data_string(node)

def parse_propierty_title_string(node):
    data = node.firstChild.data
    data = data.replace("\n",'')

    return data

def parse_propierty_int(node):
    return int(_parse_propierty_data_string(node))

def parse_propierty_color(node):
    childs = node.childNodes

    erase_childs_end_of_line(childs)
    
    for child in childs:
        if child.hasAttribute('id'):
            attr = child.getAttribute('id')
            if attr == 'r':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                r = int(aux)
            if attr == 'g':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                g = int(aux)
            if attr == 'b':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                b = int(aux)
    
    return (r,g,b)

def parse_propierty_size(node):
    childs = node.childNodes

    erase_childs_end_of_line(childs)

    for child in childs:
        if child.hasAttribute('id'):
            attr = child.getAttribute('id')
            if attr == 'weight':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                weight = int(aux)
            if attr == 'height':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                height = int(aux)
    
    return (weight,height)

def parse_propierty_button_images(node):
    childs = node.childNodes

    erase_childs_end_of_line(childs)
    
    for child in childs:
        if child.hasAttribute('id'):
            attr = child.getAttribute('id')
            if attr == 'default':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                default = xdg.get_data_path(aux)
            if attr == 'above':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                above = xdg.get_data_path(aux)
            if attr == 'pressed':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                pressed = xdg.get_data_path(aux)
    
    return (default,above,pressed)

def parse_propierty_position(node):
    childs = node.childNodes

    erase_childs_end_of_line(childs)

    for child in childs:
        if child.hasAttribute('id'):
            attr = child.getAttribute('id')
            if attr == 'x':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                x = int(aux)
            if attr == 'y':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                y = int(aux)
    
    return (x,y)

def parse_label_dynamic_surface(node):
    return _parse_childs(node)

def parse_label_names(node):
    return _parse_childs(node)

def parse_label_buttons(node):
    return _parse_childs(node)

def parse_label_button(node):
    return _parse_childs(node)

def parse_label_child_in_label(node): #labels with the player's name
    return _parse_childs(node)

def parse_label_child_button(node):
    return _parse_childs(node)
    
