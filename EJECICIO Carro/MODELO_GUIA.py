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
            print(f"El motor esta en prendido, el auto puede arrancar")

    def apagar(self,dato_motor):
        self.set_motor(dato_motor)
        if self.get_motor()=="Apagado":
            print(f"El motor se encuentra apagado")

    def acelerar(self,dato_motor,dato_aceleracion,dato_modelo):
        self.set_motor(dato_motor)
        self.set_modelo(dato_modelo)
        if self.get_motor()=="Activo":
            self.arrancar(dato_motor)
            if dato_aceleracion=="Activo" and self.get_modelo()=="Deportivo":
                print(f"Este auto es una esta acelerando, ten cuidado que es una fiera") 
            elif dato_aceleracion=="Activo" and self.get_modelo()!="Deportivo":
                print(f"El auto esta acelerando")
            else:
                print(f"El auto no esta acelerando")
        else:
            self.apagar(dato_motor)

    def frenar(self,dato_modelo):
        self.set_modelo(dato_modelo)
        if self.get_modelo()=="Camion":
            print(f"El camion tiene frenos, pero hay probabilidad de que ya no los tenga 😥")
        else:
            print(f"El carro frena de manera rapida")
    
    def combustible(self,dato_tipo_combustible):
        self.set_tipo_combustible(dato_tipo_combustible)
        print(f"El tipo de combustible es: {self.get_tipo_combustible()}")

    def luces(self,dato_color):
        self.set_color(dato_color)
        print(f"La luces del carro son : {self.get_color()}")

    def tipo_seguridad(self,dato_numero_puertas,dato_modelo):
        self.set_numero_puertas(dato_numero_puertas)
        self.set_modelo(dato_modelo)
        if self.get_modelo()=="Camion":
            print(f"El carro posee: {self.get_numero_puertas()} puertas un poco desgastadas")
        else:
            print(f"El carro posee: {self.get_numero_puertas()} puertas bien protegidas")

#crear clase hija
class Deportivo(Carro):
    def __init__(self,modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible,velocidad_maxima):
        super().__init__(modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible)
    
    #crear metodos

    def climatizador(self,dato_climatizador):
            print(f"El carro posee un sistema de refresco minimo de: {dato_climatizador}°C  con un aire fluido y fresco \n" )

    def mostar_metodos(self,dato_motor,dato_aceleracion,dato_modelo,dato_tipo_combustible,dato_color,dato_numero_puertas,dato_climatizador):
        print("-----CUALIDADES DEL CLASE DEPORTIVO-----")
        self.acelerar(dato_motor, dato_aceleracion, dato_modelo)
        self.frenar(dato_modelo)
        self.combustible(dato_tipo_combustible)
        self.luces(dato_color)
        self.tipo_seguridad(dato_numero_puertas, dato_modelo)
        self.climatizador(dato_climatizador)

#crear clase hija
class Repartidor(Carro):
    def __init__(self,modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible,capacidad_carga):
        super().__init__(modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible)
        self.capacidad_carga= capacidad_carga  
    
    #setter y getter

    def set_capacidad_carga(self,dato_capacidad_carga):
        self.capacidad_carga= dato_capacidad_carga
    
    def get_capacidad_carga(self):
        return self.capacidad_carga
    
    #crear metodos

    def cargar(self,dato_capacidad_carga):
        self.set_capacidad_carga(dato_capacidad_carga)
        print(f"La camioneta puede cargar hasta: {self.get_capacidad_carga()} metros cubicos de mercancia \n")
    
    def mostar_metodos(self,dato_motor,dato_aceleracion,dato_modelo,dato_tipo_combustible,dato_color,dato_numero_puertas,dato_capacidad_carga):
        print("-----CUALIDADES DEL CLASE CAMIONETA-----")
        self.acelerar(dato_motor, dato_aceleracion, dato_modelo)
        self.frenar(dato_modelo)
        self.combustible(dato_tipo_combustible)
        self.luces(dato_color)
        self.tipo_seguridad(dato_numero_puertas, dato_modelo)
        self.cargar(dato_capacidad_carga)

#crear clase hija
class Camion(Carro):
    def __init__(self,modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible,carga):
        super().__init__(modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible)
        self.carga= carga
    
    #setter y getter

    def set_carga(self,dato_carga):
        self.carga= dato_carga
    
    def get_carga(self):
        return self.carga
    
    #crear metodos

    def transportar_carga(self,dato_carga):
        self.set_carga(dato_carga)
        print(f"El camion puede transportar mercancia pesada de más de : {self.get_carga()}\n ")
    
    def mostar_metodos(self,dato_motor,dato_aceleracion,dato_modelo,dato_tipo_combustible,dato_color,dato_numero_puertas,dato_carga):
        print("-----CUALIDADES DEL CLASE CAMION-----")
        self.acelerar(dato_motor, dato_aceleracion, dato_modelo)
        self.frenar(dato_modelo)
        self.combustible(dato_tipo_combustible)
        self.luces(dato_color)
        self.tipo_seguridad(dato_numero_puertas, dato_modelo)
        self.transportar_carga(dato_carga)


#------------principal----------------
carro_deportivo= Deportivo(1,1,1,1,1,1,1)
carro_camioneta= Repartidor(1,1,1,1,1,1,1)
carro_camion= Camion(1,1,1,1,1,1,1)

carro_deportivo.mostar_metodos("Activo","Activo","Deportivo","Gasolina","Blanco","2","18")
carro_camioneta.mostar_metodos("Activo","Apagado","Camioneta","Diesel","Amarillo","4","12")
carro_camion.mostar_metodos("Activo","Activo","Camion","Diesel","Amarillo","2","8")