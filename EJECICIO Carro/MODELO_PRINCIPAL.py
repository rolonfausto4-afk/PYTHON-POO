from MODELO_DEPORTIVO import Deportivo
from MODELO_REPARTIDOR import Repartidor
from MODELO_CAMION import Camion
from MODELO_BASE_DATOS import Base_datos

#------------principal----------------
objeto_base_datos= Base_datos()
carro_deportivo= Deportivo(1,1,1,1,1,1,1)
carro_camioneta= Repartidor(1,1,1,1,1,1,1)
carro_camion= Camion(1,1,1,1,1,1,1)

dato_deportivo = carro_deportivo.mostar_metodos("Apagado","Activo","Deportivo","Gasolina","Blanco","2","18")
dato_repartidor = carro_camioneta.mostar_metodos("Activo","Apagado","Camioneta","Diesel","Amarillo","4","12")
dato_camion= carro_camion.mostar_metodos("Activo","Activo","Camion","Diesel","Amarillo","2","8")

objeto_base_datos.agregar_carro(dato_deportivo)
objeto_base_datos.agregar_carro(dato_repartidor)
objeto_base_datos.agregar_carro(dato_camion)

objeto_base_datos.arrojar_info()


