def LoadFunctions(clips):
    ficha_r = clips.BuildTemplate("ficha-r",
                                  "(slot equipo) (slot num) (slot puntos) (slot pos-x) (slot pos-y) (slot descubierta)")

    ficha = clips.BuildTemplate("ficha", 
                                "(slot equipo) (slot num) (slot puntos) (slot pos-x) (slot pos-y) (slot descubierta)")

    mueve = clips.BuildTemplate("mueve", 
                                "(slot num) (slot mov) (slot tiempo)")

    opciones_juego = clips.BuildDeffacts("opciones-juego", 
                                         '(tiempo 200) (dimension 8) (turno "A") (base "A" 1) (base "B" 8) (modulos INFORMAR TRADUCIRF EQUIPO-A TRADUCIRM MOVER INFORMAR TRADUCIRF EQUIPO-B TRADUCIRM MOVER)')
    
    mod_main = clips.BuildModule("MAIN",
                                 "(export deftemplate initial-fact ficha ficha-r dimension tiempo mueve) (export deffunction ?ALL))")

    borra_fich = mod_main.BuildRule("borra-fich", 
                                    "(declare (salience 100)) (not (fichero-abierto))", 
                                    '(printout t crlf "BORRANDO FICHERO" crlf) (assert (fichero-abierto)) (open "temporal.txt" fich "w") (close fich)')

    control_y_tiempo = mod_main.BuildRule("control-y-tiempo",
                                          "?c <- (tiempo ?t&~0) ?orden <- (modulos INFORMAR $?r)",
                                          '(retract ?c) (assert (tiempo (- ?t 1))) (retract ?orden) (assert (modulos $?r INFORMAR)) (printout t "Tiempo " ?t crlf) (focus INFORMAR)')

    control_sin_tiempo = mod_main.BuildRule("control-sin-tiempo",
                                            '?c <- (tiempo ?t&~0) ?orden <- (modulos ?m&~INFORMAR $?r) (ficha-r (equipo "A") (puntos 1)) (ficha-r (equipo "B") (puntos 1))','(retract ?orden) (assert (modulos $?r ?m)) (focus ?m)')
