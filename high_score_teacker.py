while True:
    game_score = input("Enter a game score:")

    if game_score == "stop".strip().lower():
        print("Game session ended!")
        break
    else:
        game_score = int(game_score)

        if game_score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")    
           