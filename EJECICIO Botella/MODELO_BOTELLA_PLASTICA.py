from MODELO_BOTELLA import Botella
#------------Crear la clase------------------------------------   
class Botella_Plastica(Botella):
#-------------Crear el constructor-----------------------------
    def __init__(self, material, capacidad, forma, tapa, diseño, grabado):
        super().__init__(material, capacidad, forma, tapa, diseño)
        self.grabado= grabado
        
#---------obtener(set) y poner(get) para atributos-------------

    def set_grabado(self,dato_grabado):
        self.grabado = dato_grabado
        
    def get_grabado(self):
        return self.grabado
    
#--------------Crear los metodos-------------------------------
    def poner_grabado(self,dato_grabado):
        self.set_grabado(dato_grabado)
        return(f"El grabado de la botella es: {self.get_grabado()}")


    def adherir_propiedades(self, dato_capacidad, dato_tapa, dato_material, dato_resistencia, dato_forma, dato_diseño, 
                            dato_grabado, dato_transparencia, dato_reciclable, dato_caja):
        
        propiedades = f"PROPIEDADES PLASTICAS \n"
        propiedades += f"{super().contener_liquidos(dato_capacidad)}\n"
        propiedades += f"{super().cerrar(dato_tapa)}\n"
        propiedades += f"{super().poseer_resistencia(dato_material, dato_resistencia)}\n"
        propiedades += f"{super().poseer_transparencia(dato_material, dato_transparencia)}\n"
        propiedades += f"{super().ser_reciclable(dato_material, dato_reciclable)}"
        propiedades += f"{self.get_grabado()}\n"
        propiedades += f"{super().transporte(dato_forma, dato_diseño, dato_caja)}\n"
        propiedades += f"{self.poner_grabado(dato_grabado)}\n"

        return propiedades