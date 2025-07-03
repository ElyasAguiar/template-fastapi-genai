"""Tests for the /user creation endpoints."""

from fastapi.testclient import TestClient

from app.core.server import app


def test_create_user():
    """Test the POST /api/v1/user endpoint to create a user."""
    with TestClient(app) as client:
        payload = {
            "name": "John Doe",
            "logo": "https://example.com/logo.png",
            "email": "johndoe@example.com",
            "password": "P@ssw0rd!",
        }

        response = client.post("/api/v1/user", json=payload)

        assert response.status_code == 200 or response.status_code == 201
        data = response.json()

        # Top-level keys
        assert "status" in data
        assert data["status"] == "success"
        assert "message" in data
        assert data["message"] == "User created successfully"
        assert "error" in data
        assert data["error"] is None
        assert "data" in data

        # User data checks
        user_data = data["data"]
        assert "name" in user_data
        assert user_data["name"] == payload["name"]
        assert "email" in user_data
        assert user_data["email"] == payload["email"]
        assert "user_id" in user_data
        assert isinstance(user_data["user_id"], int)
