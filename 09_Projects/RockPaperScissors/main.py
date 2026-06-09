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