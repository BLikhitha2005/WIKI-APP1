import os
import json
import re
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

def load_prompt(filename: str) -> str:
    path = os.path.join(PROMPTS_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


QUIZ_PROMPT = load_prompt("quiz_prompt.txt")
TOPICS_PROMPT = load_prompt("topics_prompt.txt")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.2
)

def extract_json(text):
    text = text.replace("```json", "").replace("```", "").strip()
    try:
        return json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
        raise ValueError("Invalid JSON from LLM")

def generate_quiz_and_entities(content):
    prompt = PromptTemplate.from_template(QUIZ_PROMPT)
    response = llm.invoke(prompt.format(content=content))
    return extract_json(response.content)

def generate_related_topics(title, summary):
    prompt = PromptTemplate.from_template(TOPICS_PROMPT)
    response = llm.invoke(prompt.format(title=title, summary=summary))
    return extract_json(response.content)
def generate_quiz_and_entities(content: str):
    return {
        "quiz": [
            {
                "question": "Who was Alan Turing?",
                "options": [
                    "A British mathematician",
                    "A physicist",
                    "A chemist",
                    "A biologist"
                ],
                "answer": "A British mathematician",
                "difficulty": "easy",
                "explanation": "Alan Turing is described as a British mathematician in the article."
            },
            {
                "question": "What is Alan Turing famous for?",
                "options": [
                    "Inventing the telephone",
                    "Breaking the Enigma code",
                    "Discovering gravity",
                    "Creating electricity"
                ],
                "answer": "Breaking the Enigma code",
                "difficulty": "medium",
                "explanation": "Turing played a key role in breaking the Enigma cipher during WWII."
            }
        ],
        "key_entities": {
            "people": ["Alan Turing"],
            "organizations": ["Bletchley Park"],
            "locations": ["United Kingdom"]
        }
    }

def generate_related_topics(title: str, summary: str):
    return {
        "related_topics": [
            "Cryptography",
            "Enigma Machine",
            "Computer Science History",
            "Artificial Intelligence"
        ]
    }
