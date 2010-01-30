;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     ;
;  básicas para el equipo A                            ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Alberto Bermúdez Puerta, 2009
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                 Ataques Directos
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defrule EQUIPO-A::ataqueAdelante
	(declare (salience 60))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos ?p1))
	(test (> ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataquePrimeroA
	(declare (salience 55))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x 1) (pos-y ?y) (puntos 5))
	(test (>= ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataquePrimeroB
	(declare (salience 50))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n)(pos-x ?x) (pos-y ?y) (puntos 5))
	(test (>= ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataqueSegundo
	(declare (salience 40))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 6))
	(test (>= ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataqueTercero
	(declare (salience 30))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 4))
	(test (>= ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataqueCuarto
	(declare (salience 20))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 3))
	(test (>= ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataqueQuinto
	(declare (salience 10))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 2))
	(test (>= ?y 2))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataqueSexto
	(declare (salience 5))
	(tiempo ?t)
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos ?p1))
	(test (>= ?y 1))
	=>
	(assert (mueve (num ?n) (mov 3) (tiempo ?t))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                   Limpieza
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(defrule EQUIPO-A::barridoA
	(declare(salience 75))
	(ficha (equipo "A")(num ?n)(pos-x ?x)(pos-y ?y) (puntos 6))
	(tiempo ?t)
	(test (= ?y 8))
	=>
	(assert (mueve (num ?n)(mov 2)(tiempo ?t))))


(defrule EQUIPO-A::barridoB
	(declare(salience 70))
	(ficha (equipo "A")(num ?n)(pos-x ?x)(pos-y ?y) )
	(tiempo ?t)
	(test (= ?y 8))
	=>
	(assert (mueve (num ?n)(mov 1)(tiempo ?t))))


(defrule EQUIPO-A::barridoC
	(declare(salience 70))
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 5))
	(tiempo ?t)
	(test(and(= ?y 7) (not(= ?x 1))))
	=>
	(assert (mueve (num ?n)(mov 1)(tiempo ?t))))


(defrule EQUIPO-A::barridoD
	(declare(salience 71))
	(ficha (equipo"A") (num ?n) (pos-x ?x) (pos-y ?y) (puntos 2))
	(tiempo ?t)
	(test(and(= ?y 8) (not(= ?x 8))))
	=>
	(assert (mueve (num ?n)(mov 2)(tiempo ?t))))





;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                   Huida del rey
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



(defrule EQUIPO-A::asegurarse11
(declare (salience 80))
(ficha (equipo "A") (num ?n1) (pos-x ?x) (pos-y ?y) (puntos 1))
(ficha (equipo "B") (num ?n2) (pos-x ?x) (pos-y ?y1) (puntos ?p))
(test (or(= ?y (- ?y1 1)) (= ?y (+ ?y1 1)) ))
=>
(assert (mueve (num ?n1) (mov 1) (tiempo ?t)))) 

(defrule EQUIPO-A::asegurarse12
(declare (salience 80))
(ficha (equipo "A") (num ?n1) (pos-x ?x) (pos-y ?y) (puntos 1))
(ficha (equipo "B") (num ?n2) (pos-x ?x) (pos-y ?y1) (puntos ?p))
(test (or(= ?y (- ?y1 1)) (= ?y (+ ?y1 1)) ))
=>
(assert (mueve (num ?n1) (mov 2) (tiempo ?t)))) 

(defrule EQUIPO-A::asegurarse13
(declare (salience 80))
(ficha (equipo "A") (num ?n1) (pos-x ?x) (pos-y ?y) (puntos 1))
(ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y) (puntos ?p))
(test (or(= ?x (- ?x1 1)) (= ?x (+ ?x1 1)) ))
=>
(assert (mueve (num ?n1) (mov 3) (tiempo ?t)))) 

(defrule EQUIPO-A::asegurarse14
(declare (salience 80))
(ficha (equipo "A") (num ?n1) (pos-x ?x) (pos-y ?y) (puntos 1))
(ficha (equipo "B") (num ?n2) (pos-x ?x1) (pos-y ?y1) (puntos ?p))
(test (or(= ?x (- ?x1 1)) (= ?x (+ ?x1 1)) ))
=>
(assert (mueve (num ?n1) (mov 4) (tiempo ?t)))) 

