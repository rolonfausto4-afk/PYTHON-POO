from MODELO_BOTELLA_PLASTICA import Botella_Plastica
from MODELO_BOTELLA_VIDRIO import Botella_Vidrio
from MODELO_BASE_DATOS import Base_datos
objeto_botella_plastica= Botella_Plastica(1,1,1,1,1,1)
objeto_botella_vidrio= Botella_Vidrio(1,1,1,1,1,1)
Objeto_base_datos= Base_datos()

#================FUNCIONES=================
def colocar_botella_plastica():
    capacidad= input("Ingrese la capacidad de la botella plástica (en ml): ")
    tapa= input("Ingrese el tipo de tapa de la botella plástica: ")
    material= input("Ingrese el material de la botella plástica: ")
    resistencia= input("Ingrese la resistencia de la botella plástica: ")
    forma= input("Ingrese la forma de la botella plástica: ")
    diseño= input("Ingrese el diseño de la botella plástica: ")
    grabado= input("Ingrese el grabado de la botella plástica: ")
    transparencia= input("Ingrese la transparencia de la botella plástica: ")
    reciclable= input("Ingrese el contenedor adecuado para reciclar esta botella: ")
    cantidad= input("Ingrese la cantidad de botellas plásticas que caben en una caja: ")

    objeto_botella_plastica.adherir_propiedades(capacidad, tapa, material, resistencia, forma, diseño, grabado, transparencia, reciclable, cantidad)

def colocar_botella_vidrio():
    capacidad= input("Ingrese la capacidad de la botella de vidrio (en ml): ")
    tapa= input("Ingrese el tipo de tapa de la botella de vidrio: ")
    material= input("Ingrese el material de la botella de vidrio: ")
    resistencia= input("Ingrese la resistencia de la botella de vidrio: ")
    forma= input("Ingrese la forma de la botella de vidrio: ")
    diseño= input("Ingrese el diseño de la botella de vidrio: ")
    rompibilidad = input("Ingrese el color de la botella de vidrio: ")
    transparencia= input("Ingrese el grosor de la botella de vidrio: ")
    reciclable= input("Ingrese el contenedor adecuado para reciclar esta botella: ")
    cantidad= input("Ingrese la cantidad de botellas de vidrio que caben en una caja: ")

    objeto_botella_vidrio.adherir_propiedades(capacidad, tapa, material, resistencia, forma, diseño, rompibilidad, transparencia, reciclable, cantidad)

def menu_botellas():
    print("Agregue alguna de las Botellas:")
    print("1. Botella Plástica")
    print("2. Botella de Vidrio")
    eleccion_botella= input("Ingrese el número correspondiente a su elección: ")
    return eleccion_botella

def menu():
    dato=0
    while True:
        print("SELECCIONE UNA OPCION DE ACUEDO A LOS QUE QUIERE:")
        print("1.Agregar Botella")
        print("2.Mostar Botella")
        print("3.Eliminar Botella")
        print("4.Salir")
        eleccion= input("Ingrese el número correspondiente a su elección: ")

        match eleccion:
            case 1:
                eleccion_botella= menu_botellas()
                match eleccion_botella:
                    case "1":
                        colocar_botella_plastica()
                        Objeto_base_datos.agregar_botella(objeto_botella_plastica)
                        dato= dato+1
                    case "2":
                        colocar_botella_vidrio()
                        Objeto_base_datos.agregar_botella(objeto_botella_vidrio)
                        dato= dato+1
                    case _:
                        print("Opción inválida. Por favor, seleccione 1 o 2.")
            case 2:
                Objeto_base_datos.arrojar_info()
            case 3:
                print(f"Hay {dato} botellas registradas. ten en cuenta que se empiezan a contar desde el ID 0.")
                id_eliminar= int(input("Ingrese el ID de la botella que desea eliminar: "))
                Objeto_base_datos.eliminar_dato_lista(id_eliminar)
            case 4:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción inválida. Por favor, seleccione 1, 2 o 3.")

#===============PRINCIPAL=================
menu()

