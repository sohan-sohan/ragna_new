import chromadb
import pymupdf
from chromadb.api.models.Collection import Collection

def chunk_and_populate(file_in_binary, chunk_size: int):
    """
    Creates a collection, chunks the file and populates the collection with the chunks
    Returns the populated collection object
    Adjust the chunksize(no of chars in a chunk) to your liking
    """
    
    client = chromadb.Client()
    collection = client.create_collection('collection1')

    print('collection created')

    doc = pymupdf.open(stream=file_in_binary)
    id_counter = 0

    for page in doc:
        page_text = page.get_text()
        for i in range(0, len(page_text), chunk_size):
            id_counter += 1
            chunk = page_text[i:i+chunk_size]
            collection.add(
                ids=[str(id_counter)],
                documents=[chunk]
            )
            print('added chunk')

    return collection