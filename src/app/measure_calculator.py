import itertools
from typing import Tuple

from textcomplexity.utils import conllu
from textcomplexity.utils.text import Text

from src.app.measure import MeasureType, Measure


def calculate_for_sentence(conll_sentence: str, measure: Measure) -> Tuple[str, float]:
    conll_sentence = conll_sentence.split("\n")
    sentences, graphs = zip(*conllu.read_conllu_sentences(conll_sentence))
    if len(sentences) > 1:
        raise ValueError()
    sentence_tokens = list(itertools.chain.from_iterable(sentences))
    graph = graphs[0]

    match measure.type:
        case MeasureType.text:
            text = Text.from_tokens(sentence_tokens)
            return measure.name, measure.func(text)
        case MeasureType.graph:
            return measure.name, measure.func(graph)
        case _:
            raise TypeError()
