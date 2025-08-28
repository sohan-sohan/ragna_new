from chromadb.api.models.Collection import Collection
import chromadb

def retrieve_topn_chunks(collection: Collection, query_str: str, n: int):

    results = collection.query(
        query_texts=[query_str],
        n_results=n
    )

    topn_chunks = []

    for chunk in results['documents'][0]:
        topn_chunks.append(chunk)

    return topn_chunks
