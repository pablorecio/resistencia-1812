# Soporte de logging unificado para toda la aplicacion.
# -*- coding: utf-8 -*-

import logging

def getlog(name, filename= "", level = ""):
    # DEBUG por defecto si no se especifica, en otro caso, INFO
    LEVEL = logging.DEBUG if not level else logging.INFO
    FILENAME = filename

    #Formato para el log
    FORMAT = "%(levelname)s    \t%(name)s:  %(message)s"

    logging.basicConfig(filename=FILENAME, format=FORMAT, level=LEVEL)
    return logging.getLogger(name)
