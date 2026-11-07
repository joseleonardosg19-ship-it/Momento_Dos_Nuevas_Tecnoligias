from fastapi import FastAPI
from fastapi.responses import Response
from graficos import (
    headless_productos_por_categoria,
    headless_productos_mas_vendidos,
    headless_clientes_frecuentes,
    headless_ventas_por_dia
)

app = FastAPI(title="Motor Analítico - Tienda Creativa")

# ════════════════════════════════════════════════════════
# ENDPOINTS HEADLESS → JSON (Para consumir desde el Front)
# ════════════════════════════════════════════════════════

@app.get("/api/graficos/headless/productos-por-categoria")
def ep_headless_productos_categoria():
    return headless_productos_por_categoria()

@app.get("/api/graficos/headless/productos-mas-vendidos")
def ep_headless_productos_vendidos():
    return headless_productos_mas_vendidos()

@app.get("/api/graficos/headless/clientes-frecuentes")
def ep_headless_clientes_frecuentes():
    return headless_clientes_frecuentes()

@app.get("/api/graficos/headless/ventas-por-dia")
def ep_headless_ventas_por_dia():
    return headless_ventas_por_dia()

