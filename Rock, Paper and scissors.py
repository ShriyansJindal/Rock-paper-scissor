import random
def playGame():
    lives =3
    player_score = 0
    comp_score=0
    options = ["Rock", "Paper", "Scissors"]
    while lives>0:

        player_turn = input("Choose Rock, Paper, or Scissors: ").upper()
        comp_turn = random.choice(options).upper()

        print("You chose: ", player_turn)
        print("Computer chose: ", comp_turn)
        if player_turn == comp_turn:
            print("It's a tie!")

        elif player_turn == "ROCK" and comp_turn == "SCISSORS":
            player_score+=1
            print("You win!")

        elif player_turn == "PAPER" and comp_turn == "ROCK":
            player_score += 1
            print("You win!")

        elif player_turn == "SCISSORS" and comp_turn == "PAPER":
            player_score += 1
            print("You win!")

        else:
            comp_score +=1
            lives-=1
            print("Computer wins!")
        print("Your Score: ",player_score)
        print("Computer Score: ",comp_score)
        print("lives left: ",lives)
        print()

playGame()
player = True
while player:
    n = int(input("Enter 1 to continue and 0 to stop: "))
    if(n==1):
        playGame()
    else:
        print("Thanks for playing")
        player = False