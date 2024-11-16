import threading
import time
import queue

# Crear una cola de prioridad
cola_prioridad = queue.PriorityQueue()

# Función para tareas
def tarea(prioridad, nombre):
    while True:
        if not cola_prioridad.empty():
            _, tarea_actual = cola_prioridad.get()
            if tarea_actual == nombre:
                print(f"{nombre} está ejecutándose")
                time.sleep(1)  # Simula trabajo
                cola_prioridad.task_done()
                break
        else:
            print(f"{nombre} sigue esperando...")
            time.sleep(0.5)  # Espera antes de intentar de nuevo

# Añadir tareas a la cola con diferentes prioridades
cola_prioridad.put((1, "Tarea de alta prioridad"))
cola_prioridad.put((2, "Tarea de media prioridad"))
cola_prioridad.put((3, "Tarea de baja prioridad"))

# Crear hilos para cada tarea
hilos = []
for prioridad, nombre in [(1, "Tarea de alta prioridad"), (2, "Tarea de media prioridad"), (3, "Tarea de baja prioridad")]:
    hilo = threading.Thread(target=tarea, args=(prioridad, nombre))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todas las tareas terminen
for hilo in hilos:
    hilo.join()

print("Todas las tareas han finalizado.")
