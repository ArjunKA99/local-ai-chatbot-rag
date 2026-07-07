from rag import load_documents, split_into_chunks
from vector_store import create_vector_store


def main():

    print("Loading PDF documents...")

    documents = load_documents("pdf_docs")

    print(f"Loaded {len(documents)} document(s).")

    all_chunks = []

    for doc in documents:

        chunks = split_into_chunks(doc)

        all_chunks.extend(chunks)

    print(f"Created {len(all_chunks)} chunks.")

    create_vector_store(all_chunks)


if __name__ == "__main__":
    main()