import sys


def char_count(s: str):
    '''Iterate through input strings and calculate the counts of
    uppercase, lowercase, punctuation marks, spaces, and digits.'''
    if not s:
        return None
    index = 0
    upper = 0
    lower = 0
    punc = 0
    space = 0
    digit = 0
    while (index < len(s)):
        if s[index].isupper():
            upper += 1
        elif s[index].islower():
            lower += 1
        elif s[index].isdigit():
            digit += 1
        elif s[index].isspace():
            space += 1
        else:
            punc += 1
        index += 1
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    if len(sys.argv) == 1:
        print("What is the text to count?")
        input_str = sys.stdin.readline()
    elif len(sys.argv) - 1 > 1:
        print("AssertionError: more than one argument is provided")
        return 1
    else:
        input_str = sys.argv[1]
    print(f"The text contains {len(input_str)} characters:")
    char_count(input_str)
    # print(char_count.__doc__)
    # help(char_count)
    return 0


if __name__ == "__main__":
    main()
