from MODELO_ANIMAL import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, escamas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.escamas= escamas

    def respiracion(self):
        return f"Los {self.nombre} poseen respiracion branquial"
    
    def Mostrar_info(self,dato_movimiento, dato_reproduccion, dato_adaptacion, dato_sueno):
        mensaje= (f"---- Propiedades: {self.nombre}----\n")
        mensaje+= (self.moverse(dato_movimiento)+"\n")
        mensaje+= (self.alimentarse()+"\n")
        mensaje+= (self.comunicacion()+"\n")
        mensaje+= (self.reproducirse(dato_reproduccion)+"\n")
        mensaje+= (self.adaptarse(dato_adaptacion)+"\n")
        mensaje+= (self.respiracion()+"\n")
        mensaje+= (self.dormir(dato_sueno)+"\n")
        mensaje+= (self.cubrirse(self.escamas)+"\n")

        return mensaje