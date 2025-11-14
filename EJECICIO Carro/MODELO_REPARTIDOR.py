from MODELO_CARRO import Carro

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
        return (f"La camioneta puede cargar hasta: {self.get_capacidad_carga()} metros cubicos de mercancia \n")
    
    def mostar_metodos(self,dato_motor,dato_aceleracion,dato_modelo,dato_tipo_combustible,dato_color,dato_numero_puertas,dato_capacidad_carga):
        
        mensaje= (f"PROPIEDADES DEL CARRO REPARTIDOR\n")
        mensaje+= (f"{self.acelerar(dato_motor, dato_aceleracion, dato_modelo)} \n")
        mensaje+= (f"{self.frenar(dato_modelo)} \n")
        mensaje+= (f"{self.combustible(dato_tipo_combustible)} \n")
        mensaje+= (f"{self.luces(dato_color)} \n")
        mensaje+= (f"{self.tipo_seguridad(dato_numero_puertas, dato_modelo)} \n")
        mensaje+= (f"{self.cargar(dato_capacidad_carga)} \n")

        return mensaje