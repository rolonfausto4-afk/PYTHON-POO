class Animal:
    def __init__(self,nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

    #crear metodo 
    def alimentarse(self):
        return (f"Este tipo de animales: {self.nombre} debido a su tamaño: {self.tamaño} "
        f"y su habitat: {self.habitat} posee un tipo de alimentacion: {self.dieta}")
    
    def comunicacion(self):
        return (f"Este tipo de animales: {self.nombre} se comunican de diferentes formas: "
        f"pudiendo usar su apariencia,como su color: {self.color}, o su tamaño: {self.tamaño}")
    
    def moverse(self,dato_movimiento):
        return f"La forma de moverse es estos animales: {self.nombre} es: {dato_movimiento}"
    
    def cubrirse(self,dato_proteccion):
        return f"Estos tipo de animales: {self.nombre}, se pueden proteger con sus {dato_proteccion}"
    
    def reproducirse(self,dato_reproduccion):
        return (f"Los animales: {self.nombre} se reproducen de diferentes formas, dependiendo "
        f"de su especie y habitat; en este caso el entorno de en un entorno: {self.habitat}. \n "
        f"El tipo de desarrollo embrionario es : {dato_reproduccion}")
    
    def adaptarse(self,dato_adaptacion):
        return f"Estos animales: {self.nombre} poseen un tipo de adaptacion: {dato_adaptacion} "
    
    def dormir(self,dato_sueno):
        return f"Estos animales: {self.nombre} posee un tipo de sueño: {dato_sueno} "