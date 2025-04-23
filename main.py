import pyshark

def gestion_paquetes(captura_paquetes):
    variables_paquete = []
    contador_paquetes = 0
    for paquetes in captura_paquetes:
        contador_paquetes += 1
        print(f"\n Paquete {contador_paquetes}")
        
        for i, capa in enumerate(paquetes.layers, start=1):
            print(f"🔹 Capa {i}: {capa.layer_name}")
            
            for campo in capa.field_names:
                valor = getattr(capa, campo)
                print(f"          - {campo}: {valor}")


def obtencion_paquetes(tarjeta_red):
    try:
        captura_paquetes = pyshark.LiveCapture(
            interface=tarjeta_red
        )
    except PermissionError:
        print("Revisa los permisos o usa sudo")
        exit(0)
    print("Vamos a gestionar los paquetes.")
    gestion_paquetes(captura_paquetes)

def main():
    interfaz_red = input("¿Cual es tu interfaz de red?")
    obtencion_paquetes(interfaz_red)

if __name__ == "__main__":
    print("Ejecutando el sniffer...")
    main()