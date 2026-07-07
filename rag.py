import os
from pypdf import PdfReader


def load_documents(folder_path):

    documents = []

    for file_name in os.listdir(folder_path):

        if file_name.endswith(".pdf"):

            file_path = os.path.join(folder_path, file_name)

            reader = PdfReader(file_path)

            text = ""

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted

            documents.append(
                {
                    "file_name": file_name,
                    "text": text
                }
            )

    return documents


def split_into_chunks(document, chunk_size=500, overlap=100):

    chunks = []

    text = document["text"]
    source = document["file_name"]

    start = 0
    chunk_id = 1

    while start < len(text):

        end = start + chunk_size

        chunk_text = text[start:end]

        chunks.append(
            {
                "source": source,
                "chunk_id": chunk_id,
                "text": chunk_text
            }
        )

        start += chunk_size - overlap
        chunk_id += 1

    return chunks


if __name__ == "__main__":

    docs = load_documents("pdf_docs")

    for doc in docs:

        chunks = split_into_chunks(doc)

        print("=" * 60)

        print("File:", doc["file_name"])
        print("Total Chunks:", len(chunks))

        print("\nFirst Chunk Metadata:\n")
        print(chunks[0])