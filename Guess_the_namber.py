from random import randint


def user_input():
    """Takes the number form the user.
    In loop until user gives integer.
    :return: Result as an integer.
    """
    while True:
        try:
            result = int(input("Guess the number: "))
            return result
        except ValueError:
            print("It,s not a number!")


def guess_the_number():
    """ Program where user guess generated number"""
    drawn_number = randint(1, 100)
    while True:
        user_answer = user_input()
        if user_answer == drawn_number:
            print('You win!')
            break
        elif user_answer < drawn_number:
            print("To small!")
            continue
        else:
            print("To big!")
            continue


if __name__ == '__main__':
    guess_the_number()
