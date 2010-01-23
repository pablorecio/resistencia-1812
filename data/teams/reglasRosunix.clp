
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;	Rosunix v1.5 - Módulo de IA para el equipo Rosunix                        ;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;	Autor: Rosa María Durante Lerate.

;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Se ha cargado mis fichas (4-5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::sin4-5
(declare (salience 80))
	 (not (ficha (equipo "A") (num 031) ))
	 (not (ficha (equipo "A") (num 033) ))
	 (not (ficha (equipo "A") (num 037) ))
	 (not (ficha (equipo "A") (num 038) ))
=>
	(printout t "RUBIO QUE TAN MUERTOS" crlf)
	(assert(matar1))
)

;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Al ataque mis valientes (5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::avance-5
(declare (salience 30))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 5)) 
	 (tiempo ?t)
	 (test (< ?y1 6))
=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))
)


;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Al ataque mis valientes (4) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::avance-4
(declare (salience 30))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 4)) 
	 (tiempo ?t)
	 (test  (< ?y1 6))
=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))
)


;;; ;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Al ataque mis valientes ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::avance
(declare (salience 15))
	 (matar-1-ya)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p)) 
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))
)

;;; ;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Ataque en diagonal (2-5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::ataque-diag1
(declare (salience 41))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (test (= ?x2 (- ?x1 1)))
	 (test (= ?y2 (+ ?y1 1)))
	 (tiempo ?t)
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque-diag2
(declare (salience 41))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (test (= ?x2 (+ ?x1 1)))
	 (test (= ?y2 (+ ?y1 1)))
	 (tiempo ?t)
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque-diag3
(declare (salience 41))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (test (= ?x2 (- ?x1 1)))
	 (test (= ?y2 (- ?y1 1)))
	 (tiempo ?t)
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque-diag4
(declare (salience 41))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (test (= ?x2 (+ ?x1 1)))
	 (test (= ?y2 (- ?y1 1)))
	 (tiempo ?t)
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t)))
)

;;; ;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Ataque adyacente (2-5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::ataque-frente
(declare (salience 43))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y2))
	 (tiempo ?t)
	 (test (= ?y1 (- ?y2 1)))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque-drch
(declare (salience 42))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1))
	 (tiempo ?t)
	 (test (= ?x1 (- ?x2 1)))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque-izqu
(declare (salience 42))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1))
	 (tiempo ?t)
	 (test (= ?x1 (+ ?x2 1)))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

;;; ;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Ataque no adyacente (2-5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::ataque-lejos-drch
(declare (salience 30))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1) )
	 (tiempo ?t)
	 (test (> ?x2 ?x1))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque-lejos-izqu
(declare (salience 30))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1) )
	 (tiempo ?t)
	 (test (< ?x2 ?x1))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

;;; ;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Defensa diagonal (2-5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::defensa-diag1
(declare (salience 45))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	 (test (= ?x2 (- ?x1 1)))
	 (test (= ?y2 (+ ?y1 1)))
	 (test (> ?p2 ?p1))
	 (tiempo ?t)
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::defensa-diag2
(declare (salience 45))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	 (test (= ?x2 (+ ?x1 1)))
	 (test (= ?y2 (+ ?y1 1)))
	 (test (> ?p2 ?p1))
	 (tiempo ?t)
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

;;; ;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Defensa adyacente (2-5) ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::defensa-frente
(declare (salience 45))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y2) (puntos ?p2) (descubierta 1))
	 (tiempo ?t)
	 (test (= ?y1 (- ?y2 1)))
	 (test (> ?p2 ?p1))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::defensa-izq
(declare (salience 45))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1) (puntos ?p2) (descubierta 1))
	 (tiempo ?t)
	 (test (= ?x1 (- ?x2 1)))
	 (test (> ?p2 ?p1))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::defensa-drch
(declare (salience 45))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1) (puntos ?p2) (descubierta 1))
	 (tiempo ?t)
	 (test (> ?p2 ?p1))
	 (test (= ?x1 (+ ?x2 1)))
	 (test (or (<> ?p1 1) (<> ?p1 6)))
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

	 

;;; ;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Defendiendo al rey ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::rey-diag1
(declare (salience 78))
	 (not (matar1))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (ficha (equipo "A") (num ?n3) (pos-x ?x2) (pos-y ?y3) (puntos 1))
	 (test (= ?y3 (- ?y2 2)))
	 (tiempo ?t)
=>
	(printout t moviendo ficha ?n1 defendiendo diagonal 1 crlf)
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::rey-diag2
(declare (salience 78))
	 (not(matar1))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (ficha (equipo "A") (num ?n3) (pos-x ?x3) (pos-y ?y2) (puntos 1))
	 (test (= ?x3 (- ?x2 2)))
	 (tiempo ?t)
=>
	(printout t moviendo ficha ?n1 defendiendo diagonal 2 crlf)
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::rey-ladoizq
(declare (salience 78))
	 (not(matar1))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (ficha (equipo "A") (num ?n3) (pos-x ?x2) (pos-y ?y3) (puntos 1))
	 (test (= ?y3 (- ?y2 1)))
	 (tiempo ?t)
=>
	(printout t moviendo ficha ?n1 defendiendo diagonal 1 crlf)
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::rey-abajo2
(declare (salience 78))
	 (not(matar1))
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
	 (ficha (equipo "A") (num ?n3) (pos-x ?x3) (pos-y ?y2) (puntos 1))
	 (test (= ?x3 (- ?x2 1)))
	 (tiempo ?t)
=>
	(printout t moviendo ficha ?n1 defendiendo diagonal 2 crlf)
	(assert (mueve (num ?n1) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::no-mover-1
(declare (salience 80))
	 (ficha (equipo "A") (puntos 1))
	 (tiempo ?t)
=>
	(printout t "la ficha no se mueve ni d coña XD" crlf)
)

(defrule EQUIPO-A::no-mover-6
(declare (salience 77))
	 (not (matar1))
	 (ficha (equipo "A") (puntos 6))
	 (tiempo ?t)
=>
	(printout t "La ficha no se mueve ni d coña XD" crlf)
)



;;; ;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; A por todas!!! ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; ;;;;;;;;;;;;;; ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::avanza6
(declare (salience 60))
	 (matar1)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (not (ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y2) (puntos 6) (descubierta 1)))
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::mover-6-izq-sin6contrario
(declare (salience 78))
	 (matar1)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1) (puntos ?p))
	 (test (<> ?p 6))
	 (test (< ?x2 ?x1))	 
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::mover-6-drch-sin6contrario
(declare (salience 79))
	 (matar1)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y1) (puntos ?p))
	 (test (<> ?p 6))
	 (test (> ?x2 ?x1))	 
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::mover-6-delante-sin6contrario
(declare (salience 79))
	 (matar1)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y2) (puntos ?p))
	 (test (<> ?p 6))
	 (test (= ?y2 (+ ?y1 1)))	 
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::mover-6-evitarIzq-sin6contrario
(declare (salience 78))
	 (matar1)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y2) (puntos ?p))
	 (test (= ?p 6))
	 (test (= ?y2 (+ ?y1 1)))	 
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::mover-6-evitarDrch-sin6contrario
(declare (salience 79))
	 (matar1)
	 (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos 6))
	 (ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y2) (puntos ?p))
	 (test (= ?p 6))
	 (test (= ?y2 (+ ?y1 1)))	 
	 (tiempo ?t)
=>
	(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))
)


