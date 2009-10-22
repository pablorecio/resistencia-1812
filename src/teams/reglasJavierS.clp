;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     ;
;  básicas para el equipo A                            ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; Francisco Javier Santacruz López-Cepero

; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1. Huida de nuestro rey si está bajo amenaza. 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::huida_rey_der
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en el borde izquierdo ni el derecho.
   (test (<> ?xrey  1))
   (test (<> ?xrey  8))

   ;;; Detectamos un enemigo a la derecha del rey.
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?yrey)) 
                                 (pos-x ?xenemy&:(= ?xenemy (+ ?xrey  1)))
   )

   ;;; Si no está ocupada la casilla de la izquierda
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey)) 
                         (pos-x ?xblock&:(= ?xblock (- ?xrey  1))))
   )

   ;;; Mover izquierda.
   =>
   (printout t "enemigo a la derecha, huir izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_der2
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))
     
   ;; NO estamos en el borde derecho ni en la fila 8.
   (test (<> ?xrey  8))
   (test (<> ?yrey  8))

   ;;; Detectamos un enemigo a la derecha del rey.
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?yrey)) 
                                 (pos-x ?xenemy&:(= ?xenemy (+ ?xrey  1)))
   )

   ;;; Si la izquierda está ocupada pero la de delante no.
;   (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey)) 
;                         (pos-x ?xblock&:(= ?xblock (- ?xrey  1)))
;   )

   (not (ficha (num ?n4) (pos-y ?yblock2&:(= ?yblock2 (+ ?yrey  1))) 
                         (pos-x ?xblock2&:(= ?xblock2 ?xrey)))
   )

   ;;; Mover hacia delante.
   =>
   (printout t "enemigo a la derecha, huir delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_izq
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en el límite de la derecha ni en el borde izquierdo
   (test (<> ?xrey  8))
   (test (<> ?xrey  1))

   ;;; Detectamos un enemigo a la izquierda del rey.
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?yrey)) 
                                 (pos-x ?xenemy&:(= ?xenemy (- ?xrey  1)))
   )

   ;;; Si no está ocupada la casilla de la derecha
   ;(not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey)) 
   ;                      (pos-x ?xblock&:(= ?xblock (+ ?xrey  1))))
   ;)


   ;;; Mover derecha.
   =>
   (printout t "enemigo a la izquierda , huir derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_izq2
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;; Si no estamos en el borde izquierdo ni en la última fila
   (test (<> ?xrey  1))
   (test (<> ?yrey  8))

   ;;; Detectamos un enemigo a la izquierda del rey.
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?yrey)) 
                                 (pos-x ?xenemy&:(= ?xenemy (- ?xrey  1)))
   )

   ;;; Si la derecha está ocupada pero la de delante no.
;   (ficha (num ?n3)  (pos-y ?yblock&:(= ?yblock ?yrey)) 
;                     (pos-x ?xblock&:(= ?xblock (+ ?xrey  1)))
;   )

   (not (ficha (num ?n4) (pos-y ?yblock2&:(= ?yblock2 (+ ?yrey  1))) 
                         (pos-x ?xblock2&:(= ?xblock2 ?xrey)))
   )

   ;;; Mover hacia delante.
   =>
   (printout t "enemigo a la izquierda , huir delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_delante
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en el límite derecho ni en la última fila.
   (test (<> ?xrey  8))
   (test (<> ?yrey  8))

   ;;; Detectamos un enemigo delante del rey
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (+ 1 ?yrey))) 
                                 (pos-x ?xenemy&:(= ?xenemy ?xrey))
   )

   ;;; Si la derecha está libre. 
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey)) 
                         (pos-x ?xblock&:(= ?xblock (+ ?xrey  1)))
   ))

   ;;; Mover hacia der.
   =>
   (printout t "enemigo delante, huir derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_delante2
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en el límite izquierdo ni en la última fila.
   (test (<> ?xrey  1))
   (test (<> ?yrey  8))

   ;;; Detectamos un enemigo delante del rey
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (+ ?yrey  1))) 
                                 (pos-x ?xenemy&:(= ?xenemy ?xrey))
   )

   ;;; Si la izquierda está libre. 
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey)) 
                         (pos-x ?xblock&:(= ?xblock (- ?xrey  1)))
   ))


   ;;; Mover hacia izq.
   =>
   (printout t "enemigo delante, huir izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_delante3
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en la fila 1 ni en la última
   (test (<> ?yrey  1))
   (test (<> ?yrey  8))

   ;;; Detectamos un enemigo delante del rey
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (+ ?yrey  1))) 
                                 (pos-x ?xenemy&:(= ?xenemy ?xrey))
   )

   ;;; Si atrás está libre. 
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (- ?yrey  1))) 
                         (pos-x ?xblock&:(= ?xblock ?xrey ))
   ))

   ;;; Mover hacia atrás.
   =>
   (printout t "enemigo delante, huir atrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_detras
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en la fila 1 ni en la última fila
   (test (<> ?yrey  1))
   (test (<> ?yrey  8))

   ;;; Detectamos un enemigo detrás del rey
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (- ?yrey  1))) 
                                 (pos-x ?xenemy&:(= ?xenemy ?xrey))
   )

   ;;; Si delante está libre. 
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (+ ?yrey  1))) 
                         (pos-x ?xblock&:(= ?xblock ?xrey ))
   ))
   
   ;;; Mover hacia delante.
   =>
   (printout t "enemigo detras, huir delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_detras2
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en la fila 1
   (test (<> ?yrey  1))
   ;;; Ni estamos pegados a la izquierda.
   (test (<> ?xrey  1))

   ;;; Detectamos un enemigo detrás del rey
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (- ?yrey  1))) 
                                 (pos-x ?xenemy&:(= ?xenemy ?xrey))
   )

   ;;; Si izquierda está libre. 
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey )) 
                         (pos-x ?xblock&:(= ?xblock (- ?xrey  1)))
   ))
   
   ;;; Mover hacia izquierda.
   =>
   (printout t "enemigo detras, huir izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_rey_detras2
   (declare (salience 80))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;;; Si no estamos en la fila 1
   (test (<> ?yrey  1))
   ;;; Ni estamos pegados a la derecha.
   (test (<> ?xrey  8))

   ;;; Detectamos un enemigo detrás del rey
   (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (- ?yrey  1))) 
                                 (pos-x ?xenemy&:(= ?xenemy ?xrey))
   )

   ;;; Si la derecha está libre. 
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?yrey )) 
                         (pos-x ?xblock&:(= ?xblock (+ ?xrey  1)))
   ))
   
   ;;; Mover hacia izquierda.
   =>
   (printout t "enemigo detras, huir derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

;;;; Mantener el rey todo lo atrás posible.
(defrule EQUIPO-A::huida_rey_atras
   (declare (salience 78))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;; Si no está en la linea 1
   (test (<> ?yrey  1)) 

   ;;; Libre atrás
   (not (ficha (num ?n2)  (pos-y ?yenemy&:(= ?yenemy (- ?yrey  1)))
                          (pos-x ?xenemy&:(= ?xenemy ?xrey ))
   ))


   ;;; Libre a la izquierda atrás de enemigos
   (not (ficha (equipo "B") (num ?n3) 
                                 (pos-y ?yenemy1&:(= ?yenemy1 (- ?yrey  1)))
                                 (pos-x ?xenemy1&:(= ?xenemy1 (- ?xrey  1)))
   ))

   ;;; Libre a la derecha atrás de enemigos
   (not (ficha (equipo "B") (num ?n4) 
                                 (pos-y ?yenemy2&:(= ?yenemy2 (- ?yrey  1)))
                                 (pos-x ?xenemy2&:(= ?xenemy2 (+ ?xrey  1)))
   ))

  ;;; Libre atrás-atrás de enemigos.
   (not (ficha (equipo "B") (num ?n4) 
                                 (pos-y ?yenemy2&:(= ?yenemy2 (- ?yrey  2)))
                                 (pos-x ?xenemy2&:(= ?xenemy2 ?xrey))
   ))
   
   ;;; Mover hacia atrás.
   =>
   (printout t "mantener rey atrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2. Defender al Rey 
;;; (solo se activa cuando el rey no puede huir)
;; Tirarse a defender al rey.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::defender_rey_atras
   (declare (salience 75))
   (tiempo ?t) 
   ;; El rey
   (ficha (equipo "A") (num ?n2) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;; Lo defienden las piezas mayores de tres dos puntos que estén cerca.
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(> ?ppieza 2))
   )

   ;; Tenemos un enemigo cerca del rey y lo debemos neutralizar.
   ;; Y Lo tenemos atrás!.
   (ficha (equipo "B") (num ?n3)   (pos-y ?yenemy&:(and (or (or (= ?yenemy (+ ?yrey  2)) (= ?yenemy (- ?yrey  2))) 
                                                            (or (= ?yenemy (+ ?yrey  1)) (= ?yenemy (- ?yrey  1)))
							    (= ?yenemy ?yrey))
                                                        (= ?yenemy (- ?ypieza 1))))
                                   (pos-x ?xenemy&:(and (or (or (= ?xenemy (+ ?xrey  2)) (= ?xenemy (- ?xrey  2))) 
                                                                       (or (= ?xenemy (+ ?xrey  1)) (= ?xenemy (- ?xrey  1)))
								       (= ?xenemy ?xrey))
                                                        (= ?xenemy ?xpieza)))
                                (puntos ?penemy)
                                   (descubierta ?info)
   )

   ;; O el enemigo no está descubierto, o es menor que nosotros. 
   ;; Tampoco es plan de suicidarse
   (test (or (= ?info 0) (and (= ?info 1) (<= ?penemy ?ppieza))))

   ;;; Mover hacia atrás.
   =>
   (printout t "defender rey: cargando atrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::defender_rey_delante
   (declare (salience 75))
   (tiempo ?t) 
   ;; El rey
   (ficha (equipo "A") (num ?n2) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;; Lo defienden las piezas mayores de tres dos puntos que estén cerca.
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(> ?ppieza 2))
   )

   ;; Tenemos un enemigo cerca del rey al que podemos neutralizar.
   ;; Y Lo tenemos delante!.
   (ficha (equipo "B") (num ?n3)   (pos-y ?yenemy&:(and (or (or (= ?yenemy (+ ?yrey  2)) (= ?yenemy (- ?yrey  2))) 
                                                            (or (= ?yenemy (+ ?yrey  1)) (= ?yenemy (- ?yrey  1)))
							    (= ?yenemy ?yrey))
                                                        (= ?yenemy (+ ?ypieza 1))))
                                   (pos-x ?xenemy&:(and (or (or (= ?xenemy (+ ?xrey  2)) (= ?xenemy (- ?xrey  2))) 
							 (or (= ?xenemy (+ ?xrey  1)) (= ?xenemy (- ?xrey  1)))
							 (= ?xenemy ?xrey))
                                                        (= ?xenemy ?xpieza)))
                                   (puntos ?penemy)
                                   (descubierta ?info)
   )

   ;; O el enemigo no está descubierto, o es menor que nosotros. 
   ;; Tampoco es plan de suicidarse
   (test (or (= ?info 0) (and (= ?info 1) (<= ?penemy ?ppieza))))

   ;;; Mover hacia delante.
   =>
   (printout t "defender rey: cargando delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::defender_rey_izq
   (declare (salience 75))
   (tiempo ?t) 
   ;; El rey
   (ficha (equipo "A") (num ?n2) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;; Lo defienden las piezas mayores de tres dos puntos que estén cerca.
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(> ?ppieza 2))
   )

   ;; Tenemos un enemigo cerca del rey al que podemos neutralizar.
   ;; Y Lo tenemos a la izquierda!.
   (ficha (equipo "B") (num ?n3)   (pos-y ?yenemy&:(and (or (or (= ?yenemy (+ ?yrey  2)) (= ?yenemy (- ?yrey  2))) 
                                                            (or (= ?yenemy (+ ?yrey  1)) (= ?yenemy (- ?yrey  1)))
							    (= ?yenemy ?yrey))
                                                        (= ?yenemy ?ypieza )))
                                   (pos-x ?xenemy&:(and (or (or (= ?xenemy (+ ?xrey  2)) (= ?xenemy (- ?xrey  2))) 
							    (or (= ?xenemy (+ ?xrey  1)) (= ?xenemy (- ?xrey  1)))
                                                            (= ?xenemy ?xrey)) 
                                                        (= ?xenemy (- ?xpieza 1))))
                                   (puntos ?penemy)
                                   (descubierta ?info)
   )

   ;; O el enemigo no está descubierto, o es menor que nosotros. 
   ;; Tampoco es plan de suicidarse
   (test (or (= ?info 0) (and (= ?info 1) (<= ?penemy ?ppieza))))

   ;;; Mover hacia izquierda.
   =>
   (printout t "defender rey: cargando izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::defender_rey_der
   (declare (salience 75))
   (tiempo ?t) 
   ;; El rey
   (ficha (equipo "A") (num ?n2) (pos-y ?yrey) (pos-x ?xrey) (puntos 1))

   ;; Lo defienden las piezas mayores de tres dos puntos que estén cerca.
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(> ?ppieza 2))
   )

   ;; Tenemos un enemigo cerca del rey al que podemos neutralizar.
   ;; Y Lo tenemos a la derecha!.
   (ficha (equipo "B") (num ?n3)   (pos-y ?yenemy&:(and (or (or (= ?yenemy (+ ?yrey  2)) (= ?yenemy (- ?yrey  2))) 
                                                            (or (= ?yenemy (+ ?yrey  1)) (= ?yenemy (- ?yrey  1)))
							    (= ?yenemy ?yrey))
                                                        (= ?yenemy ?ypieza )))
                                   (pos-x ?xenemy&:(and (or (or (= ?xenemy (+ ?xrey  2)) (= ?xenemy (- ?xrey  2))) 
                                                            (or (= ?xenemy (+ ?xrey  1)) (= ?xenemy (- ?xrey  1)))
                                                            (= ?xenemy ?xrey)) 
                                                        (= ?xenemy (+ ?xpieza 1))))
                                   (puntos ?penemy)
                                   (descubierta ?info)
   )

   ;; O el enemigo no está descubierto, o es menor que nosotros. 
   ;; Tampoco es plan de suicidarse
   (test (or (= ?info 0) (and (= ?info 1) (<= ?penemy ?ppieza))))

   ;;; Mover hacia derecha.
   =>
   (printout t "defender rey: cargando derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 4. ATAQUERRRR
;;      (reglas generales de combate)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::ataque_obvio_delante
   (declare (salience 71))
   (tiempo ?t) 
   ;; Atacan todos menos el rey
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Que tienen un objetivo delante 
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (+ ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza))
                                  (puntos ?penemy&:(< ?penemy ?ppieza))
				  (descubierta 1))
   ;;; Mover hacia delante.
   =>
   (printout t "ataque obvio delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque_obvio_atras
   (declare (salience 71))
   (tiempo ?t) 
   ;; Atacan todos menos el rey
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Que tienen un objetivo delante 
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (- ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza))
                                  (puntos ?penemy&:(< ?penemy ?ppieza))
				  (descubierta 1))
   ;;; Mover hacia delante.
   =>
   (printout t "ataque obvio atras" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::ataque_obvio_izq
   (declare (salience 71))
   (tiempo ?t) 
   ;; Atacan todos menos el rey
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Que tienen un objetivo delante 
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (- ?xpieza 1)))
                                  (puntos ?penemy&:(< ?penemy ?ppieza))
				  (descubierta 1))
   ;;; Mover hacia delante.
   =>
   (printout t "ataque obvio izq" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)


(defrule EQUIPO-A::ataque_obvio_der
   (declare (salience 71))
   (tiempo ?t) 
   ;; Atacan todos menos el rey
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Que tienen un objetivo derecha
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (+ ?xpieza 1)))
                                  (puntos ?penemy&:(< ?penemy ?ppieza))
				  (descubierta 1))
   ;;; Mover hacia delante.
   =>
   (printout t "ataque obvio derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_delante
   (declare (salience 70))
   (tiempo ?t) 
 
   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en la fila 8 ni en la 1.
   (test (<> ?ypieza 8))
   (test (<> ?ypieza 1))

   ;; Tenemos enemigo delante descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (+ ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza ))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie detrás.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (- ?ypieza 1)))
                         (pos-x ?xblock&:(= ?xblock ?xpieza))))

   ;;; Mover hacia atrás.
   =>
   (printout t "huida obvia delante: mover hacia atrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_delante2
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde izquierdo ni en el final.
   (test (<> ?ypieza 8))
   (test (<> ?xpieza 1))

   ;; Tenemos enemigo delante descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (+ ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza ))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie izquierda.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?ypieza ))
                         (pos-x ?xblock&:(= ?xblock (- ?xpieza 1)))))


   ;;; Mover hacia izquierda.
   =>
   (printout t "huida obvia delante: mover hacia izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_delante3
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; No estamos en la fila 8 ni en el borde derecho
   (test (<> ?xpieza 8))
   (test (<> ?ypieza 8))

   ;; Tenemos enemigo delante descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (+ ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza ))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie a la derecha.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?ypieza ))
                         (pos-x ?xblock&:(= ?xblock (+ ?xpieza 1)))))


   ;;; Mover hacia derecha.
   =>
   (printout t "huida obvia delante: mover hacia derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_detras
   (declare (salience 70))
   (tiempo ?t) 
 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en la fila uno ni en la fila 8.
   (test (<> ?ypieza 1))
   (test (<> ?ypieza 8))

   ;; Tenemos enemigo delante descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (- ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza ))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie delante.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (+ ?ypieza 1)))
                         (pos-x ?xblock&:(= ?xblock ?xpieza))))

   ;;; Mover hacia delante.
   =>
   (printout t "huida obvia detras: mover hacia delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_detras2
   (declare (salience 70))
   (tiempo ?t) 
 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en la fila uno ni en borde derecho.
   (test (<> ?ypieza 1))
   (test (<> ?xpieza 8))

   ;; Tenemos enemigo delante descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (- ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza ))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie a la derecha.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?ypieza ))
                         (pos-x ?xblock&:(= ?xblock (+ ?xpieza 1)))))

   ;;; Mover hacia derecha.
   =>
   (printout t "huida obvia detras: mover hacia derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_detras3
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en la fila uno ni en borde izquierdo.
   (test (<> ?ypieza 1))
   (test (<> ?xpieza 1))

   ;; Tenemos enemigo delante descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy (- ?ypieza 1)))
                                  (pos-x ?xenemy&:(= ?xenemy ?xpieza ))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie a la izquierda.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?ypieza ))
                         (pos-x ?xblock&:(= ?xblock (- ?xpieza 1)))))

   ;;; Mover hacia izquierda.
   =>
   (printout t "huida obvia detras: mover hacia izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_derecha
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde derecho ni en la fila 1.
   (test (<> ?xpieza 8))
   (test (<> ?ypieza 1))

   ;; Tenemos enemigo a la derecha descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (+ ?xpieza 1)))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie detras.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (- ?ypieza 1)))
                         (pos-x ?xblock&:(= ?xblock  ?xpieza ))))


   ;;; Mover hacia atrás.
   =>
   (printout t "huida obvia derecha: mover hacia atrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_derecha2
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde derecho ni en el borde izquierdo
   (test (<> ?xpieza 8))
   (test (<> ?xpieza 1))

   ;; Tenemos enemigo a la derecha descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (+ ?xpieza 1)))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie a la izq.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock ?ypieza ))
                         (pos-x ?xblock&:(= ?xblock (- ?xpieza 1)))))


   ;;; Mover hacia izquierda.
   =>
   (printout t "huida obvia derecha: mover hacia izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_derecha3
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde derecho ni en la fila 8.
   (test (<> ?xpieza 8))
   (test (<> ?ypieza 8))

   ;; Tenemos enemigo a la derecha descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (+ ?xpieza 1)))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie delante.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (+ ?ypieza 1)))
                         (pos-x ?xblock&:(= ?xblock  ?xpieza ))))


   ;;; Mover hacia delante.
   =>
   (printout t "huida obvia derecha: mover hacia delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_izquierda
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde izquierdo ni en la fila 8
   (test (<> ?xpieza 1))
   (test (<> ?ypieza 8))

   ;; Tenemos enemigo a la izquierda descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (- ?xpieza 1)))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie delante.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (+ ?ypieza 1)))
                         (pos-x ?xblock&:(= ?xblock  ?xpieza ))))


   ;;; Mover hacia delante.
   =>
   (printout t "huida obvia izquierda: mover hacia delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_izquierda2
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde izquierdo ni en la primera fila
   (test (<> ?xpieza 1))
   (test (<> ?ypieza 1))

   ;; Tenemos enemigo a la izquierda descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (- ?xpieza 1)))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie detrás.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock (- ?ypieza 1)))
                         (pos-x ?xblock&:(= ?xblock  ?xpieza ))))


   ;;; Mover hacia atrás.
   =>
   (printout t "huida obvia izquierda: mover hacia atrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::huida_obvia_izquierda3
   (declare (salience 70))
   (tiempo ?t) 

   ;; Todos menos el rey que ya tiene las suyas
   (ficha (equipo "A") (num ?n)   (pos-y ?ypieza) 
                                  (pos-x ?xpieza)
                                  (puntos ?ppieza&:(or (= ?ppieza 2) (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6)))
   )

   ;; Si no estamos en el borde izquierdo ni en el derecho.
   (test (<> ?xpieza 1))
   (test (<> ?xpieza 8))

   ;; Tenemos enemigo a la izquierda descubierto y es mayor.
   (ficha (equipo "B") (num ?n2)  (pos-y ?yenemy&: (= ?yenemy ?ypieza ))
                                  (pos-x ?xenemy&:(= ?xenemy (- ?xpieza 1)))
                                  (puntos ?penemy&:(> ?penemy ?ppieza))
				  (descubierta 1))

   ;; No tenemos a nadie derecha.
   (not (ficha (num ?n3) (pos-y ?yblock&:(= ?yblock  ?ypieza ))
                         (pos-x ?xblock&:(= ?xblock  (+ ?xpieza 1)))))


   ;;; Mover hacia derecha.
   =>
   (printout t "huida obvia izquierda: mover hacia derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Larga distancia
(defrule EQUIPO-A::obvio_largo_delante
 (declare (salience 65))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo cerca. 
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; No si hay un amigo con más puntos cerca
  (not (ficha (equipo "A") (num ?n3) (pos-y ?yotro&:(= ?yotro ?ypieza))
                              (pos-x ?xotro&:(or (= ?xotro (+ ?xpieza 1)) (= ?xotro (- ?xpieza 1))))
                              (puntos ?potro&:(> ?potro ?ppieza))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(or (= ?yenemy (+ ?ypieza 1))(= ?yenemy (+ ?ypieza 2))(= ?yenemy (+ ?ypieza 3))))
                                (pos-x ?xenemy&:(or (= ?xenemy ?xpieza) (= ?xenemy (+ ?xpieza 1)) (= ?xenemy (- ?xpieza 1))))
                                (puntos ?penemy&:(<= ?penemy ?ppieza))
                                (descubierta 1))

    ;;; Mover hacia delante
   =>
   (printout t "caza obvia delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::obvio_largo_detras
 (declare (salience 65))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo cerca. 
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; No si hay un amigo con más puntos cerca
  (not (ficha (equipo "A") (num ?n3) (pos-y ?yotro&:(= ?yotro ?ypieza))
                              (pos-x ?xotro&:(or (= ?xotro (+ ?xpieza 1)) (= ?xotro (- ?xpieza 1))))
                              (puntos ?potro&:(> ?potro ?ppieza))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(or (= ?yenemy (- ?ypieza 1))(= ?yenemy (- ?ypieza 2))(= ?yenemy (- ?ypieza 3))))
                                (pos-x ?xenemy&:(or (= ?xenemy ?xpieza) (= ?xenemy (+ ?xpieza 1)) (= ?xenemy (- ?xpieza 1))))
                                (puntos ?penemy&:(<= ?penemy ?ppieza))
                                (descubierta 1))

    ;;; Mover hacia detrás
   =>
   (printout t "caza obvia detras" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::obvio_largo_derecha
 (declare (salience 65))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo cerca. 
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; No si hay un amigo con más puntos cerca
  (not (ficha (equipo "A") (num ?n3) (pos-x ?xotro&:(= ?xotro ?xpieza))
                              (pos-y ?yotro&:(or (= ?yotro (+ ?ypieza 1)) (= ?yotro (- ?ypieza 1))))
                              (puntos ?potro&:(> ?potro ?ppieza))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-x ?xenemy&:(or (= ?xenemy (+ ?xpieza 1))(= ?xenemy (+ ?xpieza 2))(= ?xenemy (+ ?xpieza 3))))
                                (pos-y ?yenemy&:(or (= ?yenemy ?ypieza) (= ?yenemy (+ ?ypieza 1)) (= ?yenemy (- ?ypieza 1))))
                                (puntos ?penemy&:(<= ?penemy ?ppieza))
                                (descubierta 1))

    ;;; Mover hacia der
   =>
   (printout t "caza obvia derecha" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)


(defrule EQUIPO-A::obvio_largo_izquierda
 (declare (salience 65))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo cerca. 
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  (not (ficha (equipo "A") (num ?n3) (pos-x ?xotro&:(= ?xotro ?xpieza))
                              (pos-y ?yotro&:(or (= ?yotro (+ ?ypieza 1)) (= ?yotro (- ?ypieza 1))))
                              (puntos ?potro&:(> ?potro ?ppieza))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-x ?xenemy&:(or (= ?xenemy (- ?xpieza 1))(= ?xenemy (- ?xpieza 2))(= ?xenemy (- ?xpieza 3))))
                                (pos-y ?yenemy&:(or (= ?yenemy ?ypieza) (= ?yenemy (+ ?ypieza 1)) (= ?yenemy (- ?ypieza 1))))
                                (puntos ?penemy&:(<= ?penemy ?ppieza))
                                (descubierta 1))

    ;;; Mover hacia izq
   =>
   (printout t "caza obvia izquierda" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Caza (4,5,6 esos fieras)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrule EQUIPO-A::caza_menor_delante6
 (declare (salience 60))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo delante.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos 6))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (+ ?ypieza 1)))
                                (pos-x ?xenemy&:(= ?xenemy ?xpieza)))

    ;;; Mover hacia delante
   =>
   (printout t "caza menor delante 6" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_menor_atras6
 (declare (salience 60))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo detrás.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos 6))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (- ?ypieza 1)))
                                (pos-x ?xenemy&:(= ?xenemy ?xpieza)))

    ;;; Mover hacia atrás 
   =>
   (printout t "caza menor atrás 6" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_menor_izq6
 (declare (salience 60))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo delante.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos 6))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?ypieza ))
                                (pos-x ?xenemy&:(= ?xenemy (- ?xpieza 1))))

    ;;; Mover hacia izq 
   =>
   (printout t "caza menor izq 6" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_menor_der6
 (declare (salience 60))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos 6))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?ypieza ))
                                (pos-x ?xenemy&:(= ?xenemy (+ ?xpieza 1))))

    ;;; Mover hacia der
   =>
   (printout t "caza menor der 6" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_menor_der
 (declare (salience 58))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?ypieza ))
                                (pos-x ?xenemy&:(= ?xenemy (+ ?xpieza 1))))

    ;;; Mover hacia der
   =>
   (printout t "caza menor der" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)


(defrule EQUIPO-A::caza_menor_izq
 (declare (salience 58))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy ?ypieza ))
                                (pos-x ?xenemy&:(= ?xenemy (- ?xpieza 1))))

    ;;; Mover hacia der
   =>
   (printout t "caza menor izq" crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_menor_delante
 (declare (salience 58))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (+ 1 ?ypieza )))
                                (pos-x ?xenemy&:(= ?xenemy ?xpieza)))

    ;;; Mover hacia der
   =>
   (printout t "caza menor delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_menor_atras
 (declare (salience 58))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 3) (= ?ppieza 4) (= ?ppieza 5))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(= ?yenemy (- ?ypieza 1)))
                                (pos-x ?xenemy&:(= ?xenemy ?xpieza)))

    ;;; Mover hacia der
   =>
   (printout t "caza menor detrás" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

;; Larga distancia
(defrule EQUIPO-A::caza_mayor_delante
 (declare (salience 50))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(or (= ?yenemy (+ ?ypieza 1))(= ?yenemy (+ ?ypieza 2))(= ?yenemy (+ ?ypieza 3))))
                                (pos-x ?xenemy&:(or (= ?xenemy ?xpieza) (= ?xenemy (+ ?xpieza 1)) (= ?xenemy (- ?xpieza 1)))))

    ;;; Mover hacia der
   =>
   (printout t "caza mayor delante" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_mayor_detras
 (declare (salience 50))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(or (= ?yenemy (- ?ypieza 1))(= ?yenemy (- ?ypieza 2))(= ?yenemy (- ?ypieza 3))))
                                (pos-x ?xenemy&:(or (= ?xenemy ?xpieza) (= ?xenemy (+ ?xpieza 1)) (= ?xenemy (- ?xpieza 1)))))

    ;;; Mover hacia der
   =>
   (printout t "caza mayor atras" crlf)
   (assert (mueve (num ?n) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_mayor_izq
 (declare (salience 50))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(or (= ?yenemy ?ypieza) (= ?yenemy (+ ?ypieza 1)) (= ?yenemy (- ?ypieza 1))))
                                (pos-x ?xenemx&: (or (= ?xenemx (- ?xpieza 1))(= ?xenemx (- ?xpieza 2))(= ?xenemx (- ?xpieza 3)))))

    ;;; Mover hacia der
   =>
   (printout t "caza mayor izq " crlf)
   (assert (mueve (num ?n) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::caza_mayor_der

 (declare (salience 50))
 (tiempo ?t)

  ;; Tomamos el mayor con un enemigo der.
  (ficha (equipo "A") (num ?n) (pos-y ?ypieza)
                               (pos-x ?xpieza)
                               (puntos ?ppieza&:(or (= ?ppieza 4) (= ?ppieza 5) (= ?ppieza 6))))

  ;; Enemigo
  (ficha (equipo "B") (num ?n2) (pos-y ?yenemy&:(or (= ?yenemy ?ypieza) (= ?yenemy (+ ?ypieza 1)) (= ?yenemy (- ?ypieza 1))))
                                (pos-x ?xenemx&: (or (= ?xenemx (+ ?xpieza 1))(= ?xenemx (+ ?xpieza 2))(= ?xenemx (+ ?xpieza 3)))))

    ;;; Mover hacia der
   =>
   (printout t "caza mayor der" crlf)
   (assert (mueve (num ?n) (mov 1) (tiempo ?t)))
)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 5. Avanzar 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrule EQUIPO-A::mayor_avance
   (declare (salience 21))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?ypieza) (pos-x ?xpieza) (puntos ?pp&:(or  (= ?pp 3) (= ?pp 4) (= ?pp 5) (= ?pp 6))))

   ;; No existe ficha mayor.
   (not 
    (ficha (equipo "A") (num ?n1) (pos-y ?ypieza1) (pos-x ?xpieza1) (puntos ?pp1&:(> ?pp1 ?pp))))

   ;;; Mover hacia delante
   =>
   (printout t "avanzar mayor ficha" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)


(defrule EQUIPO-A::peon_avance
   (declare (salience 20))
   (tiempo ?t) 
   (ficha (equipo "A") (num ?n) (pos-y ?ypeon) (pos-x ?xpeon) (puntos 2))

   ;; Nadie delante
   (not (ficha (num ?n2)  (pos-y ?yother&:(= ?yother (+ ?ypeon 1)))
                          (pos-x ?xother&:(= ?xother ?xpeon ))
   ))

   ;; Este peón es el que está más atrás posible y que puede avanzar.

      ;; Existe un peón más atrasado... 
      (ficha (num ?n3) (pos-y ?yopeon&:(<= ?yopeon ?ypeon)) 
                            (pos-x ?xopeon)
       )

      ;; Pero no puede mover porque tiene una ficha delante!
      (ficha (num ?n4) (pos-y ?yoother&:(= ?yoother (+ ?yopeon 1)))
                            (pos-x ?xoother&:(= ?xoother ?yopeon))
      )

   ;;; Mover hacia delante
   =>
   (printout t "avanzar peón" crlf)
   (assert (mueve (num ?n) (mov 3) (tiempo ?t)))
)

