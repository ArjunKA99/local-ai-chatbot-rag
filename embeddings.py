import requests

EMBED_MODEL = "nomic-embed-text"


def get_embedding(text):

    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": EMBED_MODEL,
            "prompt": text
        }
    )

    embedding = response.json()["embedding"]

    return embedding


if __name__ == "__main__":

    vector = get_embedding("Python SQL Power BI")

    print("Vector Length:", len(vector))

    print()

    print("First 10 Numbers:")

    print(vector[:10])