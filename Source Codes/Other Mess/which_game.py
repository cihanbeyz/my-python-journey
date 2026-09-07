def main():

    difficulty = input("Choose a difficulty level: EASY OR HARD? ").lower()
    if not (difficulty == "easy" or difficulty == "hard"):
        print( "Invalid difficulty level, Please Choose One")
        return
    player = input("Choose player preference: Single player Or Multiplayer? ").lower().strip()
    if not (player == "singleplayer" or player == "multiplayer"):
        print("Invalid player, Please Choose Again.")
        return

    if player == "singleplayer" and difficulty == "hard":
        recommand("Poker")
    elif player =="singlerplayer" and difficulty == "easy":
        recommand("Pubg")
    elif player =="multiplayer" and difficulty == "hard":
        recommand("Nora")
    elif player =="multiplayer" and difficulty == "easy":
        recommand("Freefire")
def recommand(game):
    x = "We recommend you to play " + game
    print(x)

main()



