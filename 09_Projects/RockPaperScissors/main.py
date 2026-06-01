player1 = input("Player one choose rock paper and scissor: ")
player2 = input("Player one choose rock paper and scissor: ")

if player1 == player2:
    print("It's a tie")
elif player1 == "rock" and player2 == "scissor":
    print("Player 1 won the game")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 won the game")
elif player1 == "scissor" and player2 == "paper":
    print("Player 1 won the game")
else:
    print("Player 2 won the game")