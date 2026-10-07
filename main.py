import os
import pandas as pd
import cargar

def menu_principal():
    clientes = None
    ventasn = None
    ejecutando = True

    while ejecutando:
        print("\n" + "=" * 40)
        print("      SISTEMA DE PROCESAMIENTO ETL      ")
        print("=" * 40)
        print("1. Cargar archivo (ventas/raw)")
        print("2. Limpiar DataFrame")
        print("3. Guardar / Entregar datos")
        print("4. Salir")

        opcion = input("\nSeleccione una opción (1-4): ").strip()

        match opcion:
            case "1":
                clientes,ventas = cargar.cargar_data()
            case "2":
                df_clean = limpiar_data(df_raw)
            case "3":
                guardar_data(df_clean)
            case "4":
                print("\nSaliendo del programa...")
                ejecutando = False
            case _:
                print("\n[ERROR] Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu_principal()