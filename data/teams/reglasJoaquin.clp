;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     ;
;  básicas para el equipo A                            ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Joaquín Salcedo Marquez, 2009
;


;REYMUEVETE
(defrule EQUIPO-A::huyerey11
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::huyerey12
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::huyerey13
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::huyerey21
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?x1 ?x2) 1))
  (test (= ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::huyerey22
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?x1 ?x2) 1))
  (test (= ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))
(defrule EQUIPO-A::huyerey23
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?x1 ?x2) 1))
  (test (= ?y1 ?y2))
  
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::huyerey31
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::huyerey32
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::huyerey33
  (declare (salience 76))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::huyerey41
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::huyerey42
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))



(defrule EQUIPO-A::huyerey43
  (declare (salience 75))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))











;Matar Seguro


(defrule EQUIPO-A::matar1
  (declare (salience 71))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (puntos ?p2)(pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (< ?p2 ?p1))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::matar2
  (declare (salience 71))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (puntos ?p2)(pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (< ?p2 ?p1))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::matar3
  (declare (salience 71))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (< ?p2 ?p1))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::matar4
  (declare (salience 71))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2)(puntos ?p2) (pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (< ?p2 ?p1))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))



(defrule EQUIPO-A::suicida1
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (puntos ?p2)(pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (= ?p2 ?p1))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::suicida2
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (puntos ?p2)(pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (= ?p2 ?p1))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::suicida3
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (puntos ?p2) (pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (= ?p2 ?p1))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::suicida4
  (declare (salience 70))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos ?p1) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2)(puntos ?p2) (pos-x ?x2) (pos-y ?y2)(descubierta 1))
  (test (= ?p2 ?p1))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))














; REGLAS INDIVIDUALES PARA LA FICHA 6:



(defrule EQUIPO-A::matar61
  (declare (salience 69))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::matar62
  (declare (salience 69))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::matar63
  (declare (salience 69))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::matar64
  (declare (salience 69))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))



(defrule EQUIPO-A::ataquecerca61
  (declare (salience 67))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataquecerca62
  (declare (salience 67))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca63
  (declare (salience 67))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca64
  (declare (salience 67))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))





(defrule EQUIPO-A::ataque61
  (declare (salience 66))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 3))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataque62
  (declare (salience 66))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 3))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataque63
  (declare (salience 66))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 3))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataque64
  (declare (salience 66))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 3))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))





(defrule EQUIPO-A::notequedesay61
  (declare (salience 61))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::notequedesay62
  (declare (salience 61))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::notequedesay63
  (declare (salience 61))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 4))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::notequedesay64
  (declare (salience 61))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 4))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))





(defrule EQUIPO-A::simple61
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (< ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::simple62
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (> ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::simple63
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (< ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::simple64
  (declare (salience 62))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (> ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))







(defrule EQUIPO-A::basica6x1
  (declare (salience 60))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (< ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::basica6x2
  (declare (salience 60))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (> ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))
(defrule EQUIPO-A::basica6y1
  (declare (salience 60))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (< ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::basica6y2
  (declare (salience 60))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 6) (pos-x ?x) (pos-y ?y))
  (test (> ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))




; REGLAS INDIVIDUALES PARA LA FICHA 5:


(defrule EQUIPO-A::matar51
  (declare (salience 59))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))


(defrule EQUIPO-A::matar52
  (declare (salience 59))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::matar53
  (declare (salience 59))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::matar54
  (declare (salience 59))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))




(defrule EQUIPO-A::ataquecerca51
  (declare (salience 57))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataquecerca52
  (declare (salience 57))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca53
  (declare (salience 57))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca54
  (declare (salience 57))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))







(defrule EQUIPO-A::ataque51
  (declare (salience 56))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 3))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataque52
  (declare (salience 56))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 3))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataque53
  (declare (salience 56))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 3))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataque54
  (declare (salience 56))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 3))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::simple51
  (declare (salience 52))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (< ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::simple52
  (declare (salience 52))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (> ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::simple53
  (declare (salience 52))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (< ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::simple54
  (declare (salience 52))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (> ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::basica5x1
  (declare (salience 50))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x) (pos-y ?y))
  (test (< ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::basica5x2
  (declare (salience 50))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x) (pos-y ?y))
  (test (> ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))
(defrule EQUIPO-A::basica5y1
  (declare (salience 50))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x) (pos-y ?y))
  (test (< ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::basica5y2
  (declare (salience 50))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 5) (pos-x ?x) (pos-y ?y))
  (test (> ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))






; REGLAS INDIVIDUALES PARA LA FICHA 4:

;Matar

(defrule EQUIPO-A::matar41
  (declare (salience 49))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::matar42
  (declare (salience 49))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::matar43
  (declare (salience 49))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::matar44
  (declare (salience 49))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca41
  (declare (salience 47))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataquecerca42
  (declare (salience 47))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca43
  (declare (salience 47))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataquecerca44
  (declare (salience 47))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::ataque41
  (declare (salience 46))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 3))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataque42
  (declare (salience 46))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 3))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataque43
  (declare (salience 46))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 3))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataque44
  (declare (salience 46))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 3))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))





(defrule EQUIPO-A::acercamiento41
  (declare (salience 41))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::acercamiento42
  (declare (salience 41))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::acercamiento43
  (declare (salience 41))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 4))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::acercamiento44
  (declare (salience 47))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 4))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::simple41
  (declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (< ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::simple42
  (declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (> ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::simple43
  (declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (< ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::simple44
  (declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (> ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))


(defrule EQUIPO-A::basica4x1
  (declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x) (pos-y ?y))
  (test (< ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::basica4x2
  (declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x) (pos-y ?y))
  (test (> ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::basica4y1
  (declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x) (pos-y ?y))
  (test (< ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::basica4y2
  (declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 4) (pos-x ?x) (pos-y ?y))
  (test (> ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))







; REGLAS INDIVIDUALES PARA LA FICHA 3:


(defrule EQUIPO-A::matar31
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::matar32
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::matar33
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::matar34
  (declare (salience 39))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))



(defrule EQUIPO-A::ataque31
  (declare (salience 36))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::ataque32
  (declare (salience 36))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::ataque33
  (declare (salience 36))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::ataque34
  (declare (salience 36))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 2))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))



(defrule EQUIPO-A::simple31
  (declare (salience 32))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (< ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::simple32
  (declare (salience 32))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (> ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::simple33
  (declare (salience 32))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (< ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::simple34
  (declare (salience 32))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (> ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))




(defrule EQUIPO-A::basica3x1
  (declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x) (pos-y ?y))
  (test (< ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::basica3x2
  (declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x) (pos-y ?y))
  (test (> ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::basica3y1
  (declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x) (pos-y ?y))
  (test (< ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::basica3y2
  (declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 3) (pos-x ?x) (pos-y ?y))
  (test (> ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))






;Kamikazes con los 2:


(defrule EQUIPO-A::matar21
  (declare (salience 29))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x2 ?x1) 1))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::matar22
  (declare (salience 29))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (= (- ?x1 ?x2) 1))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))


(defrule EQUIPO-A::matar23
  (declare (salience 29))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y2 ?y1) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))


(defrule EQUIPO-A::matar24
  (declare (salience 29))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= (- ?y1 ?y2) 1))
  (test (= ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))

(defrule EQUIPO-A::simple21
  (declare (salience 22))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (< ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::simple22
  (declare (salience 22))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?y1 ?y2))
  (test (> ?x1 ?x2))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::simple23
  (declare (salience 22))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (< ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::simple24
  (declare (salience 22))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x1) (pos-y ?y1))
  (ficha (equipo "B") (num ?n2) (pos-x ?x2) (pos-y ?y2))
  (test (= ?x1 ?x2))
  (test (> ?y1 ?y2))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))



(defrule EQUIPO-A::basica2x1
  (declare (salience 20))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x) (pos-y ?y))
  (test (< ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 1) (tiempo ?t))))

(defrule EQUIPO-A::basica2x2
  (declare (salience 20))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x) (pos-y ?y))
  (test (> ?x 4))
  =>
  (assert (mueve (num ?n1) (mov 2) (tiempo ?t))))

(defrule EQUIPO-A::basica2y1
  (declare (salience 20))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x) (pos-y ?y))
  (test (< ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 3) (tiempo ?t))))

(defrule EQUIPO-A::basica2y2
  (declare (salience 20))
  (tiempo ?t)
  (ficha (equipo "A") (num ?n1) (puntos 2) (pos-x ?x) (pos-y ?y))
  (test (> ?y 4))
  =>
  (assert (mueve (num ?n1) (mov 4) (tiempo ?t))))



