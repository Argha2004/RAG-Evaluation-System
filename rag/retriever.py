from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def create_retriever(texts):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )

    db = FAISS.from_texts(texts, embeddings)
    return db.as_retriever(search_kwargs={"k": 5})  # get more, rerank later