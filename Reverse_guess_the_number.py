def program_menu():
    """Menu information of the program"""
    print("""Think about number between 0 to 1000 \nand I will guess it in max 10 tries.""")
    print("""Use this command to interact with program:
    1. If the answer is smaller: 'Too small',
    2. If answer is bigger: 'Too big',
    3. If answer is correct: 'You won'.
    """)


def guess_the_number():
    """Program that guesses the nuber of user"""
    program_menu()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you won":
        guess = int((max_number - min_number) / 2) + min_number
        print(f"Your number is {guess}?")
        user_answer = input("Give me some clue:")
        user_answer = user_answer.casefold()
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess
        elif user_answer == "you won":
            print("I win!")
        else:
            print("Don't cheat!")


if __name__ == '__main__':
    guess_the_number()
