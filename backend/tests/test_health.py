from pathlib import Path

import pytest
from dotenv import dotenv_values
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

env_path = Path(__file__).resolve().parents[1] / ".env"
config = dotenv_values(env_path)


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_dashboard_overview():
    response = client.get("/api/dashboard/overview")
    assert response.status_code == 200
    assert "revenue" in response.json()
    assert "top_products" in response.json()


def test_supabase_keys_are_configured():
    url = (config.get("SUPABASE_URL") or "").strip()
    anon = (config.get("SUPABASE_ANON_KEY") or config.get("SUPABASE_PUBLISHABLE_KEY") or "").strip()
    service = (config.get("SUPABASE_SERVICE_ROLE_KEY") or config.get("SUPABASE_SECRET_KEY") or "").strip()

    if "your-" in url.lower() or "your-" in anon.lower() or "your-" in service.lower():
        pytest.skip("Supabase keys are still placeholder values. Replace them in backend/.env to test a real connection.")

    assert url.startswith("https://")
    assert len(anon) > 20
    assert len(service) > 20
