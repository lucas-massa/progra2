import json 
import datetime
from Main import*
#defino a los datos como parte de datos_juego
def guardar_ranking(nombre, puntuacion, archivo="ranking.json"):
    datos = {
        "nombre": nombre,
        "Score": puntuacion,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(archivo, "w") as ranking_json:
        json.dump(datos, ranking_json, indent=4)