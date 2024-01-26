# Streamlit LLM App

An example of using `LangChain` and native `boto3` libraries to access Foundational Models hosted on AWS Bedrock. 

This application provides cooking advice by accessing the Llama 2 70b Chat Model, and tailors the response style to match the selected chef from the streamlit application

## Prerequisites

Before running the app, ensure you have the following:

- Python 3.12.1 or greater installed

Also ensure you have an AWS Access Key and Secret ID Key. These keys should be present in their default location of `~/.aws/credentials`

```
[your-aws-profile-name]
aws_access_key_id = <ACCESS_KEY_ID>
aws_secret_access_key = <SECRET_ACCESS_KEY>
```

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

```poetry run streamlit run ask_chef/main.py```

## ConfluenceLoader

In order to use ConfluenceLoader to load documents, I needed to run

```
brew install tesseract poppler
```