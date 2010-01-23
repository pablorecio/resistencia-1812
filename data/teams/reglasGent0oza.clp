;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Reglas de Inteligencia Artificial                    ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Diego Barrios Romero, 2009
; Basado en los ejemplos incluidos en el código fuente
; de "La reconquista"
;
; Disponible bajo los términos de la GNU General Public 
; License (GPL) version 2 o superior
;

;;;;;;;;;;;;;;;;;;;;;;; EXTREMO ;;;;;;;;;;;;;;;;;;;;;;;;
; Cuando se llega al extremo el avance y retroceso 
; empiezan a ser aleatorios
(defrule EQUIPO-A::pululandoextremo-arriba
  (declare (salience 40))
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y 8))
  (test (or (= ?p 5) (= ?p 4)))
  (not(arriba))
  =>
  (assert (arriba)))

(defrule EQUIPO-A::6-extremo-izq
  (declare (salience 70))
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x 1) (pos-y 8))
  (not(6ext))
  =>
  (assert (6ext)))

(defrule EQUIPO-A::6-extremo-der
  (declare (salience 70))
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x 8) (pos-y 8))
  (not(6ext))
  =>
  (assert (6ext)))


;;;;;;;;;;;;;;;;;;;;;;;;; 6 ;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Avanzar hasta llegar al final
(defrule EQUIPO-A::basica60
  (declare (salience 60))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (< ?y 8))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

; Barrer si esta al final (derecha)
(defrule EQUIPO-A::barrer70
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (and (> ?y 7) (< ?x 8)))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

; Barrer si esta al final (izquierda)
(defrule EQUIPO-A::barrer71
  (declare (salience 71))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (and (> ?y 7) (> ?x 1)))
  (not (6ext))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::ir-ultima
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (and (= ?y 6) (> ?x 1)))
  (not (6ext))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::6retroc
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (6ext)
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::6izq
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 6) (pos-x ?x) (pos-y ?y))
  (6ext)
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))

;;;;;;;;;;;;;; ATAQUE AVENTURA ;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::6mata-arriba
   (declare (salience 75))
   (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 (- ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::6mata-abajo
   (declare (salience 75))
   (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 (+ ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::6mata-derecha
   (declare (salience 75))
   (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 ?y2) (= ?x1 (- ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::6mata-izquierda
   (declare (salience 75))
   (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 ?y2) (= ?x1 (+ ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


;;;;;;;;;;;;;;;;;;;;;;;;; ATACAR ;;;;;;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::ataque-arriba
   (declare (salience 80))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 (- ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::ataque-abajo
   (declare (salience 80))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 (+ ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::ataque-derecha
   (declare (salience 80))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 ?y2) (= ?x1 (- ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::ataque-izquierda
   (declare (salience 80))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (> ?p1 ?p2))
   (test (and(= ?y1 ?y2) (= ?x1 (+ ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

;;;;;;;;;;;;;; ATAQUE SUICIDA ;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::suicida-arriba
   (declare (salience 50))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (= ?p1 ?p2))
   (test (and(= ?y1 (- ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::suicida-abajo
   (declare (salience 50))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (= ?p1 ?p2))
   (test (and(= ?y1 (+ ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::suicida-derecha
   (declare (salience 50))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (= ?p1 ?p2))
   (test (and(= ?y1 ?y2) (= ?x1 (- ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::suicida-izquierda
   (declare (salience 50))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1) (puntos ?p1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2) (puntos ?p2) (descubierta 1))
   (test (= ?p1 ?p2))
   (test (and(= ?y1 ?y2) (= ?x1 (+ ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

;;;;;;;;;;;;;; ATAQUE AVENTURA ;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::aventura-arriba
   (declare (salience 45))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 (- ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::aventura-abajo
   (declare (salience 45))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 (+ ?y2 1)) (= ?x1 ?x2)))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::aventura-derecha
   (declare (salience 45))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 ?y2) (= ?x1 (- ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::aventura-izquierda
   (declare (salience 45))
   (ficha (equipo "A") (num ?n1) (pos-x ?x1) (pos-y ?y1))
   (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
   (test (and(= ?y1 ?y2) (= ?x1 (+ ?x2 1))))
   (tiempo ?t)
   =>
   (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;; Avanzar pululando 5 y 4
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::5y4pululando-av-arriba
  (declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 5) (= ?p 4)))
  (not (arriba))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::5y4pululando-av-abajo
  (declare (salience 38))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 5) (= ?p 4)))
  (not (arriba))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::5y4pululando-izquierda
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 5) (= ?p 4)))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::5y4pululando-derecha
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 5) (= ?p 4)))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;; ALEATORIO pululando 5 y 4
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::5y4pululando-ret-arriba
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 5) (= ?p 4)))
  (arriba)
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::5y4pululando-ret-abajo
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 5) (= ?p 4)))
  (arriba)
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))


;;;;;;;;;;;;;;;; Avanzar pululando 3 y 2 ;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::3y2pululando-arriba
  (declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 3) (= ?p 2)))
  (not (arriba))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::3y2pululando-abajo
  (declare (salience 28))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 3) (= ?p 2)))
  (not (arriba))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::3y2pululando-izquierda
  (declare (salience 29))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 3) (= ?p 2)))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::3y2pululando-derecha
  (declare (salience 29))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos ?p) (pos-x ?x) (pos-y ?y))
  (test (or (= ?p 3) (= ?p 2)))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))



;;;;;;;;;;;;;;;;;;;; REY PULULANDO ;;;;;;;;;;;;;;;;;;;;;;;;;
; El rey simplemente se queda pululando aleatoriamente por detras
(defrule EQUIPO-A::reypululando-arriba
  (declare (salience 9))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::reypululando-abajo
  (declare (salience 10))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::reypululando-izquierda
  (declare (salience 10))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::reypululando-derecha
  (declare (salience 10))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n) (puntos 1) (pos-x ?x) (pos-y ?y))
  =>
  (assert (mueve (num ?n) (mov 2) (tiempo ?t))))
