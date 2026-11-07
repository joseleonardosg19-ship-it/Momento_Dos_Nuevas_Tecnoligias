from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from graficos import (
    headless_productos_por_categoria,
    headless_productos_mas_vendidos,
    headless_clientes_frecuentes,
    headless_ventas_por_dia
)

app = FastAPI(title="Motor Analítico - Tienda Creativa")

# 2. Configura los dominios permitidos (puedes poner tu URL de Vercel o "*" para permitir todos)
origins = [
    "https://proyecto-integrador-chi-orcin.vercel.app",
    "https://educlic-momento1-jhon-1.onrender.com/api",
    "http://localhost:5173",  # Por si necesitas probar tu React localmente
]

# 3. Agrega el middleware a la aplicación
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Usar ["*"] permite peticiones desde cualquier lugar, ideal para proyectos integradores
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

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

