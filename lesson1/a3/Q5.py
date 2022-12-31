# Make a two-player Rock-Paper-Scissors game.
# Ask for player plays (using input), compare them, print out a message of congratulations to the winner.
# Remember the rules:
# - Rock beats scissors
# - Scissors beats paper
# - Paper beats rock

player1 = input("Please enter your choice (rock/paper/scissors): ")
player2 = input("Please enter your choice (rock/paper/scissors): ")

if player2 == player1:
    print("It's a draw")
elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') \
        or (player1 == "paper" and player2 == 'rock'):
    print("Congrats player 1")
else:
    print("Congrats player 2")