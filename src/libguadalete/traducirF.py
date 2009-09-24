def LoadFunctions(clips):
    mod_traducir = clips.BuildModule("TRADUCIRF",
                                     "(import MAIN deftemplate initial-fact ficha ficha-r dimension tiempo) (import MAIN deffunction ?ALL)")

    inicial1 = mod_traducir.BuildRule("inicial1",
                                      "(declare (salience 100)) (tiempo ?t)",
                                      '(printout t "**********************************" crlf )')

    inicial1_2 = mod_traducir.BuildRule("inicial1",
                                        "(declare (salience 100)) (tiempo ?t) (test (= 0 (mod ?t 2)))",
                                        '(assert (equipoA ?t "B"))')

    inicial2 = mod_traducir.BuildRule("inicial2",
                                      "(declare (salience 100)) (tiempo ?t) (test (<> 0 (mod ?t 2)))",
                                      '(assert (equipoA ?t "A"))')

    elimina1 = mod_traducir.BuildRule("elimina1", "(declare (salience 20)) (tiempo ?t) ?h <- (ficha (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta ?d)) (not (limpia ?t))",
                                      "(retract ?h)")

    elimina2 = mod_traducir.BuildRule("elimina2",
                                      "(declare (salience 19)) (tiempo ?t)",
                                      '(printout t "*Limpiado" ?t  crlf) (assert (limpia ?t))')

    directo_0A = mod_traducir.BuildRule("directo-0A",
                                        '(declare (salience 10)) (tiempo ?t) (equipoA ?t "A") (ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))',
                                        '(assert (ficha (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0)))')

    directo_0B = mod_traducir.BuildRule("directo-0B",
                                        '(declare (salience 10)) (tiempo ?t) (equipoA ?t "A") (ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))',
                                        '(assert (ficha (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos 0) (descubierta 0)))')

    directo_1 = mod_traducir.BuildRule("directo-1",
                                       '(declare (salience 10)) (tiempo ?t) (equipoA ?t "A") (ficha-r (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))',
                                       "(assert (ficha (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1)))")

    indirecto_0A = mod_traducir.BuildRule("indirecto-0A",
                                          '(declare (salience 10)) (tiempo ?t) (equipoA ?t "B") (ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))',
                                          '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos 0) (descubierta 0)))')

    indirecto_0B = mod_traducir.BuildRule("indirecto-0B",
                                          '(declare (salience 10)) (tiempo ?t) (equipoA ?t "B") (ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))',
                                          '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 0)))')

    indirecto_1A = mod_traducir.BuildRule("indirecto-1A",
                                          '(declare (salience 10)) (tiempo ?t) (equipoA ?t "B") (ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))',
                                          '(assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 1)))')

    indirecto_1B = mod_traducir.BuildRule("indirecto-1B",
                                          '(declare (salience 10)) (tiempo ?t) (equipoA ?t "B") (ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))',
                                          '(assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 1)))')
