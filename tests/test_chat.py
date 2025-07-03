"""Tests for the /chat streaming endpoint."""

from fastapi.testclient import TestClient

from app.core.server import app


# Use context manager to ensure lifespan is triggered (for app.state setup)
def test_stream_chat():
    """Test the /chat streaming endpoint."""
    with TestClient(app) as client:
        response = client.get("/api/v1/chat?sleep=0.01&number=3")

        assert response.status_code == 200
        assert response.headers["content-type"] == "application/json"

        chunks = []
        for chunk in response.iter_lines():
            if chunk:  # avoid empty lines
                chunks.append(chunk)

        # Filter out data lines (ignoring 'event:' or other metadata)
        data_lines = [line for line in chunks if line.startswith("data:")]

        # Expecting 3 streamed tokens and a [DONE] completion line
        assert len(data_lines) == 4
        assert data_lines[-1] == "data: [DONE]"

        # Optionally validate values
        for i in range(3):
            assert f"data: {i}" in data_lines
