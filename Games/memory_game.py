import random
import time
from time import sleep
import app


def generate_sequence(difficulty):
    global num_list
    num_list = random.sample(range(1, 100), int(difficulty))
    for i in range(len(num_list)):
        num_list[i] = str(num_list[i])


def print_and_delete(list, duration):
    print("Pay attention and try to remember the following number\\s")
    sleep(0.7)
    print(list, end='', flush=True)  # Print the message immediately without newline
    time.sleep(duration)  # Wait for the specified duration
    print('\r' + ' ' * len(list), end='', flush=True)  # Clear the output


def get_list_from_user(difficulty):
    global user_list
    input_string = (input("Enter " + str(difficulty) + " number\\s between 1-100 separated by space\n"
                          "Press '*' to go back to game menu\n"))
    if str(input_string) == '*':
        app.start_play()
        return input_string
    else:
        user_list = input_string.split()
        is_list_equal()
        if result is True:
            return True
        else:
            return False


def is_list_equal():
    global result
    if str(num_list) == str(user_list):
        print("Success")
        result = True
    else:
        print("Incorrect")
        result = False


def play(difficulty):
    generate_sequence(difficulty)
    print_and_delete(num_list, 0.7)
    get_list_from_user(difficulty)
