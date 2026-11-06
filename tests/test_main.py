"""
Reemplaza DataExtractor por una versión falsa con monkeypatch y verifica que el pipeline valide solo los primeros 5 posts.
- Con monkeypatch, simular fetch_posts y comprobar que run_pipeline() valida y devuelve solo los primeros 5 registros.
"""

import pytest
from pydantic import ValidationError

import main
from models import RawRecordModel


def test_run_pipeline_validates_first_five_posts(monkeypatch, capsys):
    sample_posts = [
        {
            "userId": 1,
            "id": i,
            "title": f"Title {i}",
            "body": f"Body {i}",
        }
        for i in range(1, 8)
    ]

    class FakeExtractor:
        def fetch_posts(self):
            return sample_posts

    monkeypatch.setattr(main, "DataExtractor", FakeExtractor)

    result = main.run_pipeline()

    assert len(result) == 5
    assert all(isinstance(record, RawRecordModel) for record in result)
    assert [record.id for record in result] == [1, 2, 3, 4, 5]

    captured = capsys.readouterr()
    assert "Fetched 7 posts" in captured.out
    assert "Validated posts" in captured.out


def test_run_pipeline_raises_on_invalid_post(monkeypatch, capsys):
    invalid_posts = [
        {
            "userId": 1,
            "id": 1,
            "body": "Missing title",
        }
    ]

    class FakeExtractor:
        def fetch_posts(self):
            return invalid_posts

    monkeypatch.setattr(main, "DataExtractor", FakeExtractor)

    with pytest.raises(ValidationError):
        main.run_pipeline()

    captured = capsys.readouterr()
    assert "An error occurred:" in captured.out
    assert "title" in captured.out