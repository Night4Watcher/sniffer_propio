"""
Sniffer de red personalizado hecho tomando como base del proyecto el sniffer en el
siguiente repositorio de github -> https://github.com/Chispasgg/euneiz-redes1

Requisitos:
- Tener pyshark instalado
- 
"""

import pyshark

def almacenamiento_paquetes(paquetes):
    """
    Mediante esta funcion se busca lograr dividir la informacion del paquete capturado
    en diferentes secciones para luego poder procesar dichos paquetes.
    
    Keyword arguments:
    paquetes -- captura de los paquetes en transito en la interfaz de red seleccionada
    Return: return_description
    """
    
    # esto es el diccionario anidado donde almacenar toda la informacion del paquete capturado
    informacion_paquetes = {
        
    }
    # variables de contabilizacion
    paquetes_analizados = 0
    campo_informacion_general = 0
    # bucle con el que recorrer todos los paquetes que vayan siendo capturados
    for paquete in paquetes:
        paquetes_analizados += 1
        print(f'Paquete analizado num {paquetes_analizados}')
        
        # Obtencion de la informacion general del paquete
        info_general = paquete.frame_info
        for campo_informacion in info_general.field_names:
            campo_informacion_general += 1
            print(f'Campo de informacion num {campo_informacion_general}.')
            print(getattr(info_general, campo_informacion))
            # se introduce el valor obtenido en el diccionario anidado 'info_general'
            informacion_paquetes['info_general'] = getattr(info_general, campo_informacion)
            
        
        # obtencion de todas las capas que se encuentran disponibles en el paquete capturado
        capas_disponibles_paquete = paquete.layers
        # bucle con el que recorrer todas las capas disponibles en el paquete
        

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
    except PermissionError:
        print("Revisa los permisos concedidos.")
        exit(0)
    print("Vamos a almacenar la informacion de los paquetes.")
    almacenamiento_paquetes(paquetes_capturados)

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