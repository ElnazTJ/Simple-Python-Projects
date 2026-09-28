import random
from hangman_words import FRUITS

HANGMAN = {
    0: (
        " ",
        " ",
        " "
    ),
    1: (
        " O ",
        " ",
        " "
    ),
    2: (
        " O ",
        " | ",
        " "
    ),
    3: (
        " O ",
        "/| ",
        " "
    ),
    4: (
        " O ",
        "/|\\",
        " "
    ),
    5: (
        " O ",
        "/|\\",
        "/  "
    ),
    6: (
        " O ",
        "/|\\",
        "/ \\"
    ),
}


def display_hangman(mistakes):
    for line in HANGMAN[mistakes]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    is_running = True
    answer = random.choice(FRUITS)
    mistakes = 0
    hint = ["_"] * len(answer)
    guesses = set()

    while is_running:
        print("------------------")
        display_hangman(mistakes)
        display_hint(hint)
        print("------------------")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess!")
            continue

        if guess in guesses:
            print(f"You have already guessed '{guess}'!")
            continue

        guesses.add(guess)

        found = False

        for i in range(len(answer)):
            if guess == answer[i]:
                hint[i] = guess
                found = True

        if not found:
            mistakes += 1

        if "_" not in hint:
            print("\nYou Won!")
            display_answer(answer)
            is_running = False

        elif mistakes == 6:
            display_hangman(mistakes)
            print("\nYou Lost!")
            print("The word was:")
            display_answer(answer)
            is_running = False


if __name__ == "__main__":
    main()