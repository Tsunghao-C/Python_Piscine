import sys

def atoi(s: str) -> int:
    if not s:
        return 0
    # equals to escaping leading white spaces
    s = s.strip()
    if not s:
        return 0
    num = 0
    index = 0
    sign = 1
    if s[index] == '-' or s[index] == '+':
        if s[index] == '-':
            sign = sign * -1
        index += 1
    while (index < len(s) and s[index].isdigit()):
        num = num * 10 + int(s[index])
        index += 1
    return num * sign

def is_integer(s: str) -> bool:
    if not s:
        return False
    s = s.strip()
    if not s:
        return False
    index = 0
    if (s[index] == '-' or s[index] == '+'):
        index += 1
    while (index < len(s)):
        if not s[index].isdigit():
            return False
        index += 1
    return True
if (len(sys.argv) == 1):
    print("")
elif (len(sys.argv) - 1 > 1):
    print("AssertionError: more than one argument is provided")
elif (is_integer(sys.argv[1]) == False):
    print("AssertionError: argument is not an integer")
elif (atoi(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")