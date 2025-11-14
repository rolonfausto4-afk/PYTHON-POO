#------------Crear la clase------------------------------------
class Botella:
#-------------Crear el constructor-----------------------------
    def __init__(self,material,capacidad,forma,tapa,diseño):
        self.material = material
        self.capacidad= capacidad
        self.forma= forma
        self.tapa= tapa
        self.diseño= diseño
    
#---------poner valor(set) y retorna/obtener(get) para atributos-------------

    def set_tapa(self,dato_tapa):
        self.tapa = dato_tapa
        
    def get_tapa(self):
        return self.tapa
    
    def set_material(self,dato_material):
        self.material = dato_material
        
    def get_material(self):
        return self.material
    
    def set_capacidad(self,dato_capacidad):
        self.capacidad = dato_capacidad
        
    def get_capacidad(self):
        return self.capacidad
    
    def set_forma(self,dato_forma):
        self.forma = dato_forma
        
    def get_forma(self):
        return self.forma
    
    def set_diseño(self,dato_diseño):
        self.diseño = dato_diseño
        
    def get_diseño(self):
        return self.diseño 
     
#--------------Crear los metodos-------------------------------

    def contener_liquidos(self,dato_capacidad):
        self.set_capacidad(dato_capacidad)
        print(f"la botella puede contener {self.get_capacidad()} militros")
    
    def cerrar(self,dato_tapa):
        self.set_tapa(dato_tapa)
        print(f"El tipo de cierre del la tapa es: {self.get_tapa()}")

    def poseer_transparencia(self, dato_material, dato_transparencia):
        self.set_material(dato_material)
        print(f"El material {self.get_material()} posee transparencia: {dato_transparencia}")
    
    def transporte(self,dato_forma, dato_diseño, dato_caja):
        self.set_forma(dato_forma)
        self.set_diseño(dato_diseño)
        print(f"debido a su forma: {self.get_forma()},  y su diseño: {self.get_diseño()}, se puede llevar marompibilidadimo: {dato_caja} unidades por caja ")
    
    def poseer_resistencia(self,dato_material,dato_resistencia):
        self.set_material(dato_material)
        print(f"debido al material: {self.get_material()} la resistencia es: {dato_resistencia} ")
    
    def ser_reciclable(self,dato_material,dato_reciclable):
        self.set_material(dato_material)
        print(f"las botellas con el material: {self.get_material()}, deben ir en el contenedor {dato_reciclable}")
        

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
        print(f"El grabado de la botella es: {self.get_grabado()}")

    def adherir_propiedades_basicas(self,dato_capacidad,dato_tapa,dato_material,dato_resistencia):
        print(f"PROPIEDADES BASICAS:\n")
        print(f"{super().contener_liquidos(dato_capacidad)} \n")
        print(f"{super().cerrar(dato_tapa)}\n")
        print(f"{super().poseer_resistencia(dato_material,dato_resistencia)}\n")
    
    def adherir_propiedades_secundarias(self,dato_material,dato_forma,dato_diseño,dato_grabado,dato_transparencia,dato_reciclable,dato_caja):
        print(f"PROPIEDADES SECUNDARIAS:\n")
        print(f"{super().poseer_transparencia(dato_material,dato_transparencia)}\n")
        print(f"{super().ser_reciclable(dato_material,dato_reciclable)}\n")
        print(f"{self.poner_grabado(dato_grabado)}\n")
        print(f"{super().transporte(dato_forma,dato_diseño,dato_caja)}")

        
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
        print(f"la rompibilidad de la botella es: {self.get_rompibilidad()}, a un golpe medio contra todo")

    def adherir_propiedades_basicas(self,dato_capacidad,dato_tapa,dato_material,dato_resistencia):
        print(f"PROPIEDADES BASICAS:\n")
        print(f"{super().contener_liquidos(dato_capacidad)} \n")
        print(f"{super().cerrar(dato_tapa)}\n")
        print(f"{super().poseer_resistencia(dato_material,dato_resistencia)}\n")
    
    def adherir_propiedades_secundarias(self,dato_material,dato_forma,dato_diseño,dato_rompibilidad,dato_transparencia,dato_reciclable,dato_caja):
        print(f"PROPIEDADES SECUNDARIAS:\n")
        print(f"{super().poseer_transparencia(dato_material,dato_transparencia)}\n")
        print(f"{super().ser_reciclable(dato_material,dato_reciclable)}\n")
        print(f"{self.quebrar(dato_rompibilidad)}\n")
        print(f"{super().transporte(dato_forma,dato_diseño,dato_caja)}")

        
#------------CODIGO PRINCIPAL-----------------------------------

objeto_a= Botella_Plastica(1,1,1,1,1,1)
objeto_b= Botella_Vidrio(1,1,1,1,1,1)

print("---------------BOTELLA DE PLASTICO---------------\n")
objeto_a.adherir_propiedades_basicas(1000,"cierre hermetico","plastico","baja al calor")
objeto_a.adherir_propiedades_secundarias("plastico","cilindrica con cuello minimo","moderno"," superficial con rayas azules","nitida","gris",10)

print("---------------BOTELLA DE VIDRIO-----------------\n")
objeto_b.adherir_propiedades_basicas(750,"cierre a presion","vidrio","alta al calor")
objeto_b.adherir_propiedades_secundarias("vidrio","cuerpo ancho con cuello estreño","clasico","frajil","turbia","amarillo",8)

        

        