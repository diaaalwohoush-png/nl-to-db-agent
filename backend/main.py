import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db = SQLDatabase.from_uri(f"sqlite:///{BASE_DIR}/chinook.db")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=1024,
)

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=10,
    max_execution_time=30,
    agent_type="openai-tools",
)

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(question: Question):
    try:
        result = agent.invoke({"input": question.question})
        return {
            "answer": result["output"],
            "steps": str(result.get("intermediate_steps", []))
        }
    except Exception as e:
        return {"answer": f"Error: {str(e)}", "steps": []}