import os
import pickle
import faiss
import numpy as np

from embeddings import get_embedding


def create_vector_store(chunks):

    # Create vector_db folder if it doesn't exist
    os.makedirs("vector_db", exist_ok=True)

    embeddings = []
    metadata = []

    # Generate embedding for every chunk
    for chunk in chunks:

        embedding = get_embedding(chunk["text"])

        embeddings.append(embedding)

        metadata.append(
            {
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"]
            }
        )

    # Convert list to NumPy array
    embeddings = np.array(embeddings, dtype="float32")

    # Create FAISS index
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to index
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, "vector_db/index.faiss")

    # Save metadata
    with open("vector_db/metadata.pkl", "wb") as f:

        pickle.dump(metadata, f)

    print("Vector store created successfully!")
    print(f"Total Chunks Indexed: {len(metadata)}")


def search(query, k=3):

    # Load FAISS index
    index = faiss.read_index("vector_db/index.faiss")

    # Load metadata
    with open("vector_db/metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    # Convert query to embedding
    query_embedding = get_embedding(query)

    # Convert to NumPy array
    query_embedding = np.array([query_embedding], dtype="float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, k)

    results = []

    # Retrieve matching chunks
    for idx in indices[0]:
        if idx != -1:
          results.append(metadata[idx])

    return results