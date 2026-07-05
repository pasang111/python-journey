import time

while True:
    input("Ask me anything: ")

    for _ in range(10):   # Think 10 times
        print("Thinking.", end="\r")
        time.sleep(0.5)

        print("Thinking..", end="\r")
        time.sleep(0.5)

        print("Thinking...", end="\r")
        time.sleep(0.5)

    print("\nBro, just Google it. 💀\n")