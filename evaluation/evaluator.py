from rag.pipeline import run_rag
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_similarity(pred, truth):
    emb1 = model.encode([pred])
    emb2 = model.encode([truth])
    return cosine_similarity(emb1, emb2)[0][0]


def evaluate(dataset, retriever):
    results = []

    for item in dataset:
        docs, pred = run_rag(item["question"], retriever)

        sim = semantic_similarity(pred, item["answer"])

        results.append({
            "question": item["question"],
            "prediction": pred,
            "truth": item["answer"],
            "similarity": round(sim, 2),
            "correct": sim > 0.65
        })

    return results

def precision_at_k(retrieved, relevant, k=1):
    return 1 if retrieved[0] in relevant else 0