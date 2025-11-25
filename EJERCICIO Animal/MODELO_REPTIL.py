from MODELO_ANIMAL import Animal

class Reptil(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, escamas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.escamas= escamas

    def mudar_piel(self):
        return f"Los {self.nombre} mudan su piel para crecer y eliminar parásitos"
    
    def Mostrar_info(self,dato_movimiento, dato_reproduccion, dato_adaptacion, dato_sueno):
        mensaje= (f"---- Propiedades: {self.nombre}----\n")
        mensaje+= (self.moverse(dato_movimiento)+"\n")
        mensaje+= (self.alimentarse()+"\n")
        mensaje+= (self.comunicacion()+"\n")
        mensaje+= (self.reproducirse(dato_reproduccion)+"\n")
        mensaje+= (self.adaptarse(dato_adaptacion)+"\n")
        mensaje+= (self.dormir(dato_sueno)+"\n")
        mensaje+= (self.mudar_piel()+"\n")
        mensaje+= (self.cubrirse(self.escamas)+"\n")

        return mensaje