import pyshark

def gestion_paquetes():
    pass

def obtencion_paquetes(tarjeta_red):
    try:
        captura_paquetes = pyshark.LiveCapture(
            interface=tarjeta_red
        )
        captura_paquetes.sniff(packet_count=1)
        for paquete in captura_paquetes:
            print(paquete)
    except PermissionError:
        print("Revisa los permisos o usa sudo")

def main():
    interfaz_red = input("¿Cual es tu interfaz de red?")
    obtencion_paquetes(interfaz_red)

if __name__ == "__main__":
    print("Ejecutando el sniffer...")
    main()