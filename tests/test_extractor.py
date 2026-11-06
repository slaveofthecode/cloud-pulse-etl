"""
Simula la API con httpx.MockTransport, así no se hacen llamadas reales a internet.

- Respuesta 200 con una lista de posts: devuelve los datos correctamente.
- Respuesta 500: lanza httpx.HTTPStatusError.
- Error de red simulado: lanza httpx.RequestError.
"""

import pytest
import httpx
from extractor import DataExtractor


def test_fetch_posts_returns_data():
    def handler(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://jsonplaceholder.typicode.com/posts"
        return httpx.Response(
            200,
            json=[
                {
                    "userId": 1,
                    "id": 1,
                    "title": "A title",
                    "body": "A body",
                }
            ],
        )

    extractor = DataExtractor(transport=httpx.MockTransport(handler))

    result = extractor.fetch_posts()

    assert result == [
        {
            "userId": 1,
            "id": 1,
            "title": "A title",
            "body": "A body",
        }
    ]


def test_fetch_posts_raises_on_http_error():
    transport = httpx.MockTransport(
        lambda request: httpx.Response(500)
    )
    extractor = DataExtractor(transport=transport)

    with pytest.raises(httpx.HTTPStatusError):
        extractor.fetch_posts()


def test_fetch_posts_raises_on_network_error():
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("network down", request=request)

    extractor = DataExtractor(transport=httpx.MockTransport(handler))

    with pytest.raises(httpx.RequestError):
        extractor.fetch_posts()