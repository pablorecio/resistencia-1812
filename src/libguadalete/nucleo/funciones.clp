;
; Fichero funciones.clp
;
; Contiene las definiciones de funciones que pueden hacer falta para
; desarrollar las distintas estrategias de ataque o de defensa
;
; Manuel Palomo Duarte, 2007
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Funciones generales
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(deffunction MAIN::a-fichero-tiempo (?t)
  (printout fich "tiempo" crlf ?t crlf))

(deffunction MAIN::a-fichero-jugador (?e ?n ?p ?x ?y ?d)
;  (open "temporal.txt" fich "a")
  (printout fich " e:" ?e)
  (printout fich " n:" ?n)
  (printout fich " p:" ?p)
  (printout fich " x:" ?x)
  (printout fich " y:" ?y)
  (printout fich " d:" ?d)
  (printout fich crlf)
;  (close fich)
)

(deffunction MAIN::por-pantalla-jugador (?e ?n ?p ?x ?y ?d)
  (printout t "e:" ?e " n:" ?n " x:")
  (if (< ?x 1000) then
    (printout t "0"))
  (if (< ?x 100) then
    (printout t "0"))
  (if (< ?x 10) then
    (printout t "0"))
  (printout t ?x)
  (printout t " y:")
  (if (< ?y 1000) then
    (printout t "0"))
  (if (< ?y 100) then
    (printout t "0"))
  (if (< ?y 10) then
    (printout t "0"))
  (printout t ?y crlf))

;
; Funcion distancia : mide la distancia de un punto a otro
;

(deffunction MAIN::distancia (?x ?y ?x2 ?y2)
  (sqrt (+ (* (- ?x ?x2) (- ?x ?x2)) (* (- ?y ?y2) (- ?y ?y2)))))

;
; Funcion dentro: comprueba si el punto (dx,dy) esta dentro del
; recta'ngulo que forman los puntos (x1,y1) y (x2,y2) sin contar
; los bordes
;

(deffunction MAIN::dentro (?x1 ?y1 ?x2 ?y2 ?x ?y)
  (and (or (<= ?x1 ?x ?x2) (>= ?x1 ?x ?x2))
       (or (<= ?y1 ?y ?y2) (>= ?y1 ?y ?y2))))

;
; Funcion minimo: devuelve el menor de dos numeros
;

(deffunction MAIN::minimo (?n1 ?n2)
  (if (< ?n1 ?n2) then
    ?n1
    else
    ?n2))

;
; Funcion mov-x: dado un movimiento dice si la x crece, decrece o no cambia
;

(deffunction MAIN::mov-x (?m)
  (switch ?m
	  (case 1 then 1)
	  (case 2 then -1)
	  (default 0)))

;
; Funcion mov-y: dado un movimiento dice si la y crece, decrece o no cambia
;

(deffunction MAIN::mov-y (?m)
  (switch ?m
	  (case 3 then 1)
	  (case 4 then -1)
	  (default 0)))

;
; Funcion movimiento-val: dado un movimiento y unas coordenadas dice si el
;movimiento es valido
;

(deffunction MAIN::mov-valido (?dim ?m ?x ?y)
  (and (> (+ ?x (mov-x ?m)) 0) (<= (+ ?x (mov-x ?m)) ?dim)
       (> (+ ?y (mov-y ?m)) 0) (<= (+ ?y (mov-y ?m)) ?dim)))

;
; Funcion valor pone un ? si la ficha no esta descubierta y un espacio si sí
;

(deffunction MAIN::valor (?descubierto)
  (if (= 0 ?descubierto) then
    "?"
    else
    " "))


;
; Funcion sim: dado un movimiento da su simétrico
;

(deffunction MAIN::simetrico (?m)
  (switch ?m
	  (case 1 then 2)
	  (case 2 then 1)
	  (case 3 then 4)
	  (case 4 then 3) 
	  (default 0)))

;
; Funcion sim: dado una posición da su simétrica
;

(deffunction MAIN::sim (?p)
  (- 9 ?p))


; Funcion para saber a que equipo corresponde el turno actual

(deffunction MAIN::turno (?ti ?ta)
  (if (= (mod (- ?ti ?ta) 2) 1) then
      "A"
      else 
      "B"
  )
)
