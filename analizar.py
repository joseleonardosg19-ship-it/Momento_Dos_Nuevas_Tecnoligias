def analizar_merge(df_merge):
    """
    Realiza el análisis del DataFrame resultante del merge.
    Responde las métricas solicitadas en el proyecto.
    """

    if df_merge is None:
        print("\n[ERROR] Primero debes realizar el merge.")
        return

    print("\n" + "=" * 60)
    print("                 ANÁLISIS DEL MERGE")
    print("=" * 60)

    # --------------------------------------------------
    # INFORMACIÓN GENERAL
    # --------------------------------------------------

    print("\n--- Información general ---")
    df_merge.info()

    # --------------------------------------------------
    # ESTADÍSTICAS NUMÉRICAS
    # --------------------------------------------------

    print("\n--- Estadísticas numéricas ---")
    print(df_merge.describe())

    # ==================================================
    # 1. ANÁLISIS DE FRECUENCIA
    # ==================================================

    print("\n" + "-" * 60)
    print("1. ANÁLISIS DE FRECUENCIA")
    print("-" * 60)

    frecuencia_categoria = df_merge["categoria"].value_counts()

    print("\nRegistros por categoría:")
    print(frecuencia_categoria)

    categoria_mas_frecuente = frecuencia_categoria.idxmax()
    cantidad = frecuencia_categoria.max()

    print(
        f"\nCategoría con mayor cantidad de registros: "
        f"{categoria_mas_frecuente}"
    )

    print(f"Cantidad de registros: {cantidad}")

    # ==================================================
    # 2. ANÁLISIS DE AGREGACIÓN
    # ==================================================

    print("\n" + "-" * 60)
    print("2. ANÁLISIS DE AGREGACIÓN")
    print("-" * 60)

    monto_por_categoria = (
        df_merge
        .groupby("categoria")["monto_prestamo"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nMonto total de préstamos por categoría:")
    print(monto_por_categoria)

    # ==================================================
    # 3. ANÁLISIS CON FILTRADO Y CONTEO
    # ==================================================

    print("\n" + "-" * 60)
    print("3. ANÁLISIS CON FILTRADO Y CONTEO")
    print("-" * 60)

    aprobados = df_merge[
        df_merge["estado_prestamo"]
        .str.strip()
        .str.upper() == "APROBADO"
    ]

    print(f"\nCantidad de préstamos aprobados: {len(aprobados)}")

    # ==================================================
    # INFORMACIÓN ADICIONAL
    # ==================================================

    print("\n" + "-" * 60)
    print("INFORMACIÓN ADICIONAL")
    print("-" * 60)

    print("\nPréstamos por estado:")
    print(
        df_merge["estado_prestamo"]
        .str.strip()
        .str.upper()
        .value_counts()
    )

    print("\nVentas por ciudad:")
    print(
        df_merge
        .groupby("ciudad")["precio"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nAnálisis finalizado.")