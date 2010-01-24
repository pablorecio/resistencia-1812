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

import os

homedir = os.path.expanduser("~")
lastdir = homedir

data_home = os.getenv("XDG_DATA_HOME")
if data_home == None:
    data_home = os.path.join(homedir, ".local", "share")
data_home = os.path.join(data_home, "resistencia1812")
if not os.path.exists(data_home):
    os.makedirs(data_home)

config_home = os.getenv("XDG_CONFIG_HOME")
if config_home == None:
    config_home = os.path.join(homedir, ".resistencia1812")
if not os.path.exists(config_home):
    os.makedirs(config_home)

cache_home = os.getenv("XDG_CACHE_HOME")
if cache_home == None:
    cache_home = os.path.join(homedir, ".cache")
cache_home = os.path.join(cache_home, "resistencia1812")
if not os.path.exists(cache_home):
    os.makedirs(cache_home)

data_dirs = os.getenv("XDG_DATA_DIRS")
if data_dirs == None:
    data_dirs = "/usr/local/share/:/usr/share/:/opt/share/"
data_dirs = [os.path.join(d, "resistencia1812/data") for d in data_dirs.split(":")]

config_dirs = os.getenv("XDG_CONFIG_DIRS")
if config_dirs == None:
    config_dirs = "/etc/xdg"
config_dirs = [os.path.join(d, "resistencia1812") for d in config_dirs.split(":")]

resistencia_dir = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
# Detect if Resistencia is not installed.
if os.path.exists(os.path.join(resistencia_dir, 'Makefile')):
    data_dir = os.path.join(resistencia_dir, 'data')
    data_dirs.insert(0, data_dir)
    # Insert the "data" directory to data_dirs.
    # insert the config dir
    config_home = os.path.join(resistencia_dir, 'data')
    config_dir = os.path.join(resistencia_dir, 'data', 'config')
    config_dirs.insert(0, config_dir)

data_dirs.insert(0, data_home)

def get_config_dir():
    return config_home

def get_config_dirs():
    return config_dirs

def get_data_dirs():
    return data_dirs[:]

def get_cache_dir():
    return cache_home

def get_data_path(*subpath_elements):
    subpath = os.path.join(*subpath_elements)
    for dir in data_dirs:
        path = os.path.join(dir, subpath)
        if os.path.exists(path):
            return path
    return None

def get_config_path(*subpath_elements):
    subpath = os.path.join(*subpath_elements)
    for dir in config_dirs:
        path = os.path.join(dir, subpath)
        if os.path.exists(path):
            return path
    return None

def get_last_dir():
    return lastdir

# vim: et sts=4 sw=4

