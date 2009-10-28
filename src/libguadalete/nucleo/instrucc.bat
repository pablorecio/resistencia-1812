#
# Por Manuel Palomo Duarte, 2007
# Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
#
# Para ejecutar CLIPS y recoger la salida en 
#  un fichero de texto se puede hacer:
# exec clips -f instrucc.bat > salida.log
#
#
#

(clear)
(set-strategy random)
(seed 1234)
(load* "funciones.clp")
(load* "f1.clp")
(load* "mover.clp")
(load* "texto.clp")
(load* "traducirF.clp")
(load* "traducirM.clp")

(load* "./equipoA.clp")
(load* "./equipoB.clp")

(load* "fA.clp")
(load* "./reglasA.clp")
(load* "fB.clp")
(load* "./reglasB.clp")
(reset)
(facts)

(watch facts *)

(run)
;(facts)
;(exit)
