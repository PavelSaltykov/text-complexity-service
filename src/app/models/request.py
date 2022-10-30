from enum import Enum

from pydantic import BaseModel


class Language(str, Enum):
    ru = "ru"


class SentenceMeasuresRequest(BaseModel):
    id: int
    sentence: str
    language: Language
