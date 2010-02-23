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

"""
This module contains the functions that defines the way that the xml-layout
file should be processed.
"""

from resistencia import xdg

def _parse_propierty_data_string(node):
    """
    Parses an string
    """
    data = node.firstChild.data
    data = data.replace("\n",'')
    data = data.replace(' ' , '')

    return data

def _parse_childs(node):
    """
    Parses the childs of a node calling its funciones
    """
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
    """
    Removes the childs at end of line
    """
    for child in node:
        if child.nodeType == 3: #TextType
            node.remove(child)

def parse_propierty_image(node):
    """
    Parses an image
    """
    return xdg.get_data_path(_parse_propierty_data_string(node))

def parse_propierty_font(node):
    """
    Parses a font
    """
    return xdg.get_data_path(_parse_propierty_data_string(node))

def parse_propierty_string(node):
    """
    Parses an string
    """
    return _parse_propierty_data_string(node)

def parse_propierty_title_string(node):
    """
    Parses a title 
    """
    data = node.firstChild.data
    data = data.replace("\n",'')

    return data

def parse_propierty_int(node):
    """
    Parses an integer
    """
    return int(_parse_propierty_data_string(node))

def parse_propierty_color(node):
    """
    Parses a color
    """
    childs = node.childNodes

    erase_childs_end_of_line(childs)
    
    for child in childs:
        if child.hasAttribute('id'):
            attr = child.getAttribute('id')
            if attr == 'r':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                _red = int(aux)
            if attr == 'g':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                _green = int(aux)
            if attr == 'b':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                _blue = int(aux)
    
    return (_red, _green, _blue)

def parse_propierty_size(node):
    """
    Parses a size element
    """
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
    
    return (weight, height)

def parse_propierty_button_images(node):
    """
    Parses the button images
    """
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
    
    return (default, above, pressed)

def parse_propierty_position(node):
    """
    Parses the position
    """
    childs = node.childNodes

    erase_childs_end_of_line(childs)

    for child in childs:
        if child.hasAttribute('id'):
            attr = child.getAttribute('id')
            if attr == 'x':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                _x_ = int(aux)
            if attr == 'y':
                aux = child.firstChild.data
                aux.replace("\n", '')
                aux.replace(' ', '')
                _y_ = int(aux)
    
    return (_x_, _y_)

def parse_label_dynamic_surface(node):
    """
    Parses a dynamic surface
    """
    return _parse_childs(node)

def parse_label_names(node):
    """
    Parses the names of the players
    """
    return _parse_childs(node)

def parse_label_buttons(node):
    """
    Parses the main buttons
    """
    return _parse_childs(node)

def parse_label_button(node):
    """
    Parses a single button
    """
    return _parse_childs(node)

def parse_label_child_in_label(node): #labels with the player's name
    """
    Parses the childs of a label
    """
    return _parse_childs(node)

def parse_label_child_button(node):
    """
    Parses the childs of a button
    """
    return _parse_childs(node)
    
