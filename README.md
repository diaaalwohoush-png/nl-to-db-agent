# NL-to-Database Agent

A proof-of-concept AI agent that converts natural language questions into SQL queries and returns human-readable answers.

## What it does
- User types a question in plain English
- A LangChain SQL Agent figures out the right SQL query
- The query runs against the Chinook database
- The result is returned as a natural language answer

## Tech Stack
- **Backend:** FastAPI (Python)
- **AI Agent:** LangChain + Groq (llama-3.3-70b-versatile)
- **Database:** Chinook SQLite
- **Frontend:** Plain HTML/CSS/JavaScript

## How to run

1. Clone the repo
2. Create a virtual environment and activate it: