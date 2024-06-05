import random
import time
from time import sleep
import app
from Scores.score import add_score
from Scores import utils


def generate_sequence(difficulty):
    num_list = random.sample(range(2, 102), int(difficulty))
    num_list = [str(num) for num in num_list]
    return num_list


# def print_and_delete(numbers, duration):
#     print("Pay attention and try to remember the following number\\s")
#     sleep(0.7)
#     print(numbers, end='', flush=True)  # Print the message immediately without newline
#     time.sleep(duration)  # Wait for the specified duration
#     print('\r' + ' ' * len(numbers), end='', flush=True)  # Clear the output

def print_and_delete(numbers, duration):
    print("Pay attention and try to remember the following number\\s")
    sleep(0.7)
    print(' '.join(numbers))
    time.sleep(duration)
    utils.screen_cleaner()


def get_list_from_user(difficulty, num_list):
    input_string = (input(f"Enter {difficulty} number\\s between 1-100 separated by space\n"
                          "Press '*' to go back to game menu\n"))
    if input_string == '*':
        app.start_play()
        return '*', False
    else:
        user_list = input_string.split()
        return input_string, is_list_equal(num_list, user_list)


def is_list_equal(num_list, user_list):
    if num_list == user_list:
        return True
    else:
        return False


def play(difficulty):
    num_list = generate_sequence(difficulty)
    print_and_delete(num_list, 0.7)
    user_input, result = get_list_from_user(difficulty, num_list)
    if result:
        add_score(difficulty)
        print("Success")
    else:
        print("Incorrect")
