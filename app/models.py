from pydantic import BaseModel, Field

class SectorRequest(BaseModel):
    sector: str = Field(..., min_length=3, max_length=50)