#crear las clases
class Carro:
    #crear el constructor
    def __init__(self,modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible):
        self.modelo= modelo
        self.color= color
        self.motor= motor
        self.numero_puertas= numero_puertas
        self.capacidad_pasajeros= capacidad_pasajeros
        self.tipo_combustibles= tipo_combustible
    
    #setter y getter

    def set_modelo(self,dato_modelo):
        self.modelo= dato_modelo

    def get_modelo(self):
        return self.modelo
    
    def set_color(self,dato_color):
        self.color= dato_color

    def get_color(self):
        return self.color
    
    def set_motor(self,dato_motor):
        self.motor= dato_motor

    def get_motor(self):
        return self.motor
    
    def set_numero_puertas(self,dato_numero_puertas):
        self.numero_puertas= dato_numero_puertas

    def get_numero_puertas(self):
        return self.numero_puertas

    def set_capacidad_pasajeros(self,dato_capacidad_pasajeros):
        self.capacidad_pasajeros= dato_capacidad_pasajeros

    def get_capacidad_pasajeros(self):
        return self.capacidad_pasajeros
    
    def set_tipo_combustible(self,dato_tipo_combustible):
        self.tipo_combustible= dato_tipo_combustible

    def get_tipo_combustible(self):
        return self.tipo_combustible
    
    
    #crear metodos

    def arrancar(self,dato_motor):
        self.set_motor(dato_motor)
        if self.get_motor()=="Activo":
            return (f"El motor esta en prendido, el auto puede arrancar")

    def apagar(self,dato_motor):
        self.set_motor(dato_motor)
        if self.get_motor()=="Apagado":
            return (f"El motor se encuentra apagado")

    def acelerar(self,dato_motor,dato_aceleracion,dato_modelo):
        self.set_motor(dato_motor)
        self.set_modelo(dato_modelo)

        #mensaje para el motor
        if self.get_motor()=="Activo":
            mensaje= f"{self.arrancar(dato_motor)} \n"
            if dato_aceleracion=="Activo" and self.get_modelo()=="Deportivo":
                mensaje += (f"Este auto esta acelerando, ten cuidado que es una fiera ") 
            elif dato_aceleracion=="Activo" and self.get_modelo()!="Deportivo":
                mensaje += (f"El auto esta acelerando ")
            else:
                mensaje += (f"El auto no esta acelerando")
        else:
            mensaje= f"{self.apagar(dato_motor)} "
    
        #mensaje para celeracion

 
        return mensaje

    def frenar(self,dato_modelo):
        self.set_modelo(dato_modelo)
        if self.get_modelo()=="Camion":
            return (f"El camion tiene frenos, pero hay probabilidad de que ya no los tenga 😥")
        else:
            return (f"El carro frena de manera rapida")
    
    def combustible(self,dato_tipo_combustible):
        self.set_tipo_combustible(dato_tipo_combustible)
        return (f"El tipo de combustible es: {self.get_tipo_combustible()}")

    def luces(self,dato_color):
        self.set_color(dato_color)
        return (f"La luces del carro son : {self.get_color()}")

    def tipo_seguridad(self,dato_numero_puertas,dato_modelo):
        self.set_numero_puertas(dato_numero_puertas)
        self.set_modelo(dato_modelo)
        if self.get_modelo()=="Camion":
            return (f"El carro posee: {self.get_numero_puertas()} puertas un poco desgastadas")
        else:
            return (f"El carro posee: {self.get_numero_puertas()} puertas bien protegidas")