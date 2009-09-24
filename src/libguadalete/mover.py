def LoadFunctions(clips):
    mod_mover = clips.BuildModule("MOVER",
                                  "(import MAIN deftemplate initial-fact ficha-r dimension tiempo mueve) (import MAIN deffunction ?ALL)")

    movimiento = mod_mover.BuildRule("movimiento", "(declare (salience 90)) (tiempo ?t) ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t)) ?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y) (descubierta ?d)) (dimension ?dim) (test (mov-valido ?dim ?m ?x ?y)) (not (ficha-r (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2)))) (not (movido ?e ?t))",
                                         '(retract ?h1 ?h2) (printout t "Movimiento de "?n"(puntos "?p") :mov "?m crlf) (assert (movido ?e ?t)) (assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m))) (descubierta ?d)))')

    ataque_1 = mod_mover.BuildRule("ataque-1",
                                   "(declare (salience 90)) (tiempo ?t) ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t)) ?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y)) (dimension ?dim) (test (mov-valido ?dim ?m ?x ?y)) ?h3 <- (ficha-r (equipo ?e2&~?e) (puntos ?p2&:(> ?p ?p2)) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))) (not (movido ?e ?t))",
                                   '(retract ?h1 ?h2 ?h3) (printout t "Ataque con victoria de "?n"(puntos "?p") : mov "?m crlf) (assert (movido ?e ?t)) (assert (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x (+ ?x (mov-x ?m))) (pos-y (+ ?y (mov-y ?m))) (descubierta 1)))')

    ataque_2 = mod_mover.BuildRule("ataque-2",
                                   "(declare (salience 90)) (tiempo ?t) ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t)) ?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y)) (dimension ?dim) (test (mov-valido ?dim ?m ?x ?y)) ?h3 <- (ficha-r (equipo ?e2&~?e) (puntos ?p) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))) (not (movido ?e ?t))",
                                   '(retract ?h1 ?h2 ?h3) (printout t "Ataque con empate de "?n"(puntos "?p") : mov "?m crlf) (assert (movido ?e ?t))')

    ataque_3 = mod_mover.BuildRule("ataque-3",
                                   "(declare (salience 90)) (tiempo ?t) ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t)) ?h2 <- (ficha-r (equipo ?e) (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y)) (dimension ?dim) (test (mov-valido ?dim ?m ?x ?y)) ?h3 <- (ficha-r (equipo ?e2&~?e) (num ?n2) (puntos ?p2&:(< ?p ?p2)) (pos-x ?x2&:(= (+ ?x (mov-x ?m)) ?x2)) (pos-y ?y2&:(= (+ ?y (mov-y ?m)) ?y2))) (not (movido ?e ?t))",
                                   '(retract ?h1 ?h2 ?h3) (printout t "Ataque con derrota de "?n"(puntos "?p") : mov "?m crlf) (assert (movido ?e ?t)) (assert (ficha-r (equipo ?e2) (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2) (descubierta 1)))')

    limpia = mod_mover.BuildRule("limpia",
                                 "(declare (salience 0)) ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))",
                                 "(retract ?h1)")
                                   
