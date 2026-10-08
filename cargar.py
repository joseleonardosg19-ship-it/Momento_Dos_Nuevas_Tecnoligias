import os
import pandas as pd
# os trabaja con el archivo; pandas trabaja con los datos que están dentro del archivo.


def cargar_data():
    """Carga los archivos clientes.csv y ventas.csv desde data/raw."""

    ruta_clientes = os.path.join("data", "raw", "clientes.csv")
    ruta_ventas = os.path.join("data", "raw", "ventas.csv")

    try:
        # Verificar que existan los archivos
        if not os.path.exists(ruta_clientes):
            print(f"\n[ERROR] No se encontró: {ruta_clientes}")
            return None, None

        if not os.path.exists(ruta_ventas):
            print(f"\n[ERROR] No se encontró: {ruta_ventas}")
            return None, None

        # Cargar los dos archivos
        clientes = pd.read_csv(ruta_clientes)
        ventas = pd.read_csv(ruta_ventas)

        print("\n[ÉXITO] Archivos cargados correctamente.")
        print(f"Clientes: {clientes.shape[0]} filas | {clientes.shape[1]} columnas")
        print(f"Ventas:   {ventas.shape[0]} filas | {ventas.shape[1]} columnas")

        return clientes, ventas

    except Exception as e:
        print(f"\n[ERROR] Ocurrió un fallo al cargar los archivos: {e}")
        return None, None