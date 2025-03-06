# schemas/question.py
from pydantic import BaseModel
from typing import Dict

class QuestionCreate(BaseModel):
    statement: str
    options: Dict[str, str]  # e.g., {"A": "Option A", "B": "Option B"}
    correct_answer: str      # e.g., "B"
    quiz_id: int

class QuestionOut(BaseModel):
    id: int
    statement: str
    options: Dict[str, str]
    correct_answer: str
    quiz_id: int

    class Config:
        orm_mode = True