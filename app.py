from Games import guess_game, currency_roulette, memory_game


def welcome():
    while True:
        username = input("Enter Username\n")
        if 4 <= len(username) <= 12:
            print(f"Hi {username} and welcome to the World Of Games: The Epic Journey")
            return username
        else:
            print("Username must be between 4-12 characters")


def difficulty_menu():
    while True:
        difficulty = input("Please select difficulty level between 1-5\nType 'q' to exit or '*' for game menu\n")
        if difficulty == 'q':
            print("Thank you for playing, Goodbye")
            return difficulty
        elif difficulty == '*':
            return difficulty
        elif difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            return int(difficulty)
        else:
            print("Invalid input, please enter a number between 1 and 5, 'q' to exit, or '*' for game menu\n")


def start_play():
    while True:
        game = input("Please choose a game to play (1 = Memory Game, 2 = Guess Game, 3 = Currency Roulette):\n"
                     "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
                     "2. Guess Game - guess a number and see if you chose like the computer.\n"
                     "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
                     "Type 'q' to exit or 'u' to change Username\n")
        if game == 'q':
            print("Thank you for playing, Goodbye")
            return
        elif game == 'u':
            welcome()
            continue
        elif game.isdigit() and 1 <= int(game) <= 3:
            game = int(game)
            while True:
                difficulty = difficulty_menu()
                if difficulty == 'q':
                    return
                elif difficulty == '*':
                    break
                else:
                    if game == 1:
                        memory_game.play(difficulty)
                    elif game == 2:
                        guess_game.play(difficulty)
                    elif game == 3:
                        currency_roulette.play(difficulty)
                    return game
        else:
            print("Invalid input, please enter a number between 1-3, 'q' to exit, or 'u' to change Username\n")

