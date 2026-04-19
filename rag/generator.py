from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_answer(query, context):
    sentences = [s.strip() for s in context.split(".") if len(s.strip()) > 20]

    if not sentences:
        return context

    # rank sentences by similarity to query
    query_emb = model.encode([query])
    sent_emb = model.encode(sentences)

    scores = cosine_similarity(query_emb, sent_emb)[0]

    best_idx = scores.argmax()

    return sentences[best_idx]