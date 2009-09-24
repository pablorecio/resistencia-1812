
def LoadFunctions(clips):
    a_fichero_tiempo = clips.BuildFunction("a-fichero-tiempo",
                                           "?t", 
                                           '(printout fich "tiempo" crlf ?t crlf)')

    a_fichero_jugador = clips.BuildFunction("a-fichero-jugador",
                                            "?e ?n ?p ?x ?y ?d",
                                            '(printout fich " e:" ?e) (printout fich " n:" ?n) (printout fich " p:" ?p) (printout fich " x:" ?x) (printout fich " y:" ?y) (printout fich " d:" ?d) (printout fich crlf)')
    
    por_pantalla_jugador = clips.BuildFunction("por-pantalla-jugador",
                                               "?e ?n ?p ?x ?y ?d",
                                               '(if (< ?x 1000) then (printout t "0")) (if (< ?x 100) then (printout t "0")) (if (< ?x 10) then (printout t "0")) (printout t ?x) (printout t " y:") (if (< ?y 1000) then (printout t "0")) (if (< ?y 100) then (printout t "0")) (if (< ?y 10) then (printout t "0")) (printout t ?y crlf))')

    distancia = clips.BuildFunction("distancia", 
                                    "?x ?y ?x2 ?y2", 
                                    '(sqrt (+ (* (- ?x ?x2) (- ?x ?x2)) (* (- ?y ?y2) (- ?y ?y2))))')

    dentro = clips.BuildFunction("dentro", 
                                 "?x1 ?y1 ?x2 ?y2 ?x ?y",
                                 "(and (or (<= ?x1 ?x ?x2) (>= ?x1 ?x ?x2)) (or (<= ?y1 ?y ?y2) (>= ?y1 ?y ?y2)))")
    
    minimo = clips.BuildFunction("minimo", 
                                 "?n1 ?n2", 
                                 "(if (< ?n1 ?n2) then ?n1 else ?n2)")

    mov_x = clips.BuildFunction("mov-x", 
                                "?m", 
                                "(switch ?m (case 1 then 1) (case 2 then -1) (default 0))")

    mov_y = clips.BuildFunction("mov-y",
                                "?m",
                                "(switch ?m (case 3 then 1) (case 4 then -1) (default 0))")

    non_valido = clips.BuildFunction("mov-valido",
                                     "?dim ?m ?x ?y",
                                     "(and (> (+ ?x (mov-x ?m)) 0) (<= (+ ?x (mov-x ?m)) ?dim) (> (+ ?y (mov-y ?m)) 0) (<= (+ ?y (mov-y ?m)) ?dim))")

    valor = clips.BuildFunction("valor",
                                "?descubierto", 
                                '(if (= 0 ?descubierto) then "?" else " ")')
    
    simetrico = clips.BuildFunction("simetrico",
                                    "?m",
                                    "(switch ?m (case 1 then 2) (case 2 then 1) (case 3 then 4) (case 4 then 3)  (default 0))")
    
    sim = clips.BuildFunction("sim", 
                              "?p", 
                              "(- 9 ?p)")


