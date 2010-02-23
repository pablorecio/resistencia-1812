# -*- coding: utf-8 -*-
###############################################################################
# This file is part of Resistencia Cadiz 1812.                                #
#                                                                             #
# This program is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by        #
# the Free Software Foundation, either version 3 of the License, or           #
# any later version.                                                          #
#                                                                             #
# This program is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of              #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
# GNU General Public License for more details.                                #
#                                                                             #
# You should have received a copy of the GNU General Public License           #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                             #
# Copyright (C) 2010, Pablo Recio Quijano, <pablo.recioquijano@alum.uca.es>   #
###############################################################################

"""
This module is an abstraction layer to manage configuration files
and works for XML using DOM
"""

import os
import shutil
from xml.dom import minidom

from resistencia import xdg

__config_base_path__ = xdg.get_config_dir() + '/'
__file_path__ = __config_base_path__ + 'configuration.xml'

def generate_configuration_file():
    """
    This function generate the default configuration file, in case that
    the file does not exists.
    """
    impl = minidom.getDOMImplementation()
    config_xml = impl.createDocument(None, 'config', None)
    
    top_element = config_xml.documentElement
    
    se_path = config_xml.createElement('se_path')
    se_real_path = os.path.realpath(__config_base_path__) + '/teams'
    se_path.setAttribute('value', se_real_path)
    if not os.path.exists(se_real_path):
        os.mkdir(se_real_path)
        os.mkdir(se_real_path + '/rules')
        os.mkdir(se_real_path + '/formations')
        data_path = xdg.get_data_path('teams/rules')
        files = os.listdir(data_path)
        for _file in files:
            _file = data_path + '/' + _file
            shutil.copy(os.path.realpath(_file), se_real_path + '/rules')
        data_path = xdg.get_data_path('teams/formations')
        files = os.listdir(data_path)
        for _file in files:
            _file = data_path + '/' + _file
            shutil.copy(os.path.realpath(_file), se_real_path + '/formations')

    games_path = config_xml.createElement('games_path')
    games_real_path = os.path.realpath(__config_base_path__ + '/games')
    games_path.setAttribute('value', games_real_path)
    if not os.path.exists(games_real_path):
        os.mkdir(games_real_path)

    language = config_xml.createElement('language')
    language.setAttribute('value', 'es_ES')

    active_music = config_xml.createElement('music_active')
    active_music.setAttribute('value', '1')

    top_element.appendChild(se_path)
    top_element.appendChild(games_path)
    top_element.appendChild(language)
    top_element.appendChild(active_music)

    file_xml = open(__file_path__,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()
        
def load_configuration():
    """
    Returns a dictionary with the data contained on the XML file
    """
    if not os.path.exists(__file_path__):
        generate_configuration_file()
    
    params = {}
    config_xml = minidom.parse(__file_path__)
    
    se_path = config_xml.getElementsByTagName('se_path')
    params['se_path'] = se_path[0].getAttribute('value')
    
    games_path = config_xml.getElementsByTagName('games_path')
    params['games_path'] = games_path[0].getAttribute('value')
    
    language = config_xml.getElementsByTagName('language')
    params['language'] = language[0].getAttribute('value')
    
    music_active = config_xml.getElementsByTagName('music_active')
    params['music_active'] = music_active[0].getAttribute('value')

    return params

def set_se_path(new_path):
    """
    Set a new 'System Expert Path'
    """
    config_xml = minidom.parse(__file_path__)
    se_path = config_xml.getElementsByTagName('se_path')[0]

    se_path.removeAttribute('value')
    se_path.setAttribute('value', os.path.realpath(new_path))

    file_xml = open(__file_path__,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()

def set_games_path(new_path):
    """
    Set a new 'Games Path'
    """
    config_xml = minidom.parse(__file_path__)
    games_path = config_xml.getElementsByTagName('games_path')[0]

    games_path.removeAttribute('value')
    games_path.setAttribute('value', os.path.realpath(new_path))

    file_xml = open(__file_path__,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()

def set_language(new_language):
    """
    Set a new language
    """
    config_xml = minidom.parse(__file_path__)
    language = config_xml.getElementsByTagName('language')[0]

    language.removeAttribute('value')
    language.setAttribute('value', new_language)

    file_xml = open(__file_path__,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()

def set_active_music(new_music_active):
    """
    Set or unset the music on the game
    """
    config_xml = minidom.parse(__file_path__)
    music_active = config_xml.getElementsByTagName('music_active')[0]
    
    music_active.removeAttribute('value')
    music_active.setAttribute('value', new_music_active)
    
    file_xml = open(__file_path__,"w")

    file_xml.write(config_xml.toprettyxml())
    file_xml.close()
