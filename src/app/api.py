from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.app import measure_calculator
from src.app.conll_converter import ConllConverter
from src.app.measure_calculator import SentenceMeasure
from src.app.models.request import SentenceMeasuresRequest
from src.app.models.response import SentenceMeasuresResponse, MeasureResult

app = FastAPI(title="text-complexity-service", default_response_class=ORJSONResponse)

conll_converters = ConllConverter.all_language_converters()


@app.get("/", include_in_schema=False)
async def openapi():
    return app.openapi()


@app.post("/sentences_measures", response_model=list[SentenceMeasuresResponse])
async def sentences_measures(body: list[SentenceMeasuresRequest]):
    response = []
    for item in body:
        if item.language not in ConllConverter.supported_languages():
            response.append(SentenceMeasuresResponse(id=item.id, error="Unsupported language"))
            continue

        conll_sentences = conll_converters[item.language].text2conll_str(item.sentence).split("\n\n")
        conll_sentences = list(filter(None, conll_sentences))
        if len(conll_sentences) != 1:
            response.append(SentenceMeasuresResponse(id=item.id, error="Required one sentence"))
            continue

        conll_sentence = conll_sentences[0]
        calculated_measures = [measure_calculator.calculate_for_sentence(conll_sentence, m) for m in SentenceMeasure]
        calculated_measures = [MeasureResult(name=res[0], value=res[1])
                               for res in calculated_measures if res is not None]
        response.append(SentenceMeasuresResponse(id=item.id, measures=calculated_measures))
    return response
