# Ragna

A Retrieval Augmented Generation app

Uses Streamlit, FastAPI, ChromaDB and the OpenRouter API

For a detailed explantion, read [ARCHITECTURE.md](./ARCHITECTURE.md)

## Steps to run

- First, you need to have the `uv` package manager installed, you can do that [here](https://docs.astral.sh/uv/)
- Clone the git repository using:
```bash
git clone https://github.com/sohan-sohan/ragna_new.git
```
- `cd` into `ragna_new`
- Create an OpenRouter API key [here](https://openrouter.ai/) and save the following into a `.env` file:
```bash
API_KEY = <your API key>
```
- Open a terminal and run the following commands:
```bash
uv sync # sets up the virtual environment with dependencies
uv run streamlit run frontend.py
```
- Open another terminal, `cd` into the `ragna_new` folder again, and run:
```bash
uv run uvicorn backend:app --reload
```
- The app will open in your browser
