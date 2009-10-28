def LoadFunctions(clips):
    mod_informar = clips.BuildModule("INFORMAR",
                                     "(import MAIN deftemplate initial-fact ficha-r dimension tiempo) (import MAIN deffunction ?ALL)")

    informacion = mod_informar.BuildRule("informacion",
                                         "(ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y) (descubierta ?d)) (tiempo ?t) (not (impresa ?e ?n ?t))",
                                         '(assert (impresa ?e ?n ?t)) (open "temporal.txt" fich "a") (a-fichero-jugador ?e ?n ?p ?x ?y ?d) (close fich)')

    inicial = mod_informar.BuildRule("inicial",
                                     "(declare (salience 100)) (tiempo ?t) (not (iniciado ?t)) (dimension ?dim)",
                                     '(open "temporal.txt" fich "a") (a-fichero-tiempo ?t) (close fich) (assert (iniciado ?t)) (assert (fila (+ 1 ?dim))) (assert (columna (+ 1 ?dim)))')

    vacia = mod_informar.BuildRule("vacia",
                                   "(declare (salience 10)) ?c <- (columna ?x) (fila ?y) (dimension ?dim) (test (not (> ?x ?dim))) (not (ficha-r (pos-x ?x) (pos-y ?y)))",
                                   '(retract ?c) (assert (columna (+ ?x 1))) (printout t "    ")')

    noVacia = mod_informar.BuildRule("noVacia",
                                     "(declare (salience 10)) ?c <- (columna ?x) (fila ?y) (dimension ?dim) (test (not (> ?x ?dim))) (ficha-r (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta ?d))",
                                     '(retract ?c) (assert (columna (+ ?x 1))) (printout t " " ?e ?v (valor ?d))')

    siguienteFila = mod_informar.BuildRule("siguienteFila",
                                           "(declare (salience 20)) (dimension ?dim) ?c <- (columna ?x) (test (> ?x ?dim)) ?f <- (fila ?y) (test (not (<= ?y 1)))",
                                           '(retract ?c ?f) (assert (fila (- ?y 1))) (assert (columna 1)) (printout t crlf (- ?y 1) "|"))')

    filaFinal = mod_informar.BuildRule("filaFinal",
                                       "(declare (salience 20)) (dimension ?dim) ?c <- (columna ?x) (test (> ?x ?dim)) ?f <- (fila ?y) (test (= 1 ?y))",
                                       '(retract ?c ?f) (printout t crlf "----------------------------------" crlf   "x:  1   2   3   4   5   6   7   8" crlf) (readline)')

    fin1 = mod_informar.BuildRule("fin1",
                                  "(declare (salience -100)) (tiempo ?t&0)",
                                  '(printout t "Fin del tiempo" crlf) (rename "temporal.txt" "resultado.txt")')

    fin_sin_rey1 = mod_informar.BuildRule("fin-sin-rey1",
                                          '(declare (salience -100)) ?c <- (tiempo ?t&~0) (not (ficha-r (equipo "A") (puntos 1)))',
                                          '(printout t "Rey del equipo A muerto" crlf) (rename "temporal.txt" "resultado.txt")')

    fin_sin_rey2 = mod_informar.BuildRule("fin-sin-rey2",
                                          '(declare (salience -100)) ?c <- (tiempo ?t&~0) (not (ficha-r (equipo "B") (puntos 1)))',
                                          '(printout t "Empate, fin del tiempo" crlf) (printout t "Rey del equipo B muerto" crlf) (rename "temporal.txt" "resultado.txt")')
