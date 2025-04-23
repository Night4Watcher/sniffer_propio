import pyshark

def gestion_paquetes(captura_paquetes):
    contador_paquetes = 0
    for paquetes in captura_paquetes:
        contador_paquetes = contador_paquetes + 1
        print(f"Vamos a analizar el paquete {contador_paquetes}")
        contador_capas = 0
        for capas in paquetes:
            contador_capas = contador_capas + 1
            print(f"Esta es la capa {contador_capas}:")
            contador_ = 0
            for _ in capas:
                contador_ = contador_ + 1
                print(f"Este es el _ {contador_}:")
                print(_)

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