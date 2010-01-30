;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     
;  básicas para el equipo A                            
;
; Por Manuel Palomo Duarte
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Inicializamos las fichas
;
; Aqui se pueden cambiar los puntos de la ficha de cada
;  posicion al comenzar la partida
;
; Manuel Palomo Duarte, 2007
;

; Fichas del equipo A, sus num son 1XY
; Empiezan en las y 1 y 2

(deffacts fichas-A
  (ficha-r (equipo "A") (num 111) (puntos 1) (pos-x 1) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 112) (puntos 2) (pos-x 2) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 113) (puntos 2) (pos-x 3) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 114) (puntos 2) (pos-x 4) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 115) (puntos 2) (pos-x 5) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 116) (puntos 2) (pos-x 6) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 117) (puntos 2) (pos-x 7) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 118) (puntos 2) (pos-x 8) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 121) (puntos 2) (pos-x 1) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 122) (puntos 3) (pos-x 2) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 123) (puntos 3) (pos-x 3) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 124) (puntos 4) (pos-x 4) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 125) (puntos 4) (pos-x 5) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 126) (puntos 5) (pos-x 6) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 127) (puntos 5) (pos-x 7) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 128) (puntos 6) (pos-x 8) (pos-y 2) (descubierta 0)))

