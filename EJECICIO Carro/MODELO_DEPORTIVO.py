from MODELO_CARRO import Carro

#crear clase hija
class Deportivo(Carro):
    def __init__(self,modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible,climatizador):
        super().__init__(modelo,color,motor,numero_puertas,capacidad_pasajeros,tipo_combustible)
        self.climatizador= climatizador
    
    #setter y getter
    def set_climatizador(self,dato_climatizador):
        self.climatizador= dato_climatizador

    def get_climatizador(self):
        return self.climatizador
    
    #crear metodos

    def aderir_climatizador(self,dato_climatizador):
        self.set_climatizador(dato_climatizador)
        return (f"El carro posee un sistema de refresco minimo de: {self.get_climatizador()}°C  con un aire fluido y fresco \n" )

    def mostar_metodos(self,dato_motor,dato_aceleracion,dato_modelo,dato_tipo_combustible,dato_color,dato_numero_puertas,dato_climatizador):
        
        mensaje= (f"PROPIEDADES DEL CARRO DEPORTIVO \n")
        mensaje+= (f"{self.acelerar(dato_motor, dato_aceleracion, dato_modelo)} \n")
        mensaje+= (f"{self.frenar(dato_modelo)} \n")
        mensaje+= (f"{self.combustible(dato_tipo_combustible)} \n")
        mensaje+= (f"{self.luces(dato_color)} \n")
        mensaje+= (f"{self.tipo_seguridad(dato_numero_puertas, dato_modelo)} \n")
        mensaje+= (f"{self.aderir_climatizador(dato_climatizador)} \n")

        return mensaje