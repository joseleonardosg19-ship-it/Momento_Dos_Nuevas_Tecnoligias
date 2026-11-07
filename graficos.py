from io import BytesIO
import matplotlib
matplotlib.use("Agg")  # Servidor sin pantalla (obligatorio)
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import requests

# URL base de tu backend actual (ajusta los puertos o rutas si es necesario)
BASE_URL_SPRING = "https://educlic-momento1-jhon-1.onrender.com/api"


def _obtener_datos(recurso: str) -> pd.DataFrame:
    """Consume los endpoints existentes de tu backend."""
    try:
        response = requests.get(f"{BASE_URL_SPRING}/{recurso}")
        if response.status_code == 200:
            return pd.DataFrame(response.json())
    except Exception as e:
        print(f"[ERROR] Conectando con Spring Boot ({recurso}): {e}")
    return pd.DataFrame()

# ══════════════════════════════════════════════════════════
# MODELO HEADLESS → list[dict] usando tus DTOs actuales
# ══════════════════════════════════════════════════════════

def headless_productos_por_categoria() -> list[dict]:
    """Extrae el nombre de la categoría desde el objeto anidado 'categoria'."""
    df = _obtener_datos("productos")
    
    if df.empty or "categoria" not in df.columns:
        return []
    
    # Extraemos el campo 'nombre' del diccionario que viene dentro de 'categoria'
    nombres_categorias = []
    for cat in df["categoria"]:
        if isinstance(cat, dict):
            nombres_categorias.append(cat.get("nombre", "Sin Categoría"))
        else:
            nombres_categorias.append("Sin Categoría")
            
    df["categoriaNombre"] = nombres_categorias

    resumen = (
        df.groupby("categoriaNombre")
        .size()
        .reset_index(name="total_productos")
        .sort_values("total_productos", ascending=False)
        .head(10)
    )
    return resumen.to_dict(orient="records")

def headless_productos_mas_vendidos() -> list[dict]:
    """Aplica un parsing seguro de los pedidos y sus detalles anidados."""
    df_pedidos = _obtener_datos("pedidos")
    if df_pedidos.empty or "detalles" not in df_pedidos.columns:
        return []
    
    # Aplanamos la lista de detalles de manera segura
    detalles = []
    for lista in df_pedidos["detalles"]:
        if isinstance(lista, list):
            for det in lista:
                if isinstance(det, dict):
                    # Extraemos el nombre del producto de forma robusta 
                    # (puede venir como 'nombreProducto', o anidado dentro de 'producto')
                    nombre_prod = det.get("nombreProducto")
                    if not nombre_prod and isinstance(det.get("producto"), dict):
                        nombre_prod = det["producto"].get("nombre", "Desconocido")
                    elif not nombre_prod:
                        nombre_prod = "Desconocido"
                        
                    cantidad = det.get("cantidad", 0)
                    
                    detalles.append({
                        "nombreProducto": nombre_prod,
                        "cantidad": cantidad
                    })
            
    df_detalles = pd.DataFrame(detalles)
    if df_detalles.empty or "nombreProducto" not in df_detalles.columns:
        return []
        
    resumen = (
        df_detalles.groupby("nombreProducto")["cantidad"]
        .sum()
        .reset_index(name="total_vendido")
        .sort_values("total_vendido", ascending=False)
        .head(10)
    )
    return resumen.to_dict(orient="records")


def headless_clientes_frecuentes() -> list[dict]:
    """Calcula el Top 10 de clientes que más dinero han gastado en la tienda."""
    df_pedidos = _obtener_datos("pedidos")
    if df_pedidos.empty:
        return []
    
    # Extraemos el nombre del usuario de forma robusta
    nombres = []
    for _, row in df_pedidos.iterrows():
        nombre = "Anónimo"
        if "nombreUsuario" in df_pedidos.columns and pd.notna(row.get("nombreUsuario")):
            nombre = row["nombreUsuario"]
        elif "usuario" in df_pedidos.columns:
            u = row.get("usuario")
            if isinstance(u, dict):
                nombre = u.get("nombre", "Anónimo")
        nombres.append(nombre)
        
    df_pedidos["clienteNombre"] = nombres

    # Detectamos la columna del total de pago
    col_total = "total" if "total" in df_pedidos.columns else "totalPagar"
    if col_total not in df_pedidos.columns:
        return []
        
    df_pedidos[col_total] = pd.to_numeric(df_pedidos[col_total], errors="coerce").fillna(0)

    resumen = (
        df_pedidos.groupby("clienteNombre")[col_total]
        .sum()
        .reset_index(name="total_gastado")
        .sort_values("total_gastado", ascending=False)
        .head(10)
    )
    return resumen.to_dict(orient="records")

def headless_ventas_por_dia() -> list[dict]:
    """Agrupa las ventas totales por fecha para ver la tendencia diaria."""
    df_pedidos = _obtener_datos("pedidos")
    if df_pedidos.empty:
        return []
    
    # Detectamos la columna de fecha (suele llamarse 'fechaCreacion', 'fecha' o 'createdAt')
    col_fecha = None
    for posible in ["fechaCreacion", "fecha", "createdAt", "fechaPedido"]:
        if posible in df_pedidos.columns:
            col_fecha = posible
            break
            
    if not col_fecha:
        return []
        
    # Detectamos la columna del total
    col_total = "total" if "total" in df_pedidos.columns else "totalPagar"
    if col_total not in df_pedidos.columns:
        return []

    # Limpiamos y convertimos fechas a formato YYYY-MM-DD
    df_pedidos["fecha_solo"] = pd.to_datetime(df_pedidos[col_fecha], errors="coerce").dt.date
    df_pedidos[col_total] = pd.to_numeric(df_pedidos[col_total], errors="coerce").fillna(0)

    # Agrupamos sumando el dinero vendido por día
    resumen = (
        df_pedidos.dropna(subset=["fecha_solo"])
        .groupby("fecha_solo")[col_total]
        .sum()
        .reset_index(name="total_vendido")
        .sort_values("fecha_solo", ascending=True)
    )
    
    # Convertimos la fecha a string para que FastAPI la pueda serializar bien en JSON
    resumen["fecha_solo"] = resumen["fecha_solo"].astype(str)
    
    return resumen.to_dict(orient="records")


