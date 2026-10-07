import os
import pandas as pd


def cargar_data():
    """Opción 1: Carga el archivo desde data/raw y retorna el DataFrame."""
    ruta_archivo = os.path.join("ventas", "raw", "ventas.csv")

    if not os.path.exists(ruta_archivo):
        print(f"\n[ERROR] No se encontró el archivo en: {ruta_archivo}")
        return None

    try:
        df = pd.read_csv(ruta_archivo)
        print(f"\n[ÉXITO] Archivo cargado correctamente desde {ruta_archivo}.")
        print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"\n[ERROR] Ocurrió un fallo al cargar el archivo: {e}")
        return None


def limpiar_data(df):
    """Opción 2: Realiza la limpieza del DataFrame ingresado."""
    if df is None:
        print("\n[ADVERTENCIA] No hay datos cargados para limpiar. Ejecuta primero la opción 1.")
        return None

    df_limpio = df.copy()

    # 1. Sanitizar cadenas: eliminar espacios (strip) y convertir a minúsculas
    columnas_texto = df_limpio.select_dtypes(include=["object", "string"]).columns
    for col in columnas_texto:
        df_limpio[col] = df_limpio[col].astype(str).str.strip().str.lower()

    # 2. Validar y eliminar duplicados
    duplicados = df_limpio.duplicated().sum()
    if duplicados > 0:
        df_limpio = df_limpio.drop_duplicates()
        print(f"- Se eliminaron {duplicados} filas duplicadas.")
    else:
        print("- No se encontraron filas duplicadas.")

    # 3. Validar y manejar datos nulos
    nulos = df_limpio.isnull().sum().sum()
    if nulos > 0:
        df_limpio = df_limpio.dropna()
        print(f"- Se eliminaron las filas con valores nulos ({nulos} nulos encontrados).")
    else:
        print("- No se encontraron valores nulos.")

    print(f"\n[ÉXITO] Limpieza completada. Filas resultantes: {df_limpio.shape[0]}")
    return df_limpio


def guardar_data(df):
    """Opción 3: Guarda el DataFrame limpio en el destino final."""
    if df is None:
        print("\n[ADVERTENCIA] No hay datos limpios para guardar. Ejecuta la opción 2 primero.")
        return

    ruta_salida = os.path.join("ventas", "processed")
    os.makedirs(ruta_salida, exist_ok=True)
    archivo_salida = os.path.join(ruta_salida, "datos_limpios.csv")

    try:
        df.to_csv(archivo_salida, index=False)
        print(f"\n[ÉXITO] Datos limpios guardados exitosamente en: {archivo_salida}")
    except Exception as e:
        print(f"\n[ERROR] No se pudo guardar el archivo: {e}")


def menu_principal():
    df_raw = None
    df_clean = None
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

        # SWITCH (match-case en Python)
        match opcion:
            case "1":
                df_raw = cargar_data()
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