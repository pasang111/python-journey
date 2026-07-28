questions = {
    "Capital of France? ": "Paris",
    "5 + 3 = ? ": "8",
    "Python is a programming language? (yes/no): ": "yes"
}

score = 0

for question, answer in questions.items():
    user = input(question)
    if user.lower() == answer.lower():
        score += 1

print("Score:", score, "/", len(questions))
