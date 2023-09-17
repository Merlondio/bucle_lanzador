#!/usr/bin/python3

import time
import logging
import traceback

# Configuration de logging para sacar los logs a l stdout
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(levelname)s] %(asctime)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
# Variables
tiempo_entre_intervalos = 5
contador_iteraciones = 0

# Marcamos entrada al bucle
logging.info('Inicio de la ejecucion del BUCLE')

# Entramos en el bucle infinito de ejecuciones
while True:
    contador_iteraciones += 1
    logging.debug(f'Iteracion numero: {contador_iteraciones}')
    try:
        pass
        print (4/0)
    except Exception:
        error = traceback.format_exc()
        logging.error(error)
    else:
        pass
    finally:
        time.sleep(tiempo_entre_intervalos)
