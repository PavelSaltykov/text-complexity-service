import itertools
from enum import Enum
from typing import Tuple

from textcomplexity import surface, dependency
from textcomplexity.utils import conllu
from textcomplexity.utils.text import Text


class MeasureType(Enum):
    text = 1
    graph = 2


class SentenceMeasure(Enum):
    text_length_tokens = "text length (tokens)", MeasureType.text, surface.text_length_tokens
    text_length_characters = "text length (characters)", MeasureType.text, surface.text_length_characters
    type_token_ratio = "type-token ratio", MeasureType.text, surface.type_token_ratio
    guiraud_r = "Guiraud's R", MeasureType.text, surface.guiraud_r
    herdan_c = "Herdan's C", MeasureType.text, surface.herdan_c
    dugast_k = "Dugast's k", MeasureType.text, surface.dugast_k
    maas_a2 = "Maas' a²", MeasureType.text, surface.maas_a2
    dugast_u = "Dugast's U", MeasureType.text, surface.dugast_u
    tuldava_ln = "Tuldava's LN", MeasureType.text, surface.tuldava_ln
    brunet_w = "Brunet's W", MeasureType.text, surface.brunet_w
    cttr = "CTTR", MeasureType.text, surface.cttr
    summer_s = "Summer's S", MeasureType.text, surface.summer_s
    sichel_s = "Sichel's S", MeasureType.text, surface.sichel_s
    michea_m = "Michéa's M", MeasureType.text, surface.michea_m
    honore_h = "Honoré's H", MeasureType.text, surface.honore_h
    entropy = "entropy", MeasureType.text, surface.entropy
    evenness = "evenness", MeasureType.text, surface.evenness
    jarvis_evenness = "Jarvis's evenness", MeasureType.text, surface.jarvis_evenness
    yule_k = "Yule's K", MeasureType.text, surface.yule_k
    simpson_d = "Simpson's D", MeasureType.text, surface.simpson_d
    herdan_vm = "Herdan's Vm", MeasureType.text, surface.herdan_vm
    hdd = "HD-D", MeasureType.text, surface.hdd
    average_token_length = "average token length", MeasureType.text, surface.average_token_length
    orlov_z = "Orlov's Z", MeasureType.text, surface.orlov_z
    mtld = "MTLD", MeasureType.text, surface.mtld

    average_dependency_distance = ("average dependency distance", MeasureType.graph,
                                   dependency._average_dependency_distance)
    closeness_centrality = "closeness centrality", MeasureType.graph, dependency._closeness_centrality
    outdegree_centralization = "outdegree centralization", MeasureType.graph, dependency._outdegree_centralization
    closeness_centralization = "closeness centralization", MeasureType.graph, dependency._closeness_centralization
    longest_shortest_path = "longest shortest path", MeasureType.graph, dependency._longest_shortest_path
    dependents_per_word = "dependents per word", MeasureType.graph, dependency._dependents_per_word


def calculate_for_sentence(conll_sentence: str, measure: SentenceMeasure) -> Tuple[str, float] | None:
    conll_sentence = conll_sentence.split("\n")
    sentences, graphs = zip(*conllu.read_conllu_sentences(conll_sentence))
    if len(sentences) > 1:
        raise ValueError()
    sentence_tokens = list(itertools.chain.from_iterable(sentences))
    graph = graphs[0]

    m_name, m_type, m_func = measure.value
    if m_type == MeasureType.text:
        text = Text.from_tokens(sentence_tokens)
        return m_name, m_func(text)
    elif m_type == MeasureType.graph:
        return m_name, m_func(graph)
    else:
        return None
