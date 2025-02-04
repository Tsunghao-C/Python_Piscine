import sys
# from ft_filter import ft_filter


def is_integer(s: str) -> bool:
    '''Return true if s is integer'''
    try:
        int(s)
        return True
    except ValueError:
        return False


def main():
    if len(sys.argv) - 1 != 2:
        print("AssertionError: the arguments are bad")
        return 1
    elif type(sys.argv[1]).__name__ != "str" or not is_integer(sys.argv[2]):
        print("AssertionError: the arguments are bad")
        return 1
    else:
        len_limit = int(sys.argv[2])
        str_list = sys.argv[1].split()
        # Using ft_filter
        # output = list(ft_filter(lambda x: len(x) > len_limit, str_list))
        # print(output)
        # Using both lamda and list comprehension
        output2 = [x for x in str_list if (lambda s: len(s) > len_limit)(x)]
        print(output2)
    return 0


if __name__ == "__main__":
    main()
