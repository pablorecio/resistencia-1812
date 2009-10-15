;Equipo A                                              ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defrule EQUIPO-A::basica
  (declare (salience 79) )
  (tiempo ?t)
  ( ficha (equipo "A") (num A182) (puntos 4) (pos-x ?x) (pos-y ?y))
  (test (<> ?y 4) )
  => 
  ( assert ( mueve (num A182) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::basica2
  (declare (salience 79) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  (test (<> ?y 3) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)



(defrule EQUIPO-A::kill61
   (declare (salience 50))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 6)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 5)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 3)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 2)))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::kill62
   (declare (salience 50))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 6)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 5)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 3)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 2)))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::kill63
   (declare (salience 50))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 6)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 5)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 3)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 2)))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::kill64
   (declare (salience 50))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 6)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 5)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 3)))
   (not(ficha (equipo "A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 2)))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada Seis
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::seis1
  (declare (salience 67) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::seis2
  (declare (salience 67) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::seis3
  (declare (salience 67) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::seis4
  (declare (salience 67) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada cinco21
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::cinco21
  (declare (salience 66) )
  (tiempo ?t)
  ( ficha (equipo "A") (num A132) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num A132) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cinco22
  (declare (salience 66) )
  (tiempo ?t)
  ( ficha (equipo "A") (num A132) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num A132) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cinco23
  (declare (salience 66) )
  (tiempo ?t)
  ( ficha (equipo "A") (num A132) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num A132) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cinco24
  (declare (salience 66) )
  (tiempo ?t)
  ( ficha (equipo "A") (num A132) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num A132) (mov 2) (tiempo ?t) ) )
)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada cinco1
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::cinco1
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cinco2
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num 182) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cinco3
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num 182) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cinco4
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num 182) (puntos 5) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada cuatro
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::cuatro1
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos 42) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cuatro2
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos 42) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cuatro3
  (declare (salience 65) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos 42) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::cuatro3
  (declare (salience 64) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos 42) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada tres
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::tres1
  (declare (salience 63) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::tres2
  (declare (salience 63) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::tres3
  (declare (salience 63) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::tres3
  (declare (salience 63) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada dos
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::dos1
  (declare (salience 62) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 2) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::dos2
  (declare (salience 62) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 2) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?y ?y2) (= ?x ?x2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::dos3
  (declare (salience 62) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 2) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (< ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::dos3
  (declare (salience 62) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 2) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (> ?x ?x2) (= ?y ?y2) ) )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Jugada uno
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::uno21
  (declare (salience 79) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (= ?y (+ ?y2 1)) (= ?x ?x2) )  )
  => 
  ( assert ( mueve (num ?n) (mov 3) (tiempo ?t) ) )
)

(defrule EQUIPO-A::uno22
  (declare (salience 79) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (= ?y (- ?y2 1)) (= ?x ?x2) )  )
  => 
  ( assert ( mueve (num ?n) (mov 4) (tiempo ?t) ) )
)

(defrule EQUIPO-A::uno23
  (declare (salience 79) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (= ?x (+ ?x2 1)) (= ?y ?y2) )  )
  => 
  ( assert ( mueve (num ?n) (mov 1) (tiempo ?t) ) )
)

(defrule EQUIPO-A::uno24
  (declare (salience 79) )
  (tiempo ?t)
  ( ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  ( ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2))
  (test (and (= ?x (- ?x2 1)) (= ?y ?y2) )  )
  => 
  ( assert ( mueve (num ?n) (mov 2) (tiempo ?t) ) )
)

