#!/usr/bin/env python

import random

import clips

from libguadalete import rules
from libguadalete.environment import GuadaleteMainEnvironment
from libguadalete.submodules import ClipsModule

clips.Eval('(clear)')
clips.EngineConfig.Strategy = clips.RANDOM_STRATEGY
random.seed()
clips.Eval("(seed " + str(random.randint(0,9999)) + ")")

environment = GuadaleteMainEnvironment()
environment.init_environment()

submod_main = ClipsModule(rules.main.rules, rules.main.module_name,
                          rules.main.module_body)

submodules = [ClipsModule(mod.rules, mod.module_name, mod.module_body)
              for mod in [rules.move, rules.text, rules.transpiece, rules.transmov]]

submod_main.clips_load_submodule()

clips.Load('../data/teams/formations/equipoPabloRecio.clp')
clips.Load('../data/teams/formations/equipoB.clp')

clips.PrintDeffacts()

for submodule in submodules:
    submodule.clips_load_submodule()

ClipsModule.clips_load_submodule(rules.a_team.rules, rules.a_team.module_name,
                                 rules.a_team.module_body)
clips.Load('../data/teams/rules/reglasPabloRecio.clp')
ClipsModule.clips_load_submodule(rules.b_team.rules, rules.b_team.module_name,
                                 rules.b_team.module_body)
clips.Load('../data/teams/rules/reglasB.clp')

clips.Reset() #restart the environment

clips.Run() #start the simulation
t = clips.StdoutStream.Read() #print the output
print t
