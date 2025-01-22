import json

QUIZ_DATA_JSON_FILEPATH = 'quiz-data.json'
QUESTIONS_JSON_KEY = 'questions'

def load_quiz_questions(json_filepath: str):
    try:
        with open(json_filepath, 'r') as file:
            data = json.load(file)

            if QUESTIONS_JSON_KEY not in data:
                raise KeyError("Quiz questions not found in JSON structure")

            questions = data[QUESTIONS_JSON_KEY]
            if not questions:
                raise ValueError("Quiz questions array is empty")

            return questions
    except FileNotFoundError as e:
        raise FileNotFoundError(f"{json_filepath} file not found") from e
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON format in {json_filepath}", e.doc, e.pos) from e

# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

try:
    quiz_questions = load_quiz_questions(QUIZ_DATA_JSON_FILEPATH)
except Exception as e:
    print(f"Error loading quiz questions: {e}")
    exit(1)

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)

    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper()  # Ensuring the input is uppercase for comparison

    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")