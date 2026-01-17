import random

ANSWERS = [
    "It is certain",
    "It is decidedly so",
    "Yes",
    "Not sure about that",
    "Ask again later",
    "Definitely maybe",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]

def get_answer(answer_number: int) -> str:
    return ANSWERS[answer_number - 1]

input("Make a wish:\n> ")

while True:
    try:
        i = int(input("Now input an integer from 1 to 9:\n> "))
        if 1 <= i <= 9:
            break
        print("Wrong input, try again (must be 1..9).")
    except ValueError:
        print("That wasn't an integer, try again.")

r = random.randint(1, i)
print(get_answer(r))
