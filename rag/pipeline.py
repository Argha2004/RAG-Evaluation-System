from rag.generator import generate_answer
from rag.reranker import rerank

def run_rag(query, retriever):
    docs = retriever.invoke(query)
    texts = [d.page_content for d in docs]

    ranked_docs = rerank(query, texts)

    best_doc = ranked_docs[0]

    answer = generate_answer(query, best_doc)

    return [best_doc], answer