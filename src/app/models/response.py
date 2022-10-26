from typing import Optional

from pydantic import BaseModel


class MeasureResult(BaseModel):
    name: str
    value: float
    stdev: float
    error: Optional[str] = None


class SentenceMeasuresResponse(BaseModel):
    id: str
    measures: list[MeasureResult]
