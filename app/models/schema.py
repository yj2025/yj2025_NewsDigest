from pydantic import BaseModel

class SummaryRequest(BaseModel):
    url: str

class SummaryResponse(BaseModel):
    summary: str