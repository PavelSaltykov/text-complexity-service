from pydantic import BaseModel


class SentenceMeasuresRequest(BaseModel):
    id: int
    sentence: str
    language: str
