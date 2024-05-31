from Games import guess_game, currency_roulette, memory_game


def welcome():
    while True:
        username = input("Enter Username\n")
        if len(username) > 12 or len(username) < 4:
            print("Username must be between 4-12 characters")
        else:
            print("Hi", username, "and welcome to the World Of Games: The Epic Journey")
            return username


def difficulty_menu():
    global difficulty
    difficulty = input("Please select difficulty level between 1-5\n"
                       "Type 'q' to go exit or '*' for game menu\n")
    while str(difficulty) != 'q' or str(difficulty) != '*':
        try:
            if str(difficulty) == 'q':
                print("Thank you for playing, Goodbye")
                return difficulty
            elif str(difficulty) == '*':
                start_play()
                return difficulty
            elif int(difficulty) > 5 or int(difficulty) == 0:
                print("Invalid number\n")
                difficulty_menu()
                return difficulty
            else:
                if int(game) == 1:
                    memory_game.play(difficulty)
                    if str(game) == 'q':
                        return game
                elif int(game) == 2:
                    guess_game.play(difficulty)
                    if str(game) == 'q':
                        return game
                elif int(game) == 3:
                    currency_roulette.play(difficulty)
                    if str(game) == 'q':
                        return game
        except ValueError:
            print("***ERROR***\n")
            difficulty_menu()
            return difficulty
# To check: The next 5 lines might be irrelevant
    if str(difficulty) == 'q':
        print("Thank you for playing, Goodbye")
    elif str(difficulty) == '*':
        start_play()
        return difficulty


def start_play():
    # To do: Add user score based on difficulty
    # global user_score
    global game
    # user_score = 0
    game = input("Please choose a game to play (1 = Memory Game, 2 = Guess Game, 3 = Currency Roulette):\n"
                 "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
                 "2. Guess Game - guess a number and see if you chose like the computer.\n"
                 "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                 "Type 'q' to exit or 'u' to change Username\n")
    while str(game) != 'q':
        try:
            if str(game) == 'q':
                return game
            elif str(game) == 'u':
                welcome()
                start_play()
                return game
            elif int(game) > 3 or int(game) == 0:
                print("Invalid number\n"
                      "Please choose a number between 1-3\n"
                      "Type 'q' to exit or 'u' to change Username\n")
                start_play()
                return game
            else:
                difficulty_menu()
                return game
        except ValueError:
            print("***ERROR***\n"
                  "Please choose a number between 1-3\n"
                  "Type 'q' to exit or '*' for game menu\n")
            start_play()
            return game
    print("Thank you for playing, Goodbye")
