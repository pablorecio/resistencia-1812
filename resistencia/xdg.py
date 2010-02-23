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
# Copyright (C) 2008-2009 Adam Olsen (Exaile project)                         #
###############################################################################

###############################################################################
# The following execution script was modified from the Exaile project, using
# it as base for the construction of this application.
# To get the original version see <http://www.exaile.org/>
###############################################################################
"""
File that allows to abstract the ubication of the app. This way, is
independent if the program is installed or not.
"""

import os

__homedir__ = os.path.expanduser("~")
__lastdir__ = __homedir__

__data_home__ = os.getenv("XDG_DATA_HOME")
if __data_home__ == None:
    __data_home__ = os.path.join(__homedir__, ".local", "share")
__data_home__ = os.path.join(__data_home__, "resistencia1812")
if not os.path.exists(__data_home__):
    os.makedirs(__data_home__)

__config_home__ = os.getenv("XDG_CONFIG_HOME")
if __config_home__ == None:
    __config_home__ = os.path.join(__homedir__, ".resistencia1812")
if not os.path.exists(__config_home__):
    os.makedirs(__config_home__)

__cache_home__ = os.getenv("XDG_CACHE_HOME")
if __cache_home__ == None:
    __cache_home__ = os.path.join(__homedir__, ".cache")
__cache_home__ = os.path.join(__cache_home__, "resistencia1812")
if not os.path.exists(__cache_home__):
    os.makedirs(__cache_home__)

__data_dirs__ = os.getenv("XDG_DATA_DIRS")
if __data_dirs__ == None:
    __data_dirs__ = "/usr/local/share/:/usr/share/:/opt/share/"
__data_dirs__ = [os.path.join(d, "resistencia1812/data")
             for d in __data_dirs__.split(":")]

__config_dirs__ = os.getenv("XDG_CONFIG_DIRS")
if __config_dirs__ == None:
    __config_dirs__ = "/etc/xdg"
__config_dirs__ = [os.path.join(d, "resistencia1812")
               for d in __config_dirs__.split(":")]

__res_dir__ = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
# Detect if Resistencia is not installed.
if os.path.exists(os.path.join(__res_dir__, 'Makefile')):
    __data_dir__ = os.path.join(__res_dir__, 'data')
    __data_dirs__.insert(0, __data_dir__)
    # Insert the "data" directory to __data_dirs__.
    # insert the config dir
    __config_home__ = os.path.join(__res_dir__, 'data')
    __config_dir__ = os.path.join(__res_dir__, 'data', 'config')
    __config_dirs__.insert(0, __config_dir__)

__data_dirs__.insert(0, __data_home__)

def get_config_dir():
    """
    Get the path to the main config directory
    """
    return __config_home__

def get_config_dirs():
    """
    Get the path to the config directories
    """
    return __config_dirs__

def get_data_dirs():
    """
    Get the path to the data directories
    """
    return __data_dirs__[:]

def get_cache_dir():
    """
    Get the path to the cache dirs
    """
    return __cache_home__

def get_data_path(*subpath_elements):
    """
    Get the path to the element on the data path
    """
    subpath = os.path.join(*subpath_elements)
    for _dir in __data_dirs__:
        path = os.path.join(_dir, subpath)
        if os.path.exists(path):
            return path
    return None

def get_config_path(*subpath_elements):
    """
    Get the path to the element on the config path
    """
    subpath = os.path.join(*subpath_elements)
    for _dir in __config_dirs__:
        path = os.path.join(_dir, subpath)
        if os.path.exists(path):
            return path
    return None

def get_last_dir():
    """
    Get the path to the last directory
    """
    return __lastdir__

# vim: et sts=4 sw=4

