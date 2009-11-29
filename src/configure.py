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

# This module is an abstraction layer to manage configuration files
# and works for XML using DOM

import os
import sys
from xml.dom import minidom

file_path = './configuration.xml'

def generate_configuration_file():
    impl = minidom.getDOMImplementation()
    config_xml = impl.createDocument(None, 'config', None)
    
    top_element = config_xml.documentElement
    
    se_path = config_xml.createElement('se_path')
    se_path.setAttribute('value', os.path.realpath('./teams'))
    
    games_path = config_xml.createElement('games_path')
    games_path.setAttribute('value', os.path.realpath('./games'))

    language = config_xml.createElement('language')
    language.setAttribute('value', 'es_ES')

    top_element.appendChild(se_path)
    top_element.appendChild(games_path)
    top_element.appendChild(language)

    file_xml = open(file_path,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()
        
def load_configuration():
    if not os.path.exists(file_path):
        generate_configuration_file()
    
    params = {}
    config_xml = minidom.parse(file_path)
    
    se_path = config_xml.getElementsByTagName('se_path')
    params['se_path'] = se_path[0].getAttribute('value')
    
    games_path = config_xml.getElementsByTagName('games_path')
    params['games_path'] = games_path[0].getAttribute('value')
    
    language = config_xml.getElementsByTagName('language')
    params['language'] = language[0].getAttribute('value')

    return params

def set_se_path(new_path):
    config_xml = minidom.parse(file_path)
    se_path = config_xml.getElementsByTagName('se_path')[0]

    se_path.removeAttribute('value')
    se_path.setAttribute('value', os.path.realpath(new_path))

    file_xml = open(file_path,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()

def set_games_path(new_path):
    config_xml = minidom.parse(file_path)
    games_path = config_xml.getElementsByTagName('games_path')[0]

    games_path.removeAttribute('value')
    games_path.setAttribute('value', os.path.realpath(new_path))

    file_xml = open(file_path,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()

def set_language(new_language):
    config_xml = minidom.parse(file_path)
    language = config_xml.getElementsByTagName('language')[0]

    language.removeAttribute('value')
    language.setAttribute('value', new_language)

    file_xml = open(file_path,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()
