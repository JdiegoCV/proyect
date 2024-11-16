import threading
import time

# Crear bloqueos
bloqueoA = threading.Lock()
bloqueoB = threading.Lock()

# Contador compartido
contador = 0

# Tarea de concurrencia
def tarea_concurrencia():
    global contador
    for i in range(5):
        with bloqueoA:
            contador += 1
            print(f"Tarea de concurrencia incrementa contador a {contador}")
        time.sleep(1)

# Tarea de interbloqueo
def tarea_interbloqueo1():
    print("Tarea de interbloqueo 1: Intentando adquirir bloqueo A")
    with bloqueoA:
        print("Tarea de interbloqueo 1: Bloqueo A adquirido")
        time.sleep(1)
        print("Tarea de interbloqueo 1: Intentando adquirir bloqueo B")
        with bloqueoB:
            print("Tarea de interbloqueo 1: Bloqueo B adquirido")

def tarea_interbloqueo2():
    print("Tarea de interbloqueo 2: Intentando adquirir bloqueo B")
    with bloqueoB:
        print("Tarea de interbloqueo 2: Bloqueo B adquirido")
        time.sleep(1)
        print("Tarea de interbloqueo 2: Intentando adquirir bloqueo A")
        with bloqueoA:
            print("Tarea de interbloqueo 2: Bloqueo A adquirido")

# Tarea de inanición
def tarea_inanicion():
    global contador
    while True:
        if bloqueoA.acquire(blocking=False):
            try:
                contador += 1
                print(f"Tarea en inanición incrementa contador a {contador}")
            finally:
                bloqueoA.release()
            break
        else:
            print("Tarea en inanición no puede adquirir el bloqueo y sigue esperando...")
        time.sleep(0.5)  # Espera antes de intentar de nuevo

# Crear hilos
hilo_concurrencia = threading.Thread(target=tarea_concurrencia)
hilo_interbloqueo1 = threading.Thread(target=tarea_interbloqueo1)
hilo_interbloqueo2 = threading.Thread(target=tarea_interbloqueo2)
hilo_inanicion = threading.Thread(target=tarea_inanicion)

# Iniciar hilos
hilo_concurrencia.start()
hilo_interbloqueo1.start()
hilo_interbloqueo2.start()
hilo_inanicion.start()

# Esperar a que los hilos terminen
hilo_concurrencia.join()
hilo_interbloqueo1.join()
hilo_interbloqueo2.join()
hilo_inanicion.join()

print("Todas las tareas han finalizado.")
