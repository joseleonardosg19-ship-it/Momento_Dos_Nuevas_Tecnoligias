import pandas as pd

def validar_y_unir(clientes, ventas):
    """
    Valida los DataFrames de clientes y ventas, y realiza la unión (merge).
    """
    print("\n--- Validando y uniendo datos ---")
    
    # Validación básica de que los datos no estén vacíos
    if clientes is None or ventas is None:
        print("Error: Los datos de clientes o ventas no están cargados.")
        return None

    print(f"Clientes totales: {len(clientes)}")
    print(f"Ventas totales: {len(ventas)}")

    try:
        # Se usa left_on y right_on porque las columnas se llaman diferente en cada tabla
        df_merge = pd.merge(
            ventas, 
            clientes, 
            left_on="id_usuario", 
            right_on="id_cliente", 
            how="inner"
        )
        print("¡Merge realizado con éxito!")
        return df_merge
    except Exception as e:
        print(f"Error al realizar el merge: {e}")
        return None

def analizar_merge(df_merge):
    """
    Realiza un análisis básico del DataFrame resultante del merge.
    """
    print("\n--- Análisis del Merge ---")
    
    if df_merge is None or df_merge.empty:
        print("No hay datos unidos para analizar. Ejecuta la opción de unión primero.")
        return

    # Mostrar información general
    print(f"Total de registros unidos: {len(df_merge)}")
    print("\nPrimeras filas del resultado:")
    print(df_merge.head())

    print("\nInformación estadística básica:")
    print(df_merge.describe())