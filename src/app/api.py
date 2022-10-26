import itertools

from fastapi import FastAPI
from textcomplexity import sentence
from textcomplexity.utils import conllu

from src.app.conll_converter import ConllConverter
from src.app.models.request import SentenceMeasuresRequest
from src.app.models.response import SentenceMeasuresResponse, MeasureResult

app = FastAPI(title="text-complexity-service")


@app.get("/", include_in_schema=False)
async def openapi():
    return app.openapi()


@app.post("/sentences_measures", response_model=list[SentenceMeasuresResponse])
async def sentences_measures(body: list[SentenceMeasuresRequest]):
    languages = set(ConllConverter.supported_languages()).intersection(set([item.language for item in body]))
    converters = dict(zip(languages, map(ConllConverter, languages)))

    response = []
    for item in body:
        if item.language not in ConllConverter.supported_languages():
            response.append(SentenceMeasuresResponse(id=item.id, error="Unsupported language"))
            continue

        conllu_sentences = converters[item.language].text2conll_str(item.sentence).split("\n")
        sentences, graphs = zip(*conllu.read_conllu_sentences(conllu_sentences))
        tokens = list(itertools.chain.from_iterable(sentences))
        value = sentence._sentence_length_tokens(tokens)
        measure_result = MeasureResult(name="sentence length (tokens)", value=value)
        response.append(SentenceMeasuresResponse(id=item.id, measures=[measure_result]))
    return response
