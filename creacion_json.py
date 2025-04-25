import json

class archivo_json(object):
    
    existe_archivo = False
    nombre_archivo = "archivo_json.json"
    paquete = object
    
    def __init__(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                contenido_archivo = archivo.read()
                if contenido_archivo:
                    self.añadir_contenido()
        except FileNotFoundError:
            self.creacion_json()
    
    def creacion_json(self):
        try:
            with open(self.nombre_archivo, 'w') as archivo:
                json.dump(self.paquete, archivo, indent=4)
        except:
            print("Hubo un error a la hora de escribir en el archivo.")


    def añadir_contenido(self):
        with open(self.nombre_archivo, 'a') as archivo:
            json.dump(self.paquete, archivo, indent=4)

