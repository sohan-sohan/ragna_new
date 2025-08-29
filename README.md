# Ragna

A Retrieval Augmented Generation app

Uses Streamlit, FastAPI, ChromaDB and the OpenRouter API

## Steps to run

- Clone the git repository
- `cd` into `ragna_new`
- Create an OpenRouter API key and save the following into a `.env` file:
```bash
API_KEY = <your API key>
```
- Run the following commands:
```bash
uv sync # sets up dependencies
streamlit run frontend.py # runs frontend server
uvicorn backend:app --reload # runs backend server
```
- The app will open in your browser