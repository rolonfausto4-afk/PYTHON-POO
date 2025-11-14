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
        return f"la botella puede contener {self.get_capacidad()} militros"
    
    def cerrar(self,dato_tapa):
        self.set_tapa(dato_tapa)
        return f"El tipo de cierre del la tapa es: {self.get_tapa()}"

    def poseer_transparencia(self, dato_material, dato_transparencia):
        self.set_material(dato_material)
        return f"El material {self.get_material()} posee transparencia: {dato_transparencia}"
    
    def transporte(self,dato_forma, dato_diseño, dato_caja):
        self.set_forma(dato_forma)
        self.set_diseño(dato_diseño)
        return f"debido a su forma: {self.get_forma()},  y su diseño: {self.get_diseño()}, se puede llevar marompibilidadimo: {dato_caja} unidades por caja "
    
    def poseer_resistencia(self,dato_material,dato_resistencia):
        self.set_material(dato_material)
        return f"debido al material: {self.get_material()} la resistencia es: {dato_resistencia} "
    
    def ser_reciclable(self,dato_material,dato_reciclable):
        self.set_material(dato_material)
        return f"las botellas con el material: {self.get_material()}, deben ir en el contenedor {dato_reciclable}"