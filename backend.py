
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from chunking import chunk_and_populate
from database import retrieve_topn_chunks
from llm import construct_prompt, get_rag_answer

class Question(BaseModel):
    question_text: str

# post request that accepts file and chunks and stores it in chromadb


# post request that accepts a question, retrieves relevant chunks and does all others and gets response from llm


app = FastAPI()

@app.post('/processfile')
async def process_file(file: UploadFile):
    fb = await file.read()
    global col
    col = chunk_and_populate(fb, 200)
    if col:
        return {"message": "colection created"}
    else:
        return {"message": "something went wrong"}
    

@app.post('/question')
def answer_question(question: Question):
    question_text = question.question_text

    rel_chunks = retrieve_topn_chunks(col, question_text, 3)

    prompt = construct_prompt(question_text, rel_chunks)

    answer = get_rag_answer(prompt)

    return {"message": answer,
            "rel_chunks": rel_chunks}


