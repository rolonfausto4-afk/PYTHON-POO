class Base_Datos():
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def extender_lista(self, lista_animales):
        self.animales.extend(lista_animales)

    def eliminar_animal(self, dato_posicion):
        self.animales.pop(dato_posicion)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)