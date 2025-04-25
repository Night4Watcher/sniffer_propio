import json
import pyshark

def añadir_contenido(informacion_paquete):
    """Añadir contenido al archivo JSON. Si el archivo no existe, se crea."""
    try:
        # Leer el archivo JSON actual, si existe
        try:
            with open('archivo_json.json', 'r') as archivo:
                contenido_archivo = json.load(archivo)  # Usamos json.load() para leer el archivo JSON
        except FileNotFoundError:
            contenido_archivo = []  # Si no existe el archivo, iniciamos una lista vacía

        # Añadir el nuevo paquete a la lista de contenido
        contenido_archivo.append(informacion_paquete)

        # Guardar el contenido actualizado en el archivo JSON
        with open('archivo_json.json', 'w') as archivo:
            json.dump(contenido_archivo, archivo, indent=4)
    except Exception as e:
        print(f"Error al agregar contenido al archivo JSON: {e}")

def almacenamiento_paquetes(paquetes):
    """
    Procesar los paquetes capturados y extraer la información relevante para almacenarla.

    Keyword arguments:
    paquetes -- Captura de los paquetes en tránsito en la interfaz de red seleccionada.
    """
    paquetes_analizados = 0

    for paquete in paquetes:
        paquetes_analizados += 1
        print(f'Paquete analizado num {paquetes_analizados}')

        # Estructura para almacenar la información del paquete
        informacion_paquetes = {
            'informacion_general': {},
            'informacion_capa': {}
        }

        # Obtener información general del paquete
        info_general = paquete.frame_info
        for campo in info_general.field_names:
            informacion_paquetes['informacion_general'][campo] = getattr(info_general, campo, 'No disponible')

        # Procesar capas del paquete
        for capa in paquete.layers:
            campos = {}
            for attr in dir(capa):
                if not attr.startswith('_') and not callable(getattr(capa, attr)):
                    try:
                        campos[attr] = getattr(capa, attr)
                    except Exception as e:
                        print(f"Error al obtener atributo {attr} de la capa: {e}")
            informacion_paquetes['informacion_capa'][capa.layer_name] = campos

        # Almacenar la información del paquete en el archivo JSON
        añadir_contenido(informacion_paquetes)

def captura_paquetes():
    """
    Captura paquetes en tiempo real en la interfaz de red seleccionada.

    Keyword arguments:
    interfaz -- interfaz de red sobre la que trabajará el sniffer.
    """
    interfaz = input("¿Cual es tu tarjeta de red? ")
    try:
        # Iniciar la captura de paquetes en la interfaz seleccionada
        paquetes_capturados = pyshark.LiveCapture(interface=interfaz)
        print("Capturando y almacenando paquetes...")

        # Procesar los paquetes capturados
        almacenamiento_paquetes(paquetes_capturados)

    except PermissionError:
        print("Revisa los permisos concedidos. Asegúrate de tener privilegios de administrador.")
        exit(0)
    except pyshark.capture.live_capture.UnknownInterfaceException:
        print("La interfaz proporcionada no es válida.")
        interfaces_disponibles = pyshark.tshark.tshark.get_all_tshark_interfaces_names()
        print("Estas son las interfaces disponibles:")
        for num_interfaz, interfaz in enumerate(interfaces_disponibles, start=1):
            print(f'{num_interfaz}. {interfaz}')
        exit(0)

# Función principal (main)
if __name__ == '__main__':
    print("\nSniffer de red arrancado. Capturando paquetes...\n")
    captura_paquetes()
