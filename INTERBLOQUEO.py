import threading

# Crear dos bloqueos
bloqueo1 = threading.Lock()
bloqueo2 = threading.Lock()

def tarea1():
    print("Tarea 1: Intentando adquirir bloqueo 1")
    with bloqueo1:
        print("Tarea 1: Bloqueo 1 adquirido")
        print("Tarea 1: Intentando adquirir bloqueo 2")
        with bloqueo2:
            print("Tarea 1: Bloqueo 2 adquirido")

def tarea2():
    print("Tarea 2: Intentando adquirir bloqueo 2")
    with bloqueo2:
        print("Tarea 2: Bloqueo 2 adquirido")
        print("Tarea 2: Intentando adquirir bloqueo 1")
        with bloqueo1:
            print("Tarea 2: Bloqueo 1 adquirido")

# Crear hilos
hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Las tareas han finalizado.")
