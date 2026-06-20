# Trabalho Prático --- Inteligência Artificial (FACOM/UFMS, 2026/1)

**Aluno:** Fabio Batista Rodrigues
**Matrícula:** 2026.02713
**Nível:** Mestrado
**Tema da coleção:** Bancos de grafos, com foco em processamento e otimização de consultas em grafos

## Estrutura do repositório

```
.
├── README.md                  <- este arquivo
├── CHECKLIST.md               <- checklist de submissão (fornecido pela disciplina)
├── LINKS.txt                  <- link do vídeo (preencher antes da entrega)
├── demo.py                    <- demonstração mínima: query em texto -> ranking híbrido
├── requirements.txt           <- dependências Python
├── data/                      <- coleção bruta e processada
│   ├── arxiv_raw.jsonl        <- 1.097 registros coletados da API do ArXiv
│   └── corpus.jsonl           <- coleção limpa/deduplicada usada pelos recuperadores
├── notebooks/
│   ├── 01_coleta_arxiv.ipynb     <- etapa (a)+(b): coleta e geração do corpus
│   ├── 02_baseline_bm25.ipynb    <- etapa (c): BM25, gera runs/bm25.trec
│   ├── 03_retrieval_knn.ipynb    <- etapa (d): TF-IDF/KNN, gera runs/knn.trec
│   ├── 04_modulo_hibrido.ipynb   <- M5: RRF + avaliação comparativa, gera runs/hybrid.trec
│   └── runs/                     <- bm25.trec, knn.trec, hybrid.trec
├── src/                        <- código reutilizável (pré-processamento compartilhado)
│   ├── __init__.py
│   └── preprocessing.py
├── eval/
│   ├── queries.tsv             <- 14 queries de teste
│   ├── pool_for_annotation.tsv <- pool top-15 BM25 + top-15 TF-IDF, por query
│   ├── build_qrels.py          <- gera qrels.tsv a partir das anotações de relevância
│   ├── qrels.tsv               <- 304 julgamentos de relevância
│   └── evaluate.py             <- script de métricas (fornecido pela disciplina)
└── relatorio/
    ├── relatorio.tex           <- relatório no template oficial SBC (sbc-template.sty), 6 páginas
    ├── sbc-template.sty        <- estilo oficial SBC (do template oficial da SBC)
    ├── caption2.sty            <- dependência do sbc-template.sty
    └── relatorio.pdf           <- PDF compilado (gerar com: pdflatex relatorio.tex, 2x)
```

## Reprodução

```bash
# 1. Criar ambiente e instalar dependências
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. Coletar dados (ajuste as palavras-chave no notebook 01)
jupyter notebook notebooks/01_coleta_arxiv.ipynb

# 3. Rodar o baseline BM25
jupyter notebook notebooks/02_baseline_bm25.ipynb

# 3b. Rodar o recuperador KNN/TF-IDF
jupyter notebook notebooks/03_retrieval_knn.ipynb

# 3c. Rodar o módulo M5 (ranking híbrido) e a avaliação comparativa
jupyter notebook notebooks/04_modulo_hibrido.ipynb

# 4. Rodar avaliação isolada (opcional, já é feita dentro do notebook 04)
python eval/evaluate.py \
    --qrels eval/qrels.tsv \
    --runs notebooks/runs/bm25.trec notebooks/runs/knn.trec notebooks/runs/hybrid.trec \
    --k 10

# 5. Demonstração mínima: consulta em texto -> ranking híbrido (não depende dos notebooks)
python demo.py "subgraph matching algorithms for graph databases" --k 10
```

## Decisões de projeto

- **Tema/escopo da coleção:** Bancos de grafos, com foco em processamento e otimização de
  consultas (subgraph matching, query optimization, RDF/SPARQL, property graphs/Cypher,
  indexação, processamento distribuído).
- **Categorias do ArXiv consideradas:** cs.DB (principal), cs.AI, cs.DC, cs.DS, cs.IR, cs.LG, cs.SE.
- **Janela temporal:** 2008–2026 (ampliada em 3 rodadas de coleta para atingir o mínimo de
  1.000 artigos exigido; ver `notebooks/01_coleta_arxiv.ipynb`).
- **Tamanho final da coleção:** 1.097 artigos (após deduplicação e limpeza).
- **Pré-processamento:** lower-casing, remoção de pontuação, tokenização, remoção de
  stopwords (NLTK) e stemming (Porter Stemmer) --- ver `src/preprocessing.py`, usado de
  forma idêntica por BM25 e TF-IDF.
- **Modelos implementados:** BM25 (`rank_bm25`, k1=1.5, b=0.75) e KNN/denso via TF-IDF
  (`scikit-learn`, similaridade do cosseno).
- **Módulo(s) de aprofundamento:** M5 --- ranking híbrido sparse+dense via Reciprocal Rank
  Fusion (κ=60). Resultado: MAP híbrido = 0.763 vs. 0.719 (BM25) e 0.695 (KNN/TF-IDF) sobre
  as 14 queries de teste.
- **Avaliação:** 14 queries de teste, qrels construído via pooling (top-15 de cada sistema),
  304 julgamentos de relevância binária (173 relevantes).

## Uso de assistentes de IA generativa

O copilot foi utilizado para gestão do codigo auxiliando em tarefas repetitivas como atualização de documentação e correção de erros
dado uma pré-visualização de erros e entendimento deles.

## Vídeo de apresentação

URL: [Link VIDEO](https://drive.google.com/drive/folders/1VHhXLaSm9d74rKLoKvY-U_yUN-XgPzrh?usp=sharing)
