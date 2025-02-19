import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"
}


def main():
    """
    Returns input string into Morse Code.
    """
    try:
        if len(sys.argv) - 1 != 1 or not sys.argv[1].isalnum():
            raise AssertionError("the arguments are bad")
        string = sys.argv[1]
        list_code = [NESTED_MORSE[str(x).upper()] for x in string]
        # Use "*" the unpacking operator to unpack a list object into \
        # separate arguments
        print(*list_code)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
