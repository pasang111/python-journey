questions = {
    "Capital of France? ": "Paris",
    "5 + 3 = ? ": "8",
    "Python is a programming language? (yes/no): ": "yes",
    "What is 10 * 2? ": "20",
    "Capital of Nepal? ": "Kathmandu",
    "What color is the sky on a clear day? ": "blue",
    "What is 15 - 7? ": "8",
    "Python was created by Guido van Rossum? (yes/no): ": "yes",
    "How many days are in a week? ": "7",
    "What is 4 * 5? ": "20"
}

score = 0

for question, answer in questions.items():
    user = input(question)

    if user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answer)

print("Score:", score, "/", len(questions))
