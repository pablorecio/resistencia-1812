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

# Copyright (C) 2007, Manuel Palomo Duarte
# Copyright (C) 2009, Pablo Recio Quijano
#----------------------------------------------------------------------

"""
 @file f1.clp

 Core's main file. Defines the mains templates, modules and rules. It
 has the responsibility to initialize the game's world.
"""

def LoadFunctions(clips): #Maybe add number of turns, dimension, etc
    #---------------------------------
    # We define ficha-r's template that is the real piece the system uses
    #----------------------------------
    # Template name
    template_name = "ficha-r"
    # Template body
    template_body  = "(slot equipo)"
    template_body += "(slot num)"
    template_body += "(slot puntos)"
    template_body += "(slot pos-x)"
    template_body += "(slot pos-y)"
    template_body += "(slot descubierta)"
    # Building the template
    ficha_r = clips.BuildTemplate(template_name, template_body)
    # ---------------------------------
    
    #---------------------------------
    # We define ficha's template, the one that modules uses on the calcs
    #----------------------------------
    # Template name
    template_name = "ficha"
    # Template body
    template_body  = "(slot equipo)"
    template_body += "(slot num)"
    template_body += "(slot puntos)"
    template_body += "(slot pos-x)"
    template_body += "(slot pos-y)"
    template_body += "(slot descubierta)"
    # Building the template
    ficha = clips.BuildTemplate(template_name, template_body)
    # ---------------------------------
    
    #---------------------------------
    # Movement template. The movs are:
    # -------- 1 - Increase x
    # -------- 2 - Decrease x
    # -------- 3 - Increase y
    # -------- 4 - Decrease y
    #----------------------------------
    # Template name
    template_name = "mueve"
    # Template body
    template_body  = "(slot num)"
    template_body += "(slot mov)"
    template_body += "(slot tiempo)"
    # Building the template
    mueve = clips.BuildTemplate(template_name, template_body)
    # ---------------------------------
    
    #---------------------------------
    # We define max movements on a match (of both team), board
    # dimension and modules control.
    #----------------------------------
    # Variables. Now are statics, but in a future maybe will be
    # customizable, so is more generical this way
    num_turns = 200
    dimension = 8
    turn = 'A'
    base_a = 1
    base_b = dimension
    # Deffacts name
    deffacts_name = "opciones-juego"
    # Deffacts body
    deffacts_body  = "(tiempo-inicial " + str(num_turns) + ")"
    deffacts_body += "(dimension " + str(dimension) + ")"
    deffacts_body += '(turno "' + turn + '")'
    deffacts_body += 'base "A" ' + str(base_a) + ')'
    deffacts_body += 'base "B" ' + str(base_b) + ')'
    deffacts_body += '(modulos INFORMAR TRADUCIRF EQUIPO-A MOVER INFORMAR TRADUCIRF EQUIPO-B TRADUCIRM MOVER)'
    # Building the Deffact
    opciones_juego = clips.BuildDeffacts(deffacts_name, deffacts_body)
    # ---------------------------------
    
    #----------------------------------
    # MAIN module (redefines the one of the system).
    # It handles to control game time and to summon modules
    # INFORMAR ATAQUE y DEFENSA to realize movements
    #----------------------------------
    # Module name
    mod_main_name = "MAIN"
    # Module body
    mod_main_body  = "(export deftemplate initial-fact ficha ficha-r dimension tiempo mueve turno tiempo-inicial)"
    mod_main_body += "(export deffunction ?ALL)"
    # Building the module
    mod_main = clips.BuildModule(mod_main_name, mod_main_body)
    #----------------------------------
