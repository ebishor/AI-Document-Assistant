from sentence_transformers import SentenceTransformer

# Load once when the application starts
model = SentenceTransformer("BAAI/bge-small-en-v1.5")


def generate_embedding(text: str):
    """
    Generate an embedding for the given text.
    """
    embedding = model.encode(text)

    return embedding.tolist()