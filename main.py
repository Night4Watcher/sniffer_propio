import pyshark

def gestion_paquetes(captura_paquetes):
    for paquetes in captura_paquetes:
        for capas in paquetes:
            contador_capas = 0
            contador_capas =+ 1
            print(f"Esta es la capa {contador_capas}:")
            print(capas)

def obtencion_paquetes(tarjeta_red):
    try:
        captura_paquetes = pyshark.LiveCapture(
            interface=tarjeta_red
        )
        captura_paquetes.sniff(packet_count=1)
    except PermissionError:
        print("Revisa los permisos o usa sudo")
        exit(0)
    print("Vamos a gestionar los paqutes.")
    gestion_paquetes(captura_paquetes)

def main():
    interfaz_red = input("¿Cual es tu interfaz de red?")
    obtencion_paquetes(interfaz_red)

if __name__ == "__main__":
    print("Ejecutando el sniffer...")
    main()