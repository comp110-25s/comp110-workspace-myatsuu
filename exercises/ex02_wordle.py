"""Wordle Exercise"""

__author__ = "730677063"


def contains_char(searched_word: str, char_in_searched: str) -> bool:
    """looking for certain char"""
    assert len(char_in_searched) == 1, f"(len'{char_in_searched}') is not 1"
    count: int = 0
    # this will see if the letter used is in the word we want
    while count < len(searched_word):
        if searched_word[count] == char_in_searched:
            return True
        else:
            count = count + 1

    return False


def emojified(guess: str, secret: str) -> str:
    """first a guess and second a secret"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    # this is for recognizing a letter with a colored box on whether its right or not
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    result: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret, guess[idx]):
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX

        idx = idx + 1

    return result


# this is for guessing if the word has the right amount of letters
def input_guess(expected_l_guess: int) -> str:
    """expected length int of a guess"""
    n: str = input(f"Enter a {expected_l_guess} character word:")
    while len(n) != expected_l_guess:
        n = input(f"That wasn't {expected_l_guess} chars! Try again:")

    return n


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # these are the variables for the state of the game that im using
    n: int = 1
    state_1: bool = False
    end_word: str = "codes"
    # this is the game starting
    while n <= 6 and state_1 is False:
        print(f"=== Turn {n}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, end_word))

        if guess == end_word:
            state_1 = True
        else:
            n = n + 1
    # this is when the game ends and if the user has won or lost
    if state_1:
        print(f"You won in {n}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomrrow!")


if __name__ == "__main__":
    main(secret="codes")
