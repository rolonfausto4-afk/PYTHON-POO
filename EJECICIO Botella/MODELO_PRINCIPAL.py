from MODELO_BOTELLA_PLASTICA import Botella_Plastica
from MODELO_BOTELLA_VIDRIO import Botella_Vidrio
from MODELO_BASE_DATOS import Base_datos

objeto_botella_plastica= Botella_Plastica(1,1,1,1,1,1)
objeto_botella_vidrio= Botella_Vidrio(1,1,1,1,1,1)
Objeto_base_datos= Base_datos()

objeto_dato_plastico= objeto_botella_plastica.adherir_propiedades(1000,"cierre hermetico","plastico","baja al calor","cilindrica","moderno","franjas azules","Clara","Amarillo","20")

objeto_dato_vidrio= objeto_botella_vidrio.adherir_propiedades(750,"cierre a presion","vidrio","alta al calor","cuerpo ancho con cuello estreño","clasico","frajil","turbia","amarillo",8)

Objeto_base_datos.agregar_botella(objeto_dato_vidrio)
Objeto_base_datos.agregar_botella(objeto_dato_plastico)

Objeto_base_datos.arrojar_info()


