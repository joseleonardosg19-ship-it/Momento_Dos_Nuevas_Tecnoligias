import requests
import pandas as pd

# 1. URL del endpoint del API
url_api = "https://educlic-momento1-jhon-1.onrender.com/api/categorias"  # Cambia esto por la URL real de tu API

# 2. Realizar la petición GET para obtener los datos
response = requests.get(url_api)

# 3. Convertir la respuesta (que viene en formato JSON) a un diccionario de Python
datos_json = response.json()

# 4. Cargar los datos en un DataFrame
df_api = pd.DataFrame(datos_json)

df_api.info()