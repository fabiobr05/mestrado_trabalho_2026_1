"""Pré-processamento textual compartilhado entre documentos e queries.

Mesma função (`preprocess`) é aplicada à coleção e às consultas para garantir
que ambos os lados sejam tokenizados/normalizados de forma idêntica (etapa b
do enunciado).
"""
import re
import string

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

for resource in ("stopwords", "punkt", "punkt_tab"):
    try:
        nltk.data.find(f"corpora/{resource}" if resource == "stopwords" else f"tokenizers/{resource}")
    except LookupError:
        nltk.download(resource, quiet=True)

_STOPWORDS = set(stopwords.words("english"))
_STEMMER = PorterStemmer()
_PUNCT_TABLE = str.maketrans("", "", string.punctuation)


def tokenize(text: str) -> list[str]:
    """Lower-case, remove pontuação e divide em tokens por espaço."""
    text = text.lower().translate(_PUNCT_TABLE)
    text = re.sub(r"\s+", " ", text).strip()
    return text.split() if text else []


def preprocess(text: str, use_stemming: bool = True) -> list[str]:
    """Pipeline completo: tokenização -> remoção de stopwords -> stemming opcional.

    Stemming é aplicado por padrão para reduzir variações morfológicas comuns em
    textos técnicos (e.g., "querying"/"queries"/"query" -> "queri"), o que ajuda
    tanto o BM25 quanto o TF-IDF a casarem termos relacionados.
    """
    tokens = tokenize(text)
    tokens = [t for t in tokens if t not in _STOPWORDS and len(t) > 1]
    if use_stemming:
        tokens = [_STEMMER.stem(t) for t in tokens]
    return tokens


def preprocess_to_string(text: str, use_stemming: bool = True) -> str:
    """Conveniência: retorna o resultado de `preprocess` como string espaçada,
    útil para vetorizadores que esperam texto (e.g., TfidfVectorizer)."""
    return " ".join(preprocess(text, use_stemming=use_stemming))
