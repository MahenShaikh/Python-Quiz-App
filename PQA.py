# Simple Python Quiz App

score = 0

questions = {
    "What is the capital of France? ": "Paris",
    "What is 2 + 2? ": "4",
    "What is the color of the sky on a clear day? ": "Blue",
    "Who wrote 'Romeo and Juliet'? ": "Shakespeare",
    "Which planet is known as the Red Planet? ": "Mars"
}

print("Welcome to the Python Quiz App!\n")

for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.strip().lower() == answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.\n")

print(f"Your final score: {score}/{len(questions)}")
