from MODELO_DEPORTIVO import Deportivo
from MODELO_REPARTIDOR import Repartidor
from MODELO_CAMION import Camion
from MODELO_BASE_DATOS import Base_datos
objeto_base_datos= Base_datos()
carro_deportivo= Deportivo(1,1,1,1,1,1,1)
carro_camioneta= Repartidor(1,1,1,1,1,1,1)
carro_camion= Camion(1,1,1,1,1,1,1)

#---Funciones---
#menu principal
def colocar_deportivo():
    estado_motor= input("Ingrese el estado del motor (Activo/Apagado): ")
    estado_acelera= input("Ingrese el estado de la aceleracion (Activo/Apagado): ")
    tipo_carro= "Deportivo"
    tipo_combustible= input("Ingrese el tipo de combustible (Gasolina/Diesel): ")
    color_carro= input("Ingrese el color del carro: ")
    numero_puertas= input("Ingrese el numero de puertas: ")
    tamaño_llantas= input("Ingrese la temperatura minima del aire acondicionado: ")

    dato_deportivo= carro_deportivo.mostar_metodos(estado_motor,estado_acelera,tipo_carro,tipo_combustible,color_carro,numero_puertas,tamaño_llantas)

    return dato_deportivo


def colocar_repartidor():
    estado_motor= input("Ingrese el estado del motor (Activo/Apagado): ")
    estado_acelera= input("Ingrese el estado de la aceleracion (Activo/Apagado): ")
    tipo_carro= "Repartidor"
    tipo_combustible= input("Ingrese el tipo de combustible (Gasolina/Diesel): ")
    color_carro= input("Ingrese el color del carro: ")
    numero_puertas= input("Ingrese el numero de puertas: ")
    tamaño_carga= input("Ingrese el volumen de la capacidad del carro: ")

    dato_repartidor= carro_camioneta.mostar_metodos(estado_motor,estado_acelera,tipo_carro,tipo_combustible,color_carro,numero_puertas,tamaño_carga)

    return dato_repartidor


def colocar_camion():
    estado_motor= input("Ingrese el estado del motor (Activo/Apagado): ")
    estado_acelera= input("Ingrese el estado de la aceleracion (Activo/Apagado): ")
    tipo_carro= "Camion"
    tipo_combustible= input("Ingrese el tipo de combustible (Gasolina/Diesel): ")
    color_carro= input("Ingrese el color del carro: ")
    numero_ejes= input("Ingrese el numero de ejes: ")
    capacidad_carga= input("Ingrese la capacidad de carga: ")

    dato_camion= carro_camion.mostar_metodos(estado_motor,estado_acelera,tipo_carro,tipo_combustible,color_carro,numero_ejes,capacidad_carga)

    return dato_camion


def agregar_carro():
    print("-----AGREGAR CARRO-----")
    print("1. Deportivo")
    print("2. Repartidor")
    print("3. Camion")
    tipo_carro= int(input("Seleccione el tipo de carro a agregar: "))

    return tipo_carro

def seleccinar_opcion_b_d():
    dato=0
    while True:
        print("-----MENU PRINCIPAL-----")
        print("1. Agregar carro")
        print("2. Mostrar carros")
        print("3. Eliminar carro")
        print("3. Salir")
        opcion= int(input("Seleccione una opcion: "))

        match opcion:
            case 1:
                tipo_carro= agregar_carro()
                match tipo_carro:
                    case 1:
                        dato_deportivo= colocar_deportivo()
                        objeto_base_datos.agregar_carro(dato_deportivo)
                        dato= dato+1
                    case 2:
                        dato_repartidor= colocar_repartidor()
                        objeto_base_datos.agregar_carro(dato_repartidor)
                        dato= dato+1
                    case 3:
                        dato_camion= colocar_camion()
                        objeto_base_datos.agregar_carro(dato_camion)
                        dato= dato+1
                    case _:
                        print("Opcion invalida") 
            case 2:
                objeto_base_datos.arrojar_info()
            case 3:
                print(f"Hay {dato} datos en la lista. \n Tenga en cuenta que los ID empiezan a contar desde el 0.")
                id_eliminar= int(input("Ingrese el ID del carro que desea eliminar: "))
                objeto_base_datos.eliminar_dato_lista(id_eliminar)
            case 4:
                print("Fin de la operacion")
                break


#------------principal----------------
seleccinar_opcion_b_d()



