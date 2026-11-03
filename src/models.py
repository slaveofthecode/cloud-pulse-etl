from pydantic import BaseModel, Field

class RawRecordModel(BaseModel):
    userId: int = Field(..., description="The user ID")
    id: int = Field(..., description="The record ID")
    title: str = Field(..., description="The record title")
    body: str = Field(..., description="The record body")
