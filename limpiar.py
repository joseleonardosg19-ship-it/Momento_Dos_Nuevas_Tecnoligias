import pandas as pd


def limpiar_data(clientes, ventas):

    if clientes is None or ventas is None:
        print("\n[ERROR] Primero debes cargar los datos.")
        return None, None

    clientes_limpio = clientes.copy()
    ventas_limpio = ventas.copy()

    print("\n" + "=" * 50)
    print("              LIMPIEZA DE DATOS")
    print("=" * 50)

    # LIMPIAR CLIENTES
    columnas_clientes = clientes_limpio.select_dtypes(
        include=["object", "string"]
    ).columns

    for columna in columnas_clientes:
        clientes_limpio[columna] = (
            clientes_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    nulos_clientes = clientes_limpio.isnull().sum().sum()

    if nulos_clientes > 0:
        print(f"\n[CLIENTES] Se encontraron {nulos_clientes} valores nulos.")
        clientes_limpio = clientes_limpio.dropna()
        print("[CLIENTES] Valores nulos eliminados.")
    else:
        print("\n[CLIENTES] No se encontraron valores nulos.")

    duplicados_clientes = clientes_limpio.duplicated().sum()

    if duplicados_clientes > 0:
        print(f"[CLIENTES] Se encontraron {duplicados_clientes} registros duplicados.")
        clientes_limpio = clientes_limpio.drop_duplicates()
        print("[CLIENTES] Registros duplicados eliminados.")
    else:
        print("[CLIENTES] No se encontraron duplicados.")

    # LIMPIAR VENTAS
    columnas_ventas = ventas_limpio.select_dtypes(
        include=["object", "string"]
    ).columns

    for columna in columnas_ventas:
        ventas_limpio[columna] = (
            ventas_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    nulos_ventas = ventas_limpio.isnull().sum().sum()

    if nulos_ventas > 0:
        print(f"\n[VENTAS] Se encontraron {nulos_ventas} valores nulos.")
        ventas_limpio = ventas_limpio.dropna()
        print("[VENTAS] Valores nulos eliminados.")
    else:
        print("\n[VENTAS] No se encontraron valores nulos.")

    duplicados_ventas = ventas_limpio.duplicated().sum()

    if duplicados_ventas > 0:
        print(f"[VENTAS] Se encontraron {duplicados_ventas} registros duplicados.")
        ventas_limpio = ventas_limpio.drop_duplicates()
        print("[VENTAS] Registros duplicados eliminados.")
    else:
        print("[VENTAS] No se encontraron duplicados.")

    print("\n" + "-" * 50)
    print("LIMPIEZA FINALIZADA")
    print("-" * 50)

    print(
        f"Clientes antes: {len(clientes)} | "
        f"Clientes después: {len(clientes_limpio)}"
    )

    print(
        f"Ventas antes: {len(ventas)} | "
        f"Ventas después: {len(ventas_limpio)}"
    )

    return clientes_limpio, ventas_limpio