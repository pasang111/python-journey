import time
import random

responses = [
    "I have absolutely no idea.",
    "42. Probably.",
    "Error: Brain.exe stopped working.",
    "Ask your teacher.",
    "I refuse to answer."
]

while True:
    input("Ask me anything: ")

    for i in range(0, 101, 10):
        print(f"Generating answer... {i}%", end="\r")
        time.sleep(0.2)

    print("\n" + random.choice(responses))
    print()
