from random import randint


def user_input():
    """Takes the number form the user.
    In loop until user gives integer.
    :return: Result as an integer.
    """
    while True:
        try:
            number = int(input("Enter your nuber:"))
            break
        except ValueError:
            print("It's not a natural number!")
    return number


def user_list():
    """Takes 6 nuber from another function.
    in the loop until he receives a lotto-compatible combination.
    :return: List of 6 integers.
    """
    combination = []
    while len(combination) < 6:
        number = user_input()
        if number >= 50 or number <= 0:
            print("Nuber out of range!")
        elif number in combination:
            print("Don't use same number twice!")

        else:
            combination.append(number)
    return sorted(combination)


def lotto():
    """Main function of lotto lottery program """
    print("Welcome to LOTTO!")
    user_numbers = user_list()
    lotto_numbers_list = list(range(1, 49 + 1))
    winner_numbers = []
    user_score = 0

    for i in range(6):
        random_index = randint(0, 49 - i)
        winner_numbers.append(lotto_numbers_list[random_index])
    winner_numbers.sort()
    for number in user_numbers:
        if number in winner_numbers:
            user_score += 1
    print(f'These are your numbers: {user_numbers}')
    print(f"It's a winning combination: {winner_numbers}")
    print(f"Your score: {user_score}/6")


if __name__ == '__main__':
    lotto()
