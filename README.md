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
uv sync # sets up the virtual environment with dependencies
source .venv/bin/activate # activate the virtual environment that uv set up
streamlit run frontend.py # runs frontend server
```
- Open another terminal, `cd` into the `ragna_new` folder again, and run:
```bash
source .venv/bin/activate # activate the virtual environment that uv set up
uvicorn backend:app --reload # runs the backend server
```
- The app will open in your browser
