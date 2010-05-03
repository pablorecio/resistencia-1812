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

if __name__ == '__main__':
    clips.Eval('(clear)')
    clips.EngineConfig.Strategy = clips.RANDOM_STRATEGY
    random.seed()
    clips.Eval("(seed " + str(random.randint(0,9999)) + ")")

    clips_aux_functions.register_clips_functions(clips)

    environment = clips_main_environment.GuadaleteMainEnvironment(clips)
    environment.init_environment()

    submodules = [clips_main.ClipsSubModuleMain(clips),
                  clips_mover.ClipsSubModuleMover(clips),
                  clips_texto.ClipsSubModuleTexto(clips),
                  clips_traducir_ficha.ClipsTraducirFicha(clips),
                  clips_traducir_movimiento.ClipsTraducirMovimiento(clips)]

    for submodule in submodules:
        submodule.clips_load_submodule()

    clips.Load('../data/teams/formations/equipoA.clp')
    clips.Load('../data/teams/formations/equipoB.clp')

    clips_A_team.ClipsSubModuleATeam().clips_load_submodule(clips)
    clips.Load('../data/teams/rules/reglasA.clp')
    clips_B_team.ClipsSubModuleATeam().clips_load_submodule(clips)
    clips.Load('../data/teams/rules/reglasB.clp')

    clips.Reset() #restart the environment

    clips.Run() #start the simulation
    t = clips.StdoutStream.Read() #print the output
    print t
