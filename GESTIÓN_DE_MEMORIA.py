class BloqueMemoria:
    def __init__(self, inicio, tamaño):
        self.inicio = inicio
        self.tamaño = tamaño
        self.libre = True

    def __str__(self):
        estado = "Libre" if self.libre else "Ocupado"
        return f"Bloque desde {self.inicio} hasta {self.inicio + self.tamaño - 1} ({estado})"

class GestorMemoria:
    def __init__(self, tamaño_total):
        self.memoria = [BloqueMemoria(0, tamaño_total)]

    def asignar(self, tamaño):
        for bloque in self.memoria:
            if bloque.libre and bloque.tamaño >= tamaño:
                if bloque.tamaño > tamaño:
                    nuevo_bloque = BloqueMemoria(bloque.inicio + tamaño, bloque.tamaño - tamaño)
                    self.memoria.insert(self.memoria.index(bloque) + 1, nuevo_bloque)
                bloque.tamaño = tamaño
                bloque.libre = False
                print(f"Asignado: {bloque}")
                return bloque.inicio
        print("No hay suficiente memoria disponible para asignar.")
        return None

    def liberar(self, inicio):
        for bloque in self.memoria:
            if bloque.inicio == inicio and not bloque.libre:
                bloque.libre = True
                print(f"Liberado: {bloque}")
                self.compactar()
                return
        print("No se encontró el bloque para liberar.")

    def compactar(self):
        i = 0
        while i < len(self.memoria) - 1:
            actual = self.memoria[i]
            siguiente = self.memoria[i + 1]
            if actual.libre and siguiente.libre:
                actual.tamaño += siguiente.tamaño
                del self.memoria[i + 1]
            else:
                i += 1

    def mostrar_memoria(self):
        for bloque in self.memoria:
            print(bloque)

# Crear un gestor de memoria con 100 unidades de memoria
gestor = GestorMemoria(100)

# Asignar y liberar memoria
gestor.asignar(20)
gestor.asignar(30)
gestor.liberar(0)
gestor.asignar(10)
gestor.mostrar_memoria()
