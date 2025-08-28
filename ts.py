

from chunking import chunk_and_populate

file = open('s1.pdf', 'rb')

fb = file.read()

col = chunk_and_populate(fb, 300)


print(col.query(query_texts=['somato']))