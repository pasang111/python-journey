# basic version of rock paper scissors game

# first we take input from both players
player1 = input("Player one choose rock paper and scissor: ")
player2 = input("Player one choose rock paper and scissor: ")

# if both players choose the same thing then the game is a tie
if player1 == player2:
    print("It's a tie")

# now checking all the winning conditions for player 1
elif player1 == "rock" and player2 == "scissor":
    print("Player 1 won the game")

elif player1 == "paper" and player2 == "rock":
    print("Player 1 won the game")

elif player1 == "scissor" and player2 == "paper":
    print("Player 1 won the game")

# if none of the above conditions are true
# then player 2 is the winner
else:
    print("Player 2 won the game")

# this is the basic version of the game
# the game runs only once and then stops

# now making a continuous version of rock paper scissors

# while True means the loop will keep running forever
# until we manually stop it using break

while True:

    # taking input from both users
    # .lower() converts everything to lowercase
    # so ROCK, Rock and rock are all treated the same
    user1 = input("User 1 input rock, paper, or scissors: ").lower()
    user2 = input("User 2 input rock, paper, or scissors: ").lower()

    # checking if both players selected the same option
    if user1 == user2:
        print("It's a tie")

    # checking all winning conditions for player 1
    elif user1 == "rock" and user2 == "scissors":
        print("Player 1 won the game")

    elif user1 == "scissors" and user2 == "paper":
        print("Player 1 won the game")

    elif user1 == "paper" and user2 == "rock":
        print("Player 1 won the game")

    # if none of the above conditions are true
    # then player 2 wins the game
    else:
        print("Player 2 won the game")

    # asking the users if they want to play again
    play_again = input("Play again? (yes/no): ")

    # if the answer is not yes
    # print the message and stop the loop
    if play_again != "yes":
        print("Thanks for playing!")
        break

# unlike the basic version
# this version keeps running until the users decide to stop