# Checklist de submissão --- Trabalho Prático de IA (2026/1)

Use esta lista antes de submeter o seu `.zip` no AVA. Cada item evita uma penalidade comum na correção.

## Coleção
- [x] Coleção tem entre 1.000 e 5.000 artigos. (1.097)
- [x] Tema da coleção está alinhado ao seu projeto de pesquisa.
- [x] Critérios de coleta (palavras-chave, categorias, janela temporal) estão documentados.
- [x] Arquivos `arxiv_raw.jsonl` e `corpus.jsonl` (ou link externo) estão na entrega.

## Pré-processamento
- [x] Decisões de tokenização / *stopwords* / *stemming* estão justificadas no relatório.
- [x] Mesmo pré-processamento é aplicado a consultas e documentos.

## Modelos
- [x] **BM25 implementado**, hiperparâmetros documentados, conexão com paradigma probabilístico discutida.
- [x] **KNN/recuperador denso implementado**, escolha da representação justificada.
- [x] Pelo menos 1 (Mestrado) ou 2 (Doutorado) módulos de aprofundamento implementados. (M5, mestrado)
- [ ] Doutorado: módulo M1 ou M5 está entre os escolhidos. (N/A --- aluno é Mestrado)

## Avaliação
- [x] 10 a 20 *queries* criadas, refletindo o tema da coleção. (14)
- [x] Arquivo `qrels.tsv` com anotações manuais de relevância sobre o *top-k* dos modelos (*pooling*). (revisar anotações antes da entrega final --- ver README)
- [x] Métricas P@k, R@k e MAP (ou nDCG) reportadas, com análise.
- [x] Análise qualitativa de pelo menos 2 *queries* (acertos e falhas).
- [ ] Doutorado: teste estatístico de significância na comparação principal. (N/A --- aluno é Mestrado)

## Relatório
- [x] Formato SBC, até 10 páginas. (migrado para `sbc-template.sty` oficial; compilado com pdflatex --- 6 páginas)
- [x] Seções: Resumo, Introdução, Trabalhos Relacionados, Metodologia, Avaliação, Resultados, Discussão, Conclusão, Referências.
- [x] Subseção dedicada à relação entre coleção e tema de pesquisa do aluno.
- [x] Conexões explícitas entre componentes implementados e tópicos da disciplina.
- [x] Declaração curta de uso de IA generativa (se houve).
- [ ] Link do vídeo em nota de rodapé na conclusão. (ainda é placeholder `https://...`)

## Reprodutibilidade
- [x] `README.md` com instruções claras de como reproduzir.
- [x] `requirements.txt` declarando dependências.
- [x] Notebooks / scripts executam sem ajustes manuais excessivos.
- [x] Sementes aleatórias fixadas onde relevante.
- [x] Demonstração mínima de uso (item 3 dos entregáveis, Seção 7 do enunciado): script/notebook
      que recebe uma consulta em texto e devolve o ranking, executável sem rodar os notebooks
      antes. Implementado em `demo.py` (`python demo.py "<consulta>" --k 10`).

## Vídeo
- [ ] Duração ≤ 8 minutos.
- [ ] Cobre motivação, decisões de projeto, modelos, metodologia, resultados.
- [ ] Hospedado em plataforma de acesso público (YouTube ou Google Drive).
- [ ] Link incluído no relatório e em `LINKS.txt`.

## Empacotamento
- [ ] `.zip` único contendo: relatório PDF, código-fonte, eval/, `README.md`, `requirements.txt`, `LINKS.txt`.
- [ ] Submetido até **23:59 de 17/06/2026** no AVA.
