from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
client = OpenAI()

class TextInput(BaseModel):
    text: str

@app.post("/generate-questions")
def generate_questions(data: TextInput):
    prompt = f"""
Read the following text and generate 5 meaningful exam-oriented questions.

Text:
{data.text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return {
        "questions": response.choices[0].message.content
    }
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (safe for college project)
    allow_credentials=True,
    allow_methods=["*"],   # allow POST, GET, OPTIONS
    allow_headers=["*"],
)
