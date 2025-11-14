from MODELO_ANIMAL import Animal

class Ave(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color,plumas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.plumas= plumas

    def crear_nido(self):
        return f"Las {self.nombre} pueden crear nidos para proteger a sus crías"
    
    def Mostrar_info(self,dato_movimiento, dato_reproduccion, dato_adaptacion, dato_sueno):
        mensaje= (f"---- Propiedades: {self.nombre}----\n")
        mensaje+= (self.moverse(dato_movimiento)+"\n")
        mensaje+= (self.alimentarse()+"\n")
        mensaje+= (self.comunicacion()+"\n")
        mensaje+= (self.crear_nido()+"\n")
        mensaje+= (self.adaptarse(dato_adaptacion)+"\n")
        mensaje+= (self.dormir(dato_sueno)+"\n")
        mensaje+= (self.crear_nido()+"\n")
        mensaje+= (self.cubrirse(self.plumas)+"\n")

        return mensaje