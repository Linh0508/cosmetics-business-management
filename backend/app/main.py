from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cosmetics Sales Management API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check() -> dict:
    return {
        "status": "ok",
        "service": "cosmetics-sales-api",
        "version": "0.1.0",
    }


@app.get("/api/dashboard/overview")
async def dashboard_overview() -> dict:
    return {
        "revenue": 125400000,
        "orders": 1284,
        "profit": 32500000,
        "new_customers": 324,
        "low_stock_products": 12,
        "expiring_products": 8,
        "top_products": [
            {"name": "Serum A", "sales": 523, "revenue": 52000000},
            {"name": "Kem B", "sales": 412, "revenue": 38000000},
            {"name": "Toner C", "sales": 321, "revenue": 25000000},
        ],
    }
