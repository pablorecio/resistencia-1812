;
; traducirM.clp
;
; Fichero de traducción de movimientos a movimientos reales
; esto quiere decir que para el equipo A se quedan igual pero
; para el B se hacen los simétricos
;
; Manuel Palomo Duarte, 2007
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;

;
; M'odulo TRADUCIRM
;
; Cada movimiento se sustituye por su simétricos
;

(defmodule TRADUCIRM
  (import MAIN deftemplate initial-fact ficha ficha-r dimension tiempo mueve tiempo-inicial)
  (import MAIN deffunction ?ALL))

;
;

(defrule TRADUCIRM::traducir
  (declare (salience 10))
  (tiempo ?t)
  ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t))
  (tiempo-inicial ?ti)
  (test (= 0 (str-compare (turno ?ti ?t) "B")))
  (ficha-r (equipo "B") (num ?n))
  (not (traducido ?n ?t))
  =>
  (retract ?h1)
  (printout t "Traducido mov ficha-r n" ?n "de  "?m" a " (simetrico ?m) crlf)
;  (printout t "turno de " ?ti " y " ?t " vale " (turno ?ti ?t) " y su str-compare con B da " (str-compare (turno ?ti ?t) "B"))
  (assert (traducido ?n ?t))
  (assert (mueve (num ?n) (mov (simetrico ?m)) (tiempo ?t))))



