from MODELO_ANIMAL import Animal

class Mamifero(Animal):
    def __init__(self,nombre, edad, habitat, dieta, tamaño, color, pelo):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.pelo = pelo

    def alimentar_crias(self):
        return f"Los {self.nombre} alimentan a sus crías con leche materna"
    
    def Mostrar_info(self,dato_movimiento, dato_reproduccion, dato_adaptacion, dato_sueno):
        mensaje= (f"---- Propiedades de los {self.nombre}----\n")
        mensaje+= (self.moverse(dato_movimiento)+"\n")
        mensaje+= (self.alimentarse()+"\n")
        mensaje+= (self.comunicacion()+"\n")
        mensaje+= (self.reproducirse(dato_reproduccion)+"\n")
        mensaje+= (self.adaptarse(dato_adaptacion)+"\n")
        mensaje+= (self.dormir(dato_sueno)+"\n")
        mensaje+= (self.alimentar_crias()+"\n")
        mensaje+= (self.cubrirse(self.pelo)+"\n")

        return mensaje