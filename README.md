# Streamlit LLM App

This application connects to the Llama model in Bedrock using `boto3` and is built with Streamlit.

## Prerequisites

Before running the app, ensure you have the following:

- Python 3.12.1 or greater installed

## Installation

### Installing Poetry

[Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python. To install Poetry, follow these steps:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

After installing Poetry, you can then install all the required prerequisites by running
```bash
poetry install
```

## Usage

```python -m streamlit run streamlit/main.py```
