;
; traducirF.clp
;
; Fichero de traducción de fichas reales a fichas
;
; Manuel Palomo Duarte, 2007
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;

;
; M'odulo traducirF
;
; Pasa de ficha-r a ficha según de quien sea el turno
;

(defmodule TRADUCIRF
  (import MAIN deftemplate initial-fact ficha ficha-r dimension tiempo)
  (import MAIN deffunction ?ALL))


(defrule TRADUCIRF::inicial1
  (declare (salience 100))
  (tiempo ?t)
  =>
  (printout t "**********************************" crlf ))

;
; Regla inicial: mira quien ha sido el A en el último turno
;

(defrule TRADUCIRF::inicial1
  (declare (salience 100))
  (tiempo ?t)
  (test (= 0 (mod ?t 2)))
  =>
  (assert (equipoA ?t "B")))

(defrule TRADUCIRF::inicial2
  (declare (salience 100))
  (tiempo ?t)
  (test (<> 0 (mod ?t 2)))
  =>
  (assert (equipoA ?t "A")))

;
; Elimina las ficha que existen
;

(defrule TRADUCIRF::elimina1
  (declare (salience 20))
  (tiempo ?t)
  ?h <- (ficha (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta ?d))
  (not (limpia ?t))
  =>
;  (printout t "Limpiando ..." ?n crlf)
  (retract ?h))

;
; Hace que no se eliminen las fichas que se creen
;

(defrule TRADUCIRF::elimina2
  (declare (salience 19))
  (tiempo ?t)
  =>
  (printout t "*Limpiado" ?t  crlf)
;  (facts)
  (assert (limpia ?t)))

;
; Traduce de ficha a ficha-r manteniendo A como A para fichas no descubiertas
;
; El equipo A (que es el que mueve) ve los puntos de todas sus fichas

(defrule TRADUCIRF::directo-0A
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "A")
  (ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))
  =>
;  (printout t "Traduzco1 de ficha-r a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))))

;
; Traduce de ficha a ficha-r manteniendo B como B para fichas no descubiertas
;
; El equipo A (que es el que mueve) no ve los puntos de las fichas no descubiertas
; del enemigo

(defrule TRADUCIRF::directo-0B
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "A")
  (ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))
  =>
;  (printout t "Traduzco1 de ficha-r a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos 0) (descubierta 0))))

;
; Traduce de ficha a ficha-r manteniendo A como A para fichas descubiertas
;

(defrule TRADUCIRF::directo-1
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "A")
  (ficha-r (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))
  =>
;  (printout t "Traduzco2 de ficha-r a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo ?e) (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))))

;
; Traduce de ficha a ficha-r pasando A como B para fichas no descubiertas
;

(defrule TRADUCIRF::indirecto-0A
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "B")
  (ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))
  =>
;  (printout t "Traduzco3 de ficha-r a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos 0) (descubierta 0))))


;
; Traduce de ficha a ficha-r pasando A como B para fichas no descubiertas
;

(defrule TRADUCIRF::indirecto-0B
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "B")
  (ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 0))
  =>
;  (printout t "Traduzco3 de ficha-r a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 0))))


;
; Traduce de ficha a ficha-r pasando A como B para fichas descubiertas
;

(defrule TRADUCIRF::indirecto-1A
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "B")
  (ficha-r (num ?n) (equipo "A") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))
  =>
;  (printout t "Traduzco4 de ficha-r, "?n"  a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo "B") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 1))))

;
; Traduce de ficha a ficha-r pasando B como A para fichas descubiertas
;

(defrule TRADUCIRF::indirecto-1A
  (declare (salience 10))
  (tiempo ?t)
  (equipoA ?t "B")
  (ficha-r (num ?n) (equipo "B") (pos-x ?x) (pos-y ?y) (puntos ?v) (descubierta 1))
  =>
;  (printout t "Traduzco4 de ficha-r, "?n"  a ficha " ?n crlf)
  (assert (ficha (num ?n) (equipo "A") (pos-x (sim ?x)) (pos-y (sim ?y)) (puntos ?v) (descubierta 1))))

