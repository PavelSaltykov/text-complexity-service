import itertools
from enum import Enum
from typing import Tuple

from textcomplexity import sentence
from textcomplexity.utils import conllu


class MeasureType(Enum):
    token = 1
    graph = 2


class Measure(Enum):
    sentence_length_tokens = "sentence length (tokens)", MeasureType.token, sentence._sentence_length_tokens


def calculate_for_sentence(conll_sentence: str) -> list[Tuple[str, float]]:
    conll_sentence = conll_sentence.split("\n")
    sentences, graphs = zip(*conllu.read_conllu_sentences(conll_sentence))
    if len(sentences) > 1:
        raise ValueError()
    tokens = list(itertools.chain.from_iterable(sentences))

    results = []
    for m in Measure:
        m_name, m_type, m_func = m.value
        if m_type == MeasureType.token:
            results.append((m_name, m_func(tokens)))
        elif m_type == MeasureType.graph:
            results.append((m_name, m_func(graphs)))
        else:
            continue
    return results
