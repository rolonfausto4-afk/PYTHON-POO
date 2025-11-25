from MODELO_CARRO import Carro

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
        return (f"El camion puede transportar mercancia pesada de más de : {self.get_carga()}\n ")
    
    def mostar_metodos(self,dato_motor,dato_aceleracion,dato_modelo,dato_tipo_combustible,dato_color,dato_numero_puertas,dato_carga):
        
        mensaje=  (f"PROPIEDADES DEL CARRO CAMION \n")
        mensaje+= (f"{self.acelerar(dato_motor, dato_aceleracion, dato_modelo)} \n")
        mensaje+= (f"{self.frenar(dato_modelo)} \n")
        mensaje+= (f"{self.combustible(dato_tipo_combustible)} \n")
        mensaje+= (f"{self.luces(dato_color)} \n")
        mensaje+= (f"{self.tipo_seguridad(dato_numero_puertas, dato_modelo)} \n")
        mensaje+= (f"{self.transportar_carga(dato_carga)} \n")

        return mensaje