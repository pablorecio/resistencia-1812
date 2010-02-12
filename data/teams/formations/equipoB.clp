;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     
;  básicas para el equipo B                            
;
;  Por Manuel Palomo Duarte
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

; Fichas del equipo A, sus num son 2XY
; Empiezan en las y 8 y 7

(deffacts fichas-A
  (ficha-r (equipo "A") (num 211) (puntos 1) (pos-x 1) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 212) (puntos 2) (pos-x 2) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 213) (puntos 2) (pos-x 3) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 214) (puntos 2) (pos-x 4) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 215) (puntos 2) (pos-x 5) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 216) (puntos 2) (pos-x 6) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 217) (puntos 2) (pos-x 7) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 218) (puntos 2) (pos-x 8) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num 221) (puntos 2) (pos-x 1) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 222) (puntos 3) (pos-x 2) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 223) (puntos 3) (pos-x 3) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 224) (puntos 4) (pos-x 4) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 225) (puntos 4) (pos-x 5) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 226) (puntos 5) (pos-x 6) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 227) (puntos 5) (pos-x 7) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num 228) (puntos 6) (pos-x 8) (pos-y 2) (descubierta 0)))

