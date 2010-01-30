;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     ;
;  básicas para el equipo A                            ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Rafael Amigueti Camerino, 2009
;
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;

; Fichero para annadir reglas


; REGLAS INDIVIDUALES PARA LA FICHA 6:

(defrule EQUIPO-A::basica60
  (declare (salience 63))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (<> ?x 4))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::movderecha6
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (dimension ?dim&:(= ?y (- ?dim 1)))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::movizquierda6
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (dimension ?dim&:(= ?y ?dim))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataque63
  (declare (salience 80))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (dimension ?dim)
  (test(and (= ?y ?dim) (= ?x 1)))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::retroceso64
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (dimension ?dim)
  (test(and (< ?y ?dim) (> ?y 2)))
  (test(= ?x 4))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::atacando69
  (declare (salience 80))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (+ ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::atacando68
  (declare (salience 80))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (- ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::atacando67
  (declare (salience 80))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (+ ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::atacando66
  (declare (salience 80))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (- ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))


; REGLAS INDIVIDUALES PARA LA FICHA 5:


(defrule EQUIPO-A::basica50
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (test (<> ?x 6))
  (test (and <> ?x 7 <> ?y 4))
  (test (and <> ?x 8 <> ?y 4))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataque51
  (declare (salience 50))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (dimension ?dim&:(= ?y (- ?dim 1)))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::movderecha5
  (declare (salience 65))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (dimension ?dim&:(= ?y ?dim))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::movizquierda5
  (declare (salience 65))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (dimension ?dim)
  (test(and (= ?y ?dim) (= ?x ?dim)))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::retroceso54
  (declare (salience 51))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (dimension ?dim)
  (test(and (< ?y ?dim) (> ?y 1)))
  (test(= ?x 6))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::atacando59
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (+ ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::atacando58
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (- ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::atacando57
  (declare (salience 65))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (+ ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::atacando5
  (declare (salience 77))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (- ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::busqueda53
  (declare (salience 73))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (- ?y2 2)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::busqueda54
  (declare (salience 73))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (+ ?y2 2)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::busqueda51
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (- ?x2 2)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::busqueda59
  (declare (salience 73))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (+ ?x2 2)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))

;busquedas elaboradas

(defrule EQUIPO-A::busqueda532
  (declare (salience 72))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (- ?y2 2)))
  (test (= ?x (+ ?x2 1)))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::busqueda542
  (declare (salience 71))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (+ ?y2 2)))
  (test (= ?x (+ ?x2 1)))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::busqueda512
  (declare (salience 72))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (- ?x2 2)))
  (test (= ?y (+ ?y2 1)))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::busqueda592
  (declare (salience 72))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (+ ?x2 2)))
  (test (= ?y (+ ?y2 1)))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))

; REGLAS INDIVIDUALES PARA LA FICHA 4:


(defrule EQUIPO-A::basica40
  (declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (test (<> ?x 3))
  (test (and <> ?x 7 <> ?y 4))
  (test (and <> ?x 8 <> ?y 4))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::movderecha4
  (declare (salience 41))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (dimension ?dim&:(= ?y (- ?dim 1)))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::movizquierda4
  (declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (dimension ?dim&:(= ?y ?dim))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataque43
  (declare (salience 43))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (dimension ?dim)
  (test(and (= ?y ?dim) (= ?x ?dim)))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::retroceso44
  (declare (salience 44))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (dimension ?dim)
  (test(and (< ?y ?dim) (> ?y 1)))
  (test(= ?x 3))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::atacando49
  (declare (salience 49))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (+ ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::atacando48
  (declare (salience 48))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (- ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::atacando47
  (declare (salience 47))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (+ ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::atacando46
  (declare (salience 46))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (- ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))


; REGLAS INDIVIDUALES PARA LA FICHA 3:


(defrule EQUIPO-A::atacando39
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 3) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (+ ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::atacando38
  (declare (salience 38))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 3) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x (- ?x2 1)))
  (test (= ?y ?y2))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::atacando37
  (declare (salience 37))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 3) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (+ ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::atacando36
  (declare (salience 36))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 3) (pos-x ?x) (pos-y ?y))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y (- ?y2 1)))
  (test (= ?x ?x2))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                    ATAQUE GANADO                     ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::ataque-seguro-arriba
   (declare (salience 78))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 (- ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataque-seguro-abajo
   (declare (salience 78))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 (+ ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::ataque-seguro-derecha
   (declare (salience 78))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 ?y2) (= ?x1 (- ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::ataque-seguro-izquierda
   (declare (salience 78))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 ?y2) (= ?x1 (+ ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


; EN CASO QUE NO SE REALICEN NINGUNA DE LAS REGLAS ANTERIORES:



(defrule EQUIPO-A::basica6_1
  (declare (salience 9))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::basica6_2
  (declare (salience 9))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::basica5_1
  (declare (salience 8))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::basica5_2
  (declare (salience 8))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 5) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::basica4_1
  (declare (salience 7))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::basica4_2
  (declare (salience 7))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 4) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))
