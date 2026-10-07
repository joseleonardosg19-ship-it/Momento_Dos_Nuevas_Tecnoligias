import cargar

def menu_principal():

    clientes = None
    ventas = None
    df_merge = None

    ejecutando = True

    while ejecutando:

        print("\n===== MENÚ =====")
        print("1. Cargar datos")
        print("2. Limpiar datos")
        print("3. Validar y unir (merge)")
        print("4. Análisis del merge")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:

            case "1":
                clientes, ventas = cargar.cargar_data()

            case "2":
                clientes, ventas = limpiar.limpiar_data(
                    clientes,
                    ventas
                )

            case "3":
                print("\n[INFO] Aquí se realizará la validación y el merge.")
                # Aquí irá la función para validar y unir
                # df_merge = preparar.validar_y_unir(clientes, ventas)

            case "4":
                analizar.analizar_data(df_merge)

            case "5":
                print("\nSaliendo del programa...")
                ejecutando = False

            case _:
                print("\n[ERROR] Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
