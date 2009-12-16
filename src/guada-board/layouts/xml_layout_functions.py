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


def _parse_propierty_string(node):
    data = node.firstChild.data
    data = data.replace("\n",'')
    data = data.replace(' ' , '')

    return data

def erase_childs_end_of_line(node):
    for child in node:
        if child.nodeType == 3: #TextType
            node.remove(child)

def parse_propierty_image(node):
    return _parse_propierty_string(node)

def parse_propierty_font(node):
    return _parse_propierty_string(node)

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
    childs = node.childNodes

    erase_childs_end_of_line(childs)
    propierties = {}

    for propierty in childs:
        function_call = 'parse_propierty_' + propierty.getAttribute('type')
        function_call += '(propierty)'
        propierties[propierty.getAttribute('name')] = eval(function_call)

    return propierties
