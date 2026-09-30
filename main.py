<<<<<<< HEAD
import cargar
import limpiar

def menu_principal():

    clientes = None
    ventas = None
    df_merge = None
=======
<<<<<<< Updated upstream
print (hola)
=======
import cargar
import limpiar
import analizar
import merge

def menu_principal():
    clientes = None
    ventas = None
    df_merge = None
    datos_limpios = False  # <--- Bandera para controlar el flujo
>>>>>>> feature/Tania

    ejecutando = True

    while ejecutando:
<<<<<<< HEAD

=======
>>>>>>> feature/Tania
        print("\n===== MENÚ =====")
        print("1. Cargar datos")
        print("2. Limpiar datos")
        print("3. Validar y unir (merge)")
        print("4. Análisis del merge")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
<<<<<<< HEAD

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
=======
            case "1":
                clientes, ventas = cargar.cargar_data()
                datos_limpios = False  # Se cargaron datos nuevos, hay que limpiarlos de nuevo

            case "2":
                if clientes is None or ventas is None:
                    print("\n[ERROR] Primero debes cargar los datos (Opción 1).")
                else:
                    clientes, ventas = limpiar.limpiar_data(clientes, ventas)
                    datos_limpios = True  # <--- Indicamos que ya están limpios
                    print("\n[INFO] ¡Datos limpiados con éxito!")

            case "3":
                # Validamos que estén cargados Y limpios
                if clientes is None or ventas is None:
                    print("\n[ERROR] Primero debes cargar los datos.")
                elif not datos_limpios:
                    print("\n[ERROR] Debes limpiar los datos (Opción 2) antes de hacer el merge.")
                else:
                    df_merge = merge.validar_y_unir(clientes, ventas)

            case "4":
                merge.analizar_merge(df_merge)
>>>>>>> feature/Tania

            case "5":
                print("\nSaliendo del programa...")
                ejecutando = False

            case _:
                print("\n[ERROR] Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
<<<<<<< HEAD
=======
>>>>>>> Stashed changes
>>>>>>> feature/Tania
