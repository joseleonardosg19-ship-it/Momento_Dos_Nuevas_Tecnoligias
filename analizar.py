def analizar_data(clientes, ventas):
    """
    Analiza los DataFrames de clientes y ventas con las columnas reales.
    """

    if clientes is None or ventas is None:
        print("\n[ERROR] Primero debes cargar los datos.")
        return

    print("\n" + "=" * 55)
    print("                    ANÁLISIS DE DATOS")
    print("=" * 55)

    # ==================================================
    # ANÁLISIS DE CLIENTES
    # ==================================================
    print("\n" + "-" * 55)
    print("                    CLIENTES")
    print("-" * 55)

    print(f"Total de clientes: {len(clientes)}")

    if "ciudad" in clientes.columns:
        print("\nClientes por ciudad:")
        print(clientes["ciudad"].value_counts())

    if "segmento_cliente" in clientes.columns:
        print("\nClientes por segmento:")
        print(clientes["segmento_cliente"].value_counts())

    # ==================================================
    # ANÁLISIS DE VENTAS / OPERACIONES
    # ==================================================
    print("\n" + "-" * 55)
    print("                    VENTAS")
    print("-" * 55)

    print(f"Total de registros de ventas: {len(ventas)}")

    # Análisis del monto de préstamo
    if "monto_prestamo" in ventas.columns:
        print("\n--- Estadísticas de Monto de Préstamo ---")
        print(f"Total prestado: ${ventas['monto_prestamo'].sum():,.2f}")
        print(f"Promedio por préstamo: ${ventas['monto_prestamo'].mean():,.2f}")
        print(f"Préstamo máximo: ${ventas['monto_prestamo'].max():,.2f}")
        print(f"Préstamo mínimo: ${ventas['monto_prestamo'].min():,.2f}")

    # Análisis de precios
    if "precio" in ventas.columns:
        print("\n--- Estadísticas de Precios ---")
        print(f"Precio promedio: ${ventas['precio'].mean():,.2f}")
        print(f"Precio máximo: ${ventas['precio'].max():,.2f}")
        print(f"Precio mínimo: ${ventas['precio'].min():,.2f}")

    # Distribución por categorías
    if "categoria" in ventas.columns:
        print("\nDistribución por categoría de producto:")
        print(ventas["categoria"].value_counts())

    # Estado de los préstamos
    if "estado_prestamo" in ventas.columns:
        print("\nEstado de los préstamos:")
        print(ventas["estado_prestamo"].value_counts())

    # ==================================================
    # INFORMACIÓN GENERAL
    # ==================================================
    print("\n" + "-" * 55)
    print("               INFORMACIÓN GENERAL")
    print("-" * 55)

    print("\nColumnas de clientes:")
    print(list(clientes.columns))

    print("\nColumnas de ventas:")
    print(list(ventas.columns))

    print("\nAnálisis finalizado.")