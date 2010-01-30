;Leandro Team
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Reglas de Inteligencia Artificial                     
;  básicas para el equipo A                            
;
; Por Leandro Pastrana
;
; Disponible bajo los términos de la GNU General Public License (GPL) version 2 o superior
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;
; Inicializamos las fichas
;
; Bqui se pueden cambiar los puntos de la ficha de cada
;  posicion al comenzar la partida
;



(deffacts fichas-A
  (ficha-r (equipo "A") (num A111) (puntos 2) (pos-x 1) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A112) (puntos 3) (pos-x 1) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A121) (puntos 2) (pos-x 2) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A122) (puntos 2) (pos-x 2) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A132) (puntos 5) (pos-x 3) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A123) (puntos 2) (pos-x 3) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A141) (puntos 4) (pos-x 4) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A142) (puntos 2) (pos-x 4) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A151) (puntos 2) (pos-x 5) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A152) (puntos 6) (pos-x 5) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A161) (puntos 2) (pos-x 6) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A162) (puntos 2) (pos-x 6) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A171) (puntos 3) (pos-x 8) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A172) (puntos 5) (pos-x 8) (pos-y 2) (descubierta 0))
  (ficha-r (equipo "A") (num A181) (puntos 1) (pos-x 7) (pos-y 1) (descubierta 0))
  (ficha-r (equipo "A") (num A182) (puntos 4) (pos-x 7) (pos-y 2) (descubierta 0))
)
