;
; f1.clp
;
; Fichero principal
;
; Manuel Palomo Duarte, 2007
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;

;
; Cambiamos la estrategia de resolucion de conflictos por la
; aleatoria, para hacer el sistema independiente del o'rden de
; escritura de las reglas 
;

;(set-strategy random)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Definicion de plantillas
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Definimos la plantilla de ficha-r que es la ficha real que usa el sistema
;

(deftemplate ficha-r
  (slot equipo)
  (slot num)
  (slot puntos)
  (slot pos-x)
  (slot pos-y)
  (slot descubierta))


;
; Definimos la plantilla de ficha, que la usan los módulos de cálculo
;

(deftemplate ficha
  (slot equipo)
  (slot num)
  (slot puntos)
  (slot pos-x)
  (slot pos-y)
  (slot descubierta))



; Plantilla de movimiento que se desea realizar
; Los movimientos son 1 avanza x, 2 retrocede x, 3 avanza y, 4 retrocede y

(deftemplate mueve
  (slot num)
  (slot mov)
  (slot tiempo))

;
; Definimos los movimientos maximos que va tener la partida (sumando los dos bandos),
;  la dimensi'on del tablero y la secuencia de control de módulos
;

; turno sirve para decidir el ganador si la partida termina por tiempo o reyes muertos

(deffacts opciones-juego
  (tiempo-inicial 200)
  (dimension 8)
  (turno "A")
  (base "A" 1)
  (base "B" 8)
  (modulos INFORMAR TRADUCIRF EQUIPO-A MOVER INFORMAR TRADUCIRF EQUIPO-B TRADUCIRM MOVER))

;
; M'odulo MAIN (se redefine el del sistema)
; 
; Se encarga de controlar el tiempo de juego y de llamar a los
;  m'odulos de INFORMAR ATAQUE y DEFENSA para realizar los movimientos
;

(defmodule MAIN
  (export deftemplate initial-fact ficha ficha-r dimension tiempo mueve turno tiempo-inicial)
  (export deffunction ?ALL))


(defrule MAIN::inicia-tiempo
   (declare (salience 99))
   (not (tiempo-iniciado))
   (tiempo-inicial ?ti)
   =>
   (assert (tiempo-iniciado))
   (assert (tiempo ?ti))
)

;
; Regla borra-fich: abre el fichero de salida para lectura y lo
;  cierra, por lo que sabemos que este estara vacio
;

(defrule MAIN::borra-fich
  (declare (salience 100))
  (not (fichero-abierto))
  =>
  (printout t crlf "BORRANDO FICHERO" crlf)
  (assert (fichero-abierto))
  (open "temporal.txt" fich "w")
  (close fich))


;
; Regla control-y-tiempo : avanza el tiempo del sistema y llama al
;  m'odulo INFORMAR para mostrar por fichero el estado actual del
;  sistema
;

(defrule MAIN::control-y-tiempo
  ?c <- (tiempo ?t&~0)
  ?orden <- (modulos INFORMAR $?r)
;  (ficha-r (equipo "A") (puntos 1))
;  (ficha-r (equipo "B") (puntos 1))
  =>
  (retract ?c)
  (assert (tiempo (- ?t 1)))
  (retract ?orden)
  (assert (modulos $?r INFORMAR))
  (printout t "Pasamos al modulo INFORMAR." crlf)
  (printout t "Tiempo " ?t crlf)
;  (readline)
  (focus INFORMAR))


;
; Regla control-sin-tiempo : se encarga de llamar a los m'odulos de
;  EQUIPO-A o EQUIPO-B para que vayan movi'endose los jugadores
;

(defrule MAIN::control-sin-tiempo
  ?c <- (tiempo ?t&~0)
  ?orden <- (modulos ?m&~INFORMAR $?r)
  (ficha-r (equipo "A") (puntos 1))
  (ficha-r (equipo "B") (puntos 1))
  =>
  (retract ?orden)
  (printout t " Modulo->" ?m " ")
  (assert (modulos $?r ?m))
  (focus ?m))
