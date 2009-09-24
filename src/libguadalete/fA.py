def LoadFunctions(clips):
    mod_equipoA = clips.BuildModule("EQUIPO-A",
                                    "(import MAIN deftemplate initial-fact ficha dimension tiempo mueve) (import MAIN deffunction ?ALL)")

    basica1 = mod_equipoA.BuildRule("basica1",
                                    '(declare (salience 1)) (tiempo ?t) (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y)) (dimension ?dim&:(< ?x (/ ?dim 2))) (not (ficha (equipo "A") (pos-x ?x2&:(= ?x2 (+ ?x 1))) (pos-y ?y)))',
                                    '(printout t "EQUIPO-A mueve a" ?n " hacia 1 en t " ?t crlf) (assert (mueve (num ?n) (mov 1) (tiempo ?t)))')

    basica2 = mod_equipoA.BuildRule("basica2",
                                    '(declare (salience 1)) (tiempo ?t) (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y)) (dimension ?dim&:(> ?x (/ ?dim 2))) (not (ficha (equipo "A") (pos-x ?x2&:(= ?x2 (- ?x 1))) (pos-y ?y)))',
                                    '(printout t "EQUIPO-A mueve a" ?n " hacia 2 en t " ?t crlf) (assert (mueve (num ?n) (mov 2) (tiempo ?t)))')

    basica3 = mod_equipoA.BuildRule("basica3",
                                    '(declare (salience 1)) (tiempo ?t) (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y)) (dimension ?dim&:(< ?y (/ ?dim 2))) (not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ?y2 (+ ?y 1)))))',
                                    '(printout t "EQUIPO-A mueve a" ?n " hacia 3 en t " ?t crlf) (assert (mueve (num ?n) (mov 3) (tiempo ?t)))')

    basica4 = mod_equipoA.BuildRule("basica4",
                                    '(declare (salience 1)) (tiempo ?t) (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y)) (dimension ?dim&:(> ?y (/ ?dim 2))) (not (ficha (equipo "A") (pos-x ?x) (pos-y ?y2&:(= ?y2 (- ?y 1)))))',
                                    '(printout t "EQUIPO-A mueve a" ?n " hacia 4 en t " ?t crlf) (assert (mueve (num ?n) (mov 4) (tiempo ?t)))')

    termina = mod_equipoA.BuildRule("termina",
                                    '(declare (salience 100)) (tiempo ?t) (dimension ?dim) (mueve (num ?n) (mov ?m) (tiempo ?t)) (ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y)) (test (mov-valido ?dim ?m ?x ?y)) (not (ficha (equipo "A")  (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))))',
                                    "(pop-focus)")
