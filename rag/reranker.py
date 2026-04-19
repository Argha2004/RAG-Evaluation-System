from sentence_transformers import CrossEncoder

# stronger model
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, docs):
    pairs = [(query, doc) for doc in docs]
    scores = reranker.predict(pairs)

    # sort by score
    ranked = sorted(zip(docs, scores), key=lambda x: x[1], reverse=True)
    best_doc = ranked[0][0]

    return [doc for doc, _ in ranked]