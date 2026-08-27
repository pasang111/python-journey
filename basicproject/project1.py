import time
import random

# Store different responses
responses = [
    "Bro, just Google it.",
    "Bro, you nub.",
    "Do it yourself.",
    "I don't know bro.",
    "That is above my pay grade.",
    "You really thought I knew that?"
]


# Show the thinking animation
def thinking():
    for _ in range(5):
        print("Thinking.", end="\r")
        time.sleep(0.3)

        print("Thinking..", end="\r")
        time.sleep(0.3)

        print("Thinking...", end="\r")
        time.sleep(0.3)


# Generate a random response
def get_response():
    return random.choice(responses)


# Main program
while True:
    question = input("\nAsk me anything: ").strip()

    # Exit the program
    if question.lower() in ["exit", "quit", "q"]:
        print("Goodbye!")
        break

    # Check for empty input
    if not question:
        print("You need to ask something.")
        continue

    thinking()

    print(f"\n{get_response()}")
