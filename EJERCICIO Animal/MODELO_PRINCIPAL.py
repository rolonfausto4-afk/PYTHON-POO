from MODELO_MAMIFERO import Mamifero
from MODELO_PEZ import Pez
from MODELO_AVE import Ave
from MODELO_REPTIL import Reptil
from MODELO_INSECTO import Insecto
from MODELO_BASE_DATOS import Base_Datos
obj_bd= Base_Datos()

#========FUNCIONES PRINCIPALES========
def colocar_mamifero():
    nombre= input("Ingrese el nombre del mamífero: ")
    edad= int(input("Ingrese la edad del mamífero: "))
    habitat= input("Ingrese el hábitat del mamífero: ")
    dieta= input("Ingrese la dieta del mamífero: ")
    tamano= input("Ingrese el tamaño del mamífero: ")
    color= input("Ingrese el color del mamífero: ")
    pelo= "Pelaje"
    movimiento= input("Ingrese el tipo de movimiento del mamífero: ")
    reproducion= input("Ingrese el tipo de reproducción del mamífero: ")
    comportamiento= input("Ingrese el comportamiento del mamífero: ")
    descanso= input("Ingrese el tipo de descanso del mamífero: ")
    objeto_mamifero= Mamifero(nombre, edad, habitat, dieta, tamano, color, pelo)
    dato_mostar= objeto_mamifero.Mostrar_info(movimiento, reproducion, comportamiento, descanso)
    return dato_mostar

def colocar_pez():
    nombre= input("Ingrese el nombre del pez: ")
    edad= int(input("Ingrese la edad del pez: "))
    habitat= input("Ingrese el hábitat del pez: ")
    dieta= input("Ingrese la dieta del pez: ")
    tamano= input("Ingrese el tamaño del pez: ")
    color= input("Ingrese el color del pez: ")
    escamas= "Escamas"
    movimiento= input("Ingrese el tipo de movimiento del pez: ")
    reproducion= input("Ingrese el tipo de reproducción del pez: ")
    comportamiento= input("Ingrese el comportamiento del pez: ")
    descanso= input("Ingrese el tipo de descanso del pez: ")
    objeto_pez= Pez(nombre, edad, habitat, dieta, tamano, color, escamas)
    dato_mostar= objeto_pez.Mostrar_info(movimiento, reproducion, comportamiento, descanso)
    return dato_mostar

def colocar_ave():
    nombre= input("Ingrese el nombre del ave: ")
    edad= int(input("Ingrese la edad del ave: "))
    habitat= input("Ingrese el hábitat del ave: ")
    dieta= input("Ingrese la dieta del ave: ")
    tamano= input("Ingrese el tamaño del ave: ")
    color= input("Ingrese el color del ave: ")
    plumas= "Plumas"
    movimiento= input("Ingrese el tipo de movimiento del ave: ")
    reproducion= input("Ingrese el tipo de reproducción del ave: ")
    comportamiento= input("Ingrese el comportamiento del ave: ")
    descanso= input("Ingrese el tipo de descanso del ave: ")
    objeto_ave= Ave(nombre, edad, habitat, dieta, tamano, color, plumas)
    dato_mostar= objeto_ave.Mostrar_info(movimiento, reproducion, comportamiento, descanso)
    return dato_mostar

def colocar_reptil():
    nombre= input("Ingrese el nombre del reptil: ")
    edad= int(input("Ingrese la edad del reptil: "))
    habitat= input("Ingrese el hábitat del reptil: ")
    dieta= input("Ingrese la dieta del reptil: ")
    tamano= input("Ingrese el tamaño del reptil: ")
    color= input("Ingrese el color del reptil: ")
    escamas= "Escamas"
    movimiento= input("Ingrese el tipo de movimiento del reptil: ")
    reproducion= input("Ingrese el tipo de reproducción del reptil: ")
    comportamiento= input("Ingrese el comportamiento del reptil: ")
    descanso= input("Ingrese el tipo de descanso del reptil: ")
    objeto_reptil= Reptil(nombre, edad, habitat, dieta, tamano, color, escamas)
    dato_mostar= objeto_reptil.Mostrar_info(movimiento, reproducion, comportamiento, descanso)
    return dato_mostar  

def colocar_insecto():
    nombre= input("Ingrese el nombre del insecto: ")
    edad= int(input("Ingrese la edad del insecto: "))
    habitat= input("Ingrese el hábitat del insecto: ")
    dieta= input("Ingrese la dieta del insecto: ")
    tamano= input("Ingrese el tamaño del insecto: ")
    color= input("Ingrese el color del insecto: ")
    exoesqueleto= "Exoesqueleto"
    movimiento= input("Ingrese el tipo de movimiento del insecto: ")
    reproducion= input("Ingrese el tipo de reproducción del insecto: ")
    comportamiento= input("Ingrese el comportamiento del insecto: ")
    descanso= input("Ingrese el tipo de descanso del insecto: ")
    objeto_insecto= Insecto(nombre, edad, habitat, dieta, tamano, color, exoesqueleto)
    dato_mostar= objeto_insecto.Mostrar_info(movimiento, reproducion, comportamiento, descanso)
    return dato_mostar

def agregar_animal():
    print("Seleccione el tipo de animal que desea agregar:")
    print("1. Mamífero")
    print("2. Pez")
    print("3. Ave")
    print("4. Reptil")
    print("5. Insecto")
    opcion_animal= int(input("Ingrese el número correspondiente a su opción: "))

    return opcion_animal

def menu():
    dato=0
    while True:
        print("=== MENÚ DE ANIMALES ===")
        print("1. Agregar un animal")
        print("2. Mostrar todos los animales")
        print("3.Eliminar un animal")
        print("4. Salir")
        eleccion= int(input("Ingrese el número correspondiente a su elección: "))
        
        match eleccion:
            case 1:
                tipo_animal= agregar_animal()
                match tipo_animal:
                    case 1:
                        dato_mamifero= colocar_mamifero()
                        obj_bd.extender_lista([dato_mamifero])
                        dato= dato+1
                    case 2:
                        dato_pez= colocar_pez()
                        obj_bd.extender_lista([dato_pez])
                        dato= dato+1
                    case 3:
                        dato_ave= colocar_ave() 
                        obj_bd.extender_lista([dato_ave])
                        dato= dato+1
                    case 4:
                        dato_reptil= colocar_reptil()
                        obj_bd.extender_lista([dato_reptil])
                        dato= dato+1
                    case 5:
                        dato_insecto= colocar_insecto()
                        obj_bd.extender_lista([dato_insecto])
                        dato= dato+1
                    case _:
                        print("Opción inválida. Por favor, intente de nuevo.")
            case 2:
                obj_bd.mostrar_animales()
            case 3:
                print(f"Hay {dato} en la lista. \n Tenga en cuenta que los ID empiezan a contar desde el 0.")
                id_eliminar= int(input("Ingrese el ID del animal que desea eliminar: "))
                obj_bd.eliminar_animal(id_eliminar)
            case 4:
                print("Saliendo del menú. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Por favor, intente de nuevo.")
        
                    
#------------principal----------------
menu()