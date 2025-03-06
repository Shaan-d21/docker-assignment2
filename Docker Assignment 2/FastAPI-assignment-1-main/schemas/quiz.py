# schemas/quiz.py
from pydantic import BaseModel
from typing import List, Dict

class QuizCreate(BaseModel):
    title: str
    description: str

# Schema for questions as seen by participants (excludes correct_answer)
class QuestionParticipant(BaseModel):
    id: int
    statement: str
    options: Dict[str, str]  # e.g., {"A": "Option A", "B": "Option B"}
    quiz_id: int

class QuizOut(BaseModel):
    id: int
    title: str
    description: str
    created_by: int
    questions: List[QuestionParticipant] =[]  # Add questions here

    class Config:
        orm_mode = True