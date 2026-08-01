import time
import random

# List of possible answers
responses = [
    "I have absolutely no idea.",
    "42. Probably.",
    "Error: Brain.exe stopped working.",
    "Ask your teacher.",
    "I refuse to answer."
]

# Keep running until the user stops the program
while True:
    # Ask the user to type a question
    input("Ask me anything: ")

    # Show a fake loading animation
    for i in range(0, 101, 10):
        print(f"Generating answer... {i}%", end="\r")
        time.sleep(0.2)  # Wait for 0.2 seconds

    # Print a random answer from the list
    print("\n" + random.choice(responses))

    # It Print a blank line for better spacing
    print()
