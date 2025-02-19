import sys
from ft_filter import ft_filter


def main():
    """
    Accept 2 arguemnts:
    1. string
    2. integer

    Returns a list of string whose length is greater than the integer.
    """
    try:
        if len(sys.argv) - 1 != 2:
            raise AssertionError("the arguments are bad")
        num = int(sys.argv[2])
        if not isinstance(sys.argv[1], str) or not isinstance(num, int):
            raise AssertionError("the arguments are bad")
        else:
            str_list = sys.argv[1].split()
            # Using ft_filter
            output = list(ft_filter(lambda x: len(x) > num, str_list))
            # Using both lamda and list comprehension
            # output = [x for x in str_list if (lambda s: len(s) > num)(x)]
            print(output)
    except ValueError as e:
        print("ValueError:", e)
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
