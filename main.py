"""
Sniffer de red personalizado hecho tomando como base del proyecto el sniffer en el
siguiente repositorio de github -> https://github.com/Chispasgg/euneiz-redes1

Requisitos:
- Tener pyshark instalado
- 
"""

from creacion_json import archivo_json
import identificacion_paquetes
import pyshark
import pyshark.capture
import pyshark.capture.live_capture
import pyshark.tshark
import pyshark.tshark.tshark

def almacenamiento_paquetes(paquetes):
    """
    Mediante esta funcion se busca lograr dividir la informacion del paquete capturado
    en diferentes secciones para luego poder procesar dichos paquetes.
    
    Keyword arguments:
    paquetes -- captura de los paquetes en transito en la interfaz de red seleccionada
    Return: return_description
    """
    
    # variables de contabilizacion
    paquetes_analizados = 0
    campo_informacion_general = 0
    # bucle con el que recorrer todos los paquetes que vayan siendo capturados
    for paquete in paquetes:
        # esto es el diccionario anidado donde almacenar toda la informacion del paquete capturado
        informacion_paquetes = {
            'informacion_general':{
                
            },
            'informacion_capa':{
                
            }
        }
        paquetes_analizados += 1
        print(f'Paquete analizado num {paquetes_analizados}')
        
        # Obtencion de la informacion general del paquete
        info_general = paquete.frame_info
        for campos in info_general.field_names:
            informacion_paquetes['informacion_general'][campos] = getattr(info_general, campos)
        
        for capa in paquete.layers:
            campos = {}
            for attr in dir(capa):
                if not attr.startswith('_') and not callable(getattr(capa, attr)):
                    try:
                        campos[attr] = getattr(capa, attr)
                    except:
                        pass
        informacion_paquetes['informacion_capa'][capa.layer_name] = campos
        
        archivo_json(informacion_paquetes)
    

def captura_paquetes():
    """
    Mediante esta funcion se realiza la captura de los distintos paquetes que transitan
    por la interfaz de red seleccionada. Para luego ser enviados para su almacenamiento
    y gestion.
    
    Keyword arguments:
    interfaz -- interfaz de red sobre la que trabajara el sniffer
    """
    
    interfaz = input("¿Cual es tu tarjeta de red?")
    try:
        paquetes_capturados = pyshark.LiveCapture(
            interface=interfaz
        )
        print("Vamos a almacenar la informacion de los paquetes.")
        almacenamiento_paquetes(paquetes_capturados)
    except PermissionError:
        print("Revisa los permisos concedidos.")
        exit(0)
    # error en caso de introducir incorrectamente una interfaz de red
    except pyshark.capture.live_capture.UnknownInterfaceException:
        print("La interfaz que has introducido, no es correcta")
        interfaces_disponibles = pyshark.tshark.tshark.get_all_tshark_interfaces_names()
        print("Estas son las interfaces que tienes disponibles: ")
        num_interfaz = 0
        for interfaces in interfaces_disponibles:
            num_interfaz += 1
            print(f'{num_interfaz}. {interfaces}')
        exit(0)

# Este va a ser el bloque o la funcion 'main' del programa
if __name__ == '__main__':
    print("")
    print("  _           _____   _____  _____  ")
    print(" | |         |  __ \ / ____|/ ____| ")
    print(" | |__  _   _| |__) | |  __| |  __  ")
    print(" | '_ \| | | |  ___/| | |_ | | |_ | ")
    print(" | |_) | |_| | |    | |__| | |__| | ")
    print(" |_.__/ \__, |_|     \_____|\_____| ")
    print("         __/ |                      ")
    print("        |___/                       ")
    print("")
    print("Sniffer arrancado.")
    captura_paquetes()          