"""
- Un JSON válido se convierte en RawRecordModel.
- Si falta title, lanza ValidationError.
- Si un campo obligatorio no tiene el tipo esperado, lanza ValidationError.
"""

import pytest 
from pydantic import ValidationError
from models import RawRecordModel

def test_raw_record_model_valid():
    record = RawRecordModel(
        userId=1,
        id=1,
        title="Test title",
        body="Test body",
    )
    assert record.userId == 1
    assert record.id == 1
    assert record.title == "Test title"
    assert record.body == "Test body"

def test_raw_record_missing_title_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        RawRecordModel(
            userId=1,
            id=1,
            body="Test body",
        )
    assert "title" in str(exc_info.value)

def test_raw_record_invalid_type_raises_validation_error():
    with pytest.raises(ValidationError) as exc_info:
        RawRecordModel(
            userId="nor-an-int",
            id=1,
            title="Test title",
            body="Test body",
        )
