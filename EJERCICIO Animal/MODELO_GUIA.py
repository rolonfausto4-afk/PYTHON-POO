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
        return (f"Este tipo de animales: {self.nombre} debido a su tamaño: {self.tamaño}"
        f"y su habitat: {self.habitat} se alimentan de: {self.dieta}")
    
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

#----------codigo principal----------

obj_bd= Base_Datos()
obj_mamifero= Mamifero("Mamiferos", 5, "Domestico", "Carnívora", "Mediano", "Marrón", "Pelaje")
obj_pez= Pez("Peces", 2, "Acuático", "Omnívora", "Pequeño", "Plateado", "Escamas")
obj_ave= Ave("Aves", 3, "Aéreo", "Herbívora", "Pequeño", "Multicolor", "Plumas")
obj_reptil= Reptil("Reptiles", 4, "Terrestre", "Carnívora", "Grande", "Verde", "Escamas")
obj_insecto= Insecto("Insectos", 1, "Variado", "Herbívora", "Muy pequeño", "Negro", "Exoesqueleto")

obj_mostrar_mamifero = obj_mamifero.Mostrar_info("Corriendo/Caminando", "Vivíparo", "Nomada", "Nocturno")
obj_mostrar_pez = obj_pez.Mostrar_info("Nadando", "Ovíparo", "Dependeniente", "Diurno")
obj_mostrar_ave = obj_ave.Mostrar_info("Volando", "Ovíparo", "Migratoria", "Diurno")
obj_mostrar_reptil = obj_reptil.Mostrar_info("Corriendo/Caminando o Reptando", "Ovíparo", "Termorregulatoria", "Diurno")
obj_mostrar_insecto = obj_insecto.Mostrar_info("poseen todo tipo de movimiento", "Ovíparo", "Dependiente", "Diurno")

obj_bd.extender_lista([obj_mostrar_mamifero, obj_mostrar_pez, obj_mostrar_ave, obj_mostrar_reptil, obj_mostrar_insecto])
obj_bd.mostrar_animales()



    


    

    
     
        