from MODELO_BOTELLA import Botella
#------------Crear la clase------------------------------------   
class Botella_Vidrio(Botella):
#-------------Crear el constructor-----------------------------
    def __init__(self, material, capacidad, forma, tapa, diseño, rompibilidad):
        super().__init__(material, capacidad, forma, tapa, diseño)
        self.rompibilidad= rompibilidad
        
#---------obtener(set) y poner(get) para atributos-------------

    def set_rompibilidad(self,dato_rompibilidad):
        self.rompibilidad = dato_rompibilidad
        
    def get_rompibilidad(self):
        return self.rompibilidad
    
#--------------Crear los metodos-------------------------------
    def quebrar(self,dato_rompibilidad):
        self.set_rompibilidad(dato_rompibilidad)
        return (f"la rompibilidad de la botella es: {self.get_rompibilidad()}, a un golpe medio contra todo")

    def adherir_propiedades(self, dato_capacidad, dato_tapa, dato_material, dato_resistencia, dato_forma, dato_diseño, 
                            dato_rompibilidad, dato_transparencia, dato_reciclable, dato_caja):
        propiedades = f"PROPIEDADES VIDRICAS \n"
        propiedades += f"{super().contener_liquidos(dato_capacidad)}\n"
        propiedades += f"{super().cerrar(dato_tapa)}\n"
        propiedades += f"{super().poseer_resistencia(dato_material, dato_resistencia)}\n"
        propiedades += f"{super().poseer_transparencia(dato_material, dato_transparencia)}\n"
        propiedades += f"{super().ser_reciclable(dato_material, dato_reciclable)}\n"
        propiedades += f"{self.quebrar(dato_rompibilidad)}\n"
        propiedades += f"{super().transporte(dato_forma, dato_diseño, dato_caja)}"
        
        return propiedades