class Base_datos:
    def __init__(self):
        self.lista_botella= []
    
    def agregar_botella(self,dato_botella):
        self.lista_botella.append(dato_botella)

    def extender_lista(self,dato_agregado):
        self.lista_botella.extend(dato_agregado)

    def eliminar_dato_lista(self,dato_posicion):
        self.lista_botella.pop(dato_posicion)

    def insertar_dato_lista(self,dato_posicion):
        self.lista_botella.insert(dato_posicion)

    def remover_lista(self):
        self.lista_botella.remove()
    
    def posicion_dato(self,dato_index):
        self.lista_botella.index(dato_index)

    def contar_dato(self):
        self.lista_botella.count()

    def ordenar_lista(self):
        self.lista_botella.sort()

    def invertir(self):
        self.lista_botella.reverse()

    def arrojar_info(self):
        for botella in self.lista_botella:
            print(f"{botella}\n")

            
    
