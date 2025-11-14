class Base_datos:
    def __init__(self):
          self.lista_carro= []
        
    def agregar_carro(self,dato_carro):            
        self.lista_carro.append(dato_carro)

    def extender_lista(self,dato_agregado):
        self.lista_carro.extend(dato_agregado)

    def eliminar_dato_lista(self,dato_posicion):
        self.lista_carro.pop(dato_posicion)

    def insertar_dato_lista(self,dato_posicion):
        self.lista_carro.insert(dato_posicion)

    def remover_lista(self):
        self.lista_carro.remove()
        
    def posicion_dato(self,dato_index):
        self.lista_carro.index(dato_index)

    def contar_dato(self):
        self.lista_carro.count()

    def ordenar_lista(self):
        self.lista_carro.sort()

    def invertir(self):
        self.lista_carro.reverse()

    def arrojar_info(self):
        for carro in self.lista_carro:
            print(f"{carro}\n")