from Games import guess_game, currency_roulette, memory_game


def welcome():
    while True:
        username = input("Enter Username\n")
        if len(username) > 12 or len(username) < 4:
            print("Username must be between 4-12 characters")
        else:
            print("Hi", username, "and welcome to the World Of Games: The Epic Journey")
            return username


def start_play():
    global user_score
    global game_on
    game_on = True
    user_score = 0
    while game_on is True:
        global game
        game = input("Please choose a game to play:\n"
            "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
            "2. Guess Game - guess a number and see if you chose like the computer.\n"
            "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                     "Type 'q' to exit or 'u' to change Username\n")
        try:
            if str(game) == 'u':
                welcome()
            elif str(game) == 'q':
                game_on = False
            elif int(game) > 3 or int(game) == 0:
                print("Please choose a number between 1-3\n"
                      "Type 'q' to exit or 'u' to change Username\n")
            else:
                global difficulty
                difficulty = input("Please select difficulty level between 1-5\n"
                                   "Type 'q' to go exit or '*' for game menu\n")
                try:
                    if str(difficulty) == 'q':
                        game_on = False
                    elif str(difficulty) == '*':
                        start_play()
                    elif int(difficulty) > 5 or int(difficulty) == 0:
                        print("Please choose a number between 1-5\n"
                              "Type 'q' to to go back or '*' for game menu\n")
                    else:
                        while True:
                            if str(game) == 'q':
                                game_on = False
                            elif str(game) == '*':
                                start_play()
                            elif int(game) == 1:
                                memory_game.play(difficulty)
                            elif int(game) == 2:
                                guess_game.play(difficulty)
                            elif int(game) == 3:
                                currency_roulette.play(difficulty)
                except ValueError:
                    print("***ERROR***\n"
                    "Please choose a number between 1-5\n"
                          "Type 'q' to to go back or '*' for game menu\n")
        except ValueError:
            print("***ERROR***\n"
                  "Please choose a number between 1-3\n"
                  "Type 'q' to exit or '*' for game menu\n")
