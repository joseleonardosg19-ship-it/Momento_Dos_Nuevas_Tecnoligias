#  Sistema de Procesamiento y Análisis de Datos

Sistema modular desarrollado en **Python** diseñado para la carga, limpieza, validación, fusión (*merge*) y análisis de datos relacionales (clientes y ventas) a través de un menú interactivo en consola.

---

##  Estructura del Proyecto

El proyecto está organizado en módulos independientes para mantener un código limpio y escalable:

* **`main.py`**: Archivo principal que ejecuta la aplicación, gestiona el menú interactivo mediante `match-case` y controla el flujo secuencial de los procesos.
* **`cargar.py`**: Módulo encargado de la lectura y carga inicial de los archivos de datos (`clientes` y `ventas`).
* **`limpiar.py`**: Módulo responsable de procesar, depurar y normalizar los dataframes.
* **`merge.py`**: Realiza la validación de integridad, la unión de las tablas (`clientes` usando `id_cliente` y `ventas` usando `id_usuario`) y análisis avanzados sobre los datos unidos.
* **`analizar.py`**: Contiene funciones orientadas al análisis estadístico e individual de los datasets.

---

##  Flujo de Trabajo (Cascada Obligatoria)

Para garantizar la integridad de los datos, el sistema implementa una **cascada lógica de control**:
1. **Cargar datos (Opción 1):** Es el punto de partida obligatorio. Si no se cargan los archivos, los siguientes pasos no permitirán avanzar.
2. **Limpiar datos (Opción 2):** Permite procesar los datos crudos cargados previamente.
3. **Validar y Unir / Merge (Opción 3):** Valida que los datos estén listos y ejecuta la combinación relacional entre clientes y ventas.
4. **Análisis del Merge (Opción 4):** Muestra métricas e información detallada del resultado de la unión.
5. **Salir (Opción 5):** Finaliza la ejecución del programa de forma limpia.

---

##  Requisitos e Instalación

Asegúrate de tener instalado Python y las dependencias necesarias (como `pandas`).

1. Clona el repositorio y cambia a la rama de desarrollo (`dev`):
   
```git checkout dev```

2. Activa tu entorno virtual (venv):

```source venv/Scripts/activate```

3. Instala las dependencias necesarias: 

```pip install -r requirements.txt```

Ejecuta el script principal desde la terminal con el entorno virtual activo: python main.py

