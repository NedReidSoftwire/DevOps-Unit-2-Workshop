from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import json
from pydantic import BaseModel
from typing import TypedDict, List

class QuizQuestion(BaseModel):
    question: str
    options: List[str]
    answerIndex: int

class QuizData(BaseModel):
    questions: List[QuizQuestion]

load_dotenv()

QUIZ_DATA_JSON_FILEPATH = 'quiz-data.json'
QUESTIONS_JSON_KEY = 'questions'
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=os.getenv('TOKEN'))

def load_quiz_questions(json_filepath: str) -> List[QuizQuestion]:
    try:
        with open(json_filepath, 'r') as file:
            data = QuizData.model_validate_json(file.read())

            questions = data.questions
            if not questions:
                raise ValueError("Quiz questions array is empty")

            return questions
    except FileNotFoundError as e:
        raise FileNotFoundError(f"{json_filepath} file not found") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in {json_filepath}", e.doc, e.pos) from e

print("Welcome to the Pub Quiz!")
score = 0

try:
    quiz_questions = load_quiz_questions(QUIZ_DATA_JSON_FILEPATH)
except Exception as e:
    print(f"Error loading quiz questions: {e}")
    exit(1)

for question in quiz_questions:
    question_text = question.question
    messages = [{"role": "user",
                 "content": f' rewrite the following question as if you are a DevOps trainer named Ray. Ray starts his questions by saying his name. '
                            f'Include lots of DevOps words like 7000x more deployments. Make responses short and snappy: {question_text}'}]
    print(client.chat_completion(messages, max_tokens=150).get('choices')[0].get('message').get('content'))

    question_options = question.options
    for i, option in enumerate(question_options):
        option_id = chr(ord('A') + i)
        print(f"{option_id}) {option}")

    user_answer = input("Your answer (A, B, C, D): ").strip().upper()
    user_answer_index = ord(user_answer) - ord('A')

    question_correct_answer_index = question.answerIndex
    if user_answer_index == question_correct_answer_index:
        print("Correct!")
        score += 1
    else:
        question_correct_answer = question_options[question_correct_answer_index]
        print(f"Wrong! The correct answer was {question_correct_answer}.")

print("Thanks for playing the Pub Quiz!")
print(f"Your final score is {score}")
