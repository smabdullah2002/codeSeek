from sentence_transformers import SentenceTransformer

model= SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts: list[str]):
    return model.encode(texts, batch_size=32, show_progress_bar=True).tolist()
def embed_query(text:str):
    return model.encode(text).tolist()