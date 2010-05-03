#!/usr/bin/env python

import random

import clips

import clips_main_environment
import clips_aux_functions
import clips_main
import clips_mover
import clips_texto
import clips_traducir_ficha
import clips_traducir_movimiento
import clips_A_team
import clips_B_team

clips.Eval('(clear)')
clips.EngineConfig.Strategy = clips.RANDOM_STRATEGY
random.seed()
clips.Eval("(seed " + str(random.randint(0,9999)) + ")")

clips_aux_functions.register_clips_functions(clips)

environment = clips_main_environment.GuadaleteMainEnvironment(clips)
environment.init_environment()
submod_main = clips_main.ClipsSubModuleMain(clips)
              
submodules = [clips_mover.ClipsSubModuleMover(clips),
              clips_texto.ClipsSubModuleTexto(clips),
              clips_traducir_ficha.ClipsSubModuleTraducirFicha(clips),
              clips_traducir_movimiento.ClipsSubModuleTraducirMovimiento(clips)]

submod_main.clips_load_submodule()

clips.Load('../data/teams/formations/equipoA.clp')
clips.Load('../data/teams/formations/equipoB.clp')

clips.PrintDeffacts()

for submodule in submodules:
    submodule.clips_load_submodule()

clips_A_team.ClipsSubModuleBaseATeam(clips).clips_load_submodule()
clips.Load('../data/teams/rules/reglasA.clp')
clips_B_team.ClipsSubModuleBaseBTeam(clips).clips_load_submodule()
clips.Load('../data/teams/rules/reglasB.clp')

clips.Reset() #restart the environment

clips.Run() #start the simulation
t = clips.StdoutStream.Read() #print the output
print t
