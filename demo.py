"""Demonstração mínima de uso --- Trabalho Prático de IA (FACOM/UFMS, 2026/1).

Dada uma consulta em texto livre, devolve a lista ranqueada de documentos da
coleção usando o ranking híbrido (BM25 + TF-IDF/KNN via Reciprocal Rank Fusion).

Uso:
    python demo.py "subgraph matching algorithms for graph databases"
    python demo.py "subgraph matching algorithms for graph databases" --k 5
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

from rank_bm25 import BM25Okapi
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.preprocessing import preprocess, preprocess_to_string

KAPPA = 60  # constante do Reciprocal Rank Fusion


def load_corpus(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f]


def build_indexes(docs):
    texts = [d["title"] + ". " + d["abstract"] for d in docs]

    tokenized = [preprocess(t) for t in texts]
    bm25 = BM25Okapi(tokenized, k1=1.5, b=0.75)

    preprocessed_strings = [preprocess_to_string(t) for t in texts]
    vectorizer = TfidfVectorizer(min_df=2, max_df=0.85)
    doc_vectors = vectorizer.fit_transform(preprocessed_strings)

    return bm25, vectorizer, doc_vectors


def rank_bm25(query, bm25, top_k):
    scores = bm25.get_scores(preprocess(query))
    order = scores.argsort()[::-1][:top_k]
    return [(int(i), int(rank)) for rank, i in enumerate(order, 1)]


def rank_knn(query, vectorizer, doc_vectors, top_k):
    q_vector = vectorizer.transform([preprocess_to_string(query)])
    sims = cosine_similarity(q_vector, doc_vectors).flatten()
    order = sims.argsort()[::-1][:top_k]
    return [(int(i), int(rank)) for rank, i in enumerate(order, 1)]


def reciprocal_rank_fusion(*rankings, kappa=KAPPA):
    scores = defaultdict(float)
    for ranking in rankings:
        for doc_idx, rank in ranking:
            scores[doc_idx] += 1.0 / (kappa + rank)
    return sorted(scores.items(), key=lambda x: x[1], reverse=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("query", help="Consulta em texto livre")
    ap.add_argument("--k", type=int, default=10, help="Número de documentos a retornar")
    ap.add_argument("--corpus", type=Path, default=Path("data/corpus.jsonl"))
    args = ap.parse_args()

    docs = load_corpus(args.corpus)
    bm25, vectorizer, doc_vectors = build_indexes(docs)

    bm25_ranking = rank_bm25(args.query, bm25, top_k=100)
    knn_ranking = rank_knn(args.query, vectorizer, doc_vectors, top_k=100)
    fused = reciprocal_rank_fusion(bm25_ranking, knn_ranking)[: args.k]

    print(f'Consulta: "{args.query}"\n')
    for rank, (doc_idx, score) in enumerate(fused, 1):
        d = docs[doc_idx]
        print(f"{rank:>2}. [RRF={score:.5f}] {d['title']}")
        print(f"    {d['arxiv_id']} | {d.get('primary_category')} | {d.get('published', '')[:10]}")
        print(f"    {d['abstract'][:200]}...")
        print()


if __name__ == "__main__":
    main()
