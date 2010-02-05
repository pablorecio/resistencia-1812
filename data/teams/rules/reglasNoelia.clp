;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                 Reglas de Inteligencia Artificial                       ;
;                     básicas para el equipo A                            ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;                                                                         ;
; Copyright (C) 2009 Noelia Sales Montes                                  ;
;                                                                         ;
; This program is free software: you can redistribute it and/or modify    ;
; it under the terms of the GNU General Public License as published by    ;
; the Free Software Foundation, either version 3 of the License, or       ;
; (at your option) any later version.                                     ;
;                                                                         ;
; This program is distributed in the hope that it will be useful,         ;
; but WITHOUT ANY WARRANTY; without even the implied warranty of          ;
; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           ;
; GNU General Public License for more details.                            ;
;                                                                         ;
; You should have received a copy of the GNU General Public License       ;
; along with this program.  If not, see <http://www.gnu.org/licenses/>.   ;
;                                                                         ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;     Inicio de las reglas de comportamiento de la IA Seek & Destroy      ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Bandera de muerte:
; Se activa si han sido eliminados todos los combatientes básicos

(defrule EQUIPO-A::eliminados
(declare (salience 80))
  (not (ficha (equipo "A") (puntos 4) ))
  (not (ficha (equipo "A") (puntos 5) ))
  =>
  (assert(matar1))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Movimiento principal:
; Los 5 van por delante (son potentes, pero reservamos el 6 para lo mejor).

(defrule EQUIPO-A::movimientoPrincipal
(declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos 5)) 
  
  (test (< ?ya 6))
  =>
  (assert (mueve (num ?na) (mov 3) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Movimiento cobaya:
; Utilidad de los 4 = morir por la causa. Abrir terreno por ahí.

(defrule EQUIPO-A::movimientoCobaya
(declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos 4))

  (test  (< ?ya 6))
  =>
  (assert (mueve (num ?na) (mov 3) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Movimiento elemental:
; El resto de fichas se mueven si no hay nada más que hacer.
; Prioridad más baja.

(defrule EQUIPO-A::movimientoElemental
(declare (salience 10))
  (tiempo ?t)
  (matar-1-ya)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa)) 
  =>
  (assert (mueve (num ?na) (mov 3) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ataque en estrategia:
; Movimiento de ataque de cualquier ficha que no sea un 1 o un 6.

(defrule EQUIPO-A::ataqueBasico1
(declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))

  (test (= ?xb (- ?xa 1)))
  (test (= ?yb (+ ?ya 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::ataqueBasico2
(declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))

  (test (= ?xb (+ ?xa 1)))
  (test (= ?yb (+ ?ya 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 1) (tiempo ?t)))
)

(defrule EQUIPO-A::ataqueBasico3
(declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))
	
  (test (= ?xb (- ?xa 1)))
  (test (= ?yb (- ?ya 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::ataqueBasico4
(declare (salience 40))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))
  
  (test (= ?xb (+ ?xa 1)))
  (test (= ?yb (- ?ya 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 4) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ataque ZAS:
; De frente. Para qué dar más vueltas?

(defrule EQUIPO-A::zasEnTodaLaBoca
(declare (salience 44))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xa) (pos-y ?yb))

  (test (= ?ya (- ?yb 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 3) (tiempo ?t)))
)

; Ataque ZAS:
; Hacia la derecha.

(defrule EQUIPO-A::zasEnTodaLaDerecha
(declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?ya))

  (test (= ?xa (- ?xb 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 1) (tiempo ?t)))
)

; Ataque ZAS:
; Hacia la izquierda.

(defrule EQUIPO-A::zasEnTodaLaIzquierda
(declare (salience 42))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?ya))
	
  (test (= ?xa (+ ?xb 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Ataque tapadete:
; Por la derecha.

(defrule EQUIPO-A::ataqueTapadeteDcha
(declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?ya) )

  (test (> ?xb ?xa))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 1) (tiempo ?t)))
)

; Por la izquierda.

(defrule EQUIPO-A::ataqueTapadeteIzda
(declare (salience 30))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?ya) )

  (test (< ?xb ?xa))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Defensa a la burra:
; Descubierto enemigo hacia la derecha.

(defrule EQUIPO-A::defensaDescubiertoDcha
(declare (salience 45))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb) (puntos ?pb) (descubierta 1))

  (test (= ?xb (- ?xa 1)))
  (test (= ?yb (+ ?ya 1)))
  (test (> ?pb ?pa))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 1) (tiempo ?t)))
)

; Descubierto enemigo hacia la izquierda.

(defrule EQUIPO-A::defensaDescubiertoIzda
(declare (salience 45))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb) (puntos ?pb) (descubierta 1))
  
  (test (= ?xb (+ ?xa 1)))
  (test (= ?yb (+ ?ya 1)))
  (test (> ?pb ?pa))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Defensa "pa qué te acercas?":
; Demasiadas confianzas para acercarse tanto: arréale.
; De frente.

(defrule EQUIPO-A::paQueTeAcercasFrente
(declare (salience 45))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xa) (pos-y ?yb) (puntos ?pb) (descubierta 1))

  (test (= ?ya (- ?yb 1)))
  (test (> ?pb ?pa))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 4) (tiempo ?t)))
)

; Hacia la izquierda.

(defrule EQUIPO-A::paQueTeAcercasIzq
(declare (salience 45))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?ya) (puntos ?pb) (descubierta 1))

  (test (= ?xa (- ?xb 1)))
  (test (> ?pb ?pa))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 1) (tiempo ?t)))
)

; Hacia la derecha.

(defrule EQUIPO-A::paQueTeAcercasDcha
(declare (salience 45))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos ?pa))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?ya) (puntos ?pb) (descubierta 1))

  (test (> ?pb ?pa))
  (test (= ?xa (+ ?xb 1)))
  (test (or (<> ?pa 1) (<> ?pa 6)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

	 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Defensa "Al rey ni tocarlo":
; Si lo matan se acabó el juego.

(defrule EQUIPO-A::alReyNiTocarlo1
(declare (salience 78))
  (not (matar1))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos 6))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))
  (ficha (equipo "A") (num ?n3) (pos-x ?xb) (pos-y ?yc) (puntos 1))
  
  (test (= ?yc (- ?yb 2)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::alReyNiTocarlo2
(declare (salience 78))
  (not(matar1))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos 6))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))
  (ficha (equipo "A") (num ?n3) (pos-x ?xc) (pos-y ?yb) (puntos 1))

  (test (= ?xc (- ?xb 2)))
  =>
  (assert (mueve (num ?na) (mov 4) (tiempo ?t)))
)

(defrule EQUIPO-A::alReyNiTocarloIzda
(declare (salience 78))
  (not(matar1))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos 6))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))
  (ficha (equipo "A") (num ?n3) (pos-x ?xb) (pos-y ?yc) (puntos 1))

  (test (= ?yc (- ?yb 1)))
  =>
  (assert (mueve (num ?na) (mov 2) (tiempo ?t)))
)

(defrule EQUIPO-A::alReyNiTocarloAbajo
(declare (salience 78))
  (not(matar1))
  (tiempo ?t)
  (ficha (equipo "A") (num ?na) (pos-x ?xa) (pos-y ?ya) (puntos 6))
  (ficha (equipo "B") (num ?nb) (pos-x ?xb) (pos-y ?yb))
  (ficha (equipo "A") (num ?n3) (pos-x ?xc) (pos-y ?yb) (puntos 1))

  (test (= ?xc (- ?xb 1)))
  =>
  (assert (mueve (num ?na) (mov 4) (tiempo ?t)))
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Reglas nulas: "Quieto parao"
; Impedimos que se nos vaya de madre.
; El rey no puede irse por ahí aunque quiera.

(defrule EQUIPO-A::quietoParaoRey
(declare (salience 80))
  (ficha (equipo "A") (puntos 1))
  (tiempo ?t)
  =>
  (printout t "Quieto parao Rey!" crlf)
)

; El 6 es nuestra última defensa, y nuestro as en la manga. No podemos perderlo
; a la primera de cambio.

(defrule EQUIPO-A::quietoParaoPetoto
(declare (salience 77))
  (not (matar1))
  (ficha (equipo "A") (puntos 6))
  (tiempo ?t)
  =>
  (printout t "Quieto parao petoto!" crlf)
)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Regla de ataque principal:
; Petoto al poder.
; El 6 puede con todo.
; Prioridad alta: cuanto antes destruyamos sus fichas, menos peligro
; correrá nuestro rey.

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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

