def LoadFunctions(clips):
    mod_traducirM = clips.BuildModule("TRADUCIRM",
                                     "(import MAIN deftemplate initial-fact ficha ficha-r dimension tiempo mueve) (import MAIN deffunction ?ALL)")

    traducir = mod_traducirM.BuildRule("traducir",
                                       '(declare (salience 10)) (tiempo ?t) ?h1 <- (mueve (num ?n) (mov ?m) (tiempo ?t)) (ficha-r (equipo "B") (num ?n)) (not (traducido ?n ?t))',
                                       "(retract ?h1) (assert (traducido ?n ?t)) (assert (mueve (num ?n) (mov (simetrico ?m)) (tiempo ?t)))")
