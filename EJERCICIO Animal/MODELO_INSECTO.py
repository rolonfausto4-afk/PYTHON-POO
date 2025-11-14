from MODELO_ANIMAL import Animal

class Insecto(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, exoesqueleto):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.exoesqueleto= exoesqueleto

    def metamorfosis(self):
        return f"Los {self.nombre} para llegar a ser insectos pasar por una fase lalvaria para luego convertirse en adultos"
    
    def Mostrar_info(self,dato_movimiento, dato_reproduccion, dato_adaptacion, dato_sueno):
        mensaje= (f"---- Propiedades: {self.nombre}----\n")
        mensaje+= (self.moverse(dato_movimiento)+"\n")
        mensaje+= (self.alimentarse()+"\n")
        mensaje+= (self.comunicacion()+"\n")
        mensaje+= (self.reproducirse(dato_reproduccion)+"\n")
        mensaje+= (self.adaptarse(dato_adaptacion)+"\n")
        mensaje+= (self.dormir(dato_sueno)+"\n")
        mensaje+= (self.metamorfosis()+"\n")
        mensaje+= (self.cubrirse(self.exoesqueleto)+"\n")

        return mensaje