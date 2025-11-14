from MODELO_MAMIFERO import Mamifero
from MODELO_PEZ import Pez
from MODELO_AVE import Ave
from MODELO_REPTIL import Reptil
from MODELO_INSECTO import Insecto
from MODELO_BASE_DATOS import Base_Datos

obj_bd= Base_Datos()
obj_mamifero= Mamifero("Mamiferos", 5, "Domestico", "Omnívora", "Mediano", "Marrón", "Pelaje")
obj_pez= Pez("Peces", 2, "Acuático", "Omnívora", "Pequeño", "Plateado", "Escamas")
obj_ave= Ave("Aves", 3, "Aéreo", "Herbívora", "Pequeño", "Multicolor", "Plumas")
obj_reptil= Reptil("Reptiles", 4, "Terrestre", "Carnívora", "Grande", "Verde", "Escamas")
obj_insecto= Insecto("Insectos", 1, "Variado", "Hebívora", "Muy pequeño", "Negro", "Exoesqueleto")

obj_mostrar_mamifero = obj_mamifero.Mostrar_info("Corriendo/Caminando", "Vivíparo", "Nomada", "No Rem")
obj_mostrar_pez = obj_pez.Mostrar_info("Nadando", "Ovíparo", "Dependeniente", "Rem")
obj_mostrar_ave = obj_ave.Mostrar_info("Volando", "Ovíparo", "Migratoria", "Rem")
obj_mostrar_reptil = obj_reptil.Mostrar_info("Corriendo/Caminando o Reptando", "Ovíparo", "Termorregulatoria", "No rem")
obj_mostrar_insecto = obj_insecto.Mostrar_info("poseen todo tipo de movimiento", "Ovíparo", "Dependiente", "Rem")

obj_bd.extender_lista([obj_mostrar_mamifero, obj_mostrar_pez, obj_mostrar_ave, obj_mostrar_reptil, obj_mostrar_insecto])
obj_bd.mostrar_animales()