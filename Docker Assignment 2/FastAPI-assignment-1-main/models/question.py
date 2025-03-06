# models/question.py
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))  # Link to quiz
    statement = Column(String)                           # Question text
    options = Column(JSON)                               # Options as JSON (e.g., {"A": "Option A", "B": "Option B"})
    correct_answer = Column(String)                      # Correct option (e.g., "A")