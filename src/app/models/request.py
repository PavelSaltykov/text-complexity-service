from pydantic import BaseModel


class SentenceMeasuresRequest(BaseModel):
    id: str
    sentence: str
    language: str
