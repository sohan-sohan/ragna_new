import requests
import json
from dotenv import load_dotenv
import os



def construct_prompt(question: str, relevant_chunks: list):

    prompt = f'answer the following question with the context provided, return only the answer, and not any other information \n Question: {question} \n Context: {relevant_chunks}'

    return prompt



def get_rag_answer(prompt: str) -> str:
    
    """
    takes in a prompt(consisting of the question and the relevant chunks), sends it to an LLM and returns its response
    """

    load_dotenv()
    api_key = os.getenv("API_KEY")

    response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "google/gemma-3n-e4b-it:free", # 
    "messages": [
      {
        "role": "user",
        "content": prompt
      }
    ],
    
  })
)
    
    print(response.json())
    
    answer = response.json()['choices'][0]['message']['content']

    return answer
