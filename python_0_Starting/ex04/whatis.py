import sys


def main():
    '''return what it is'''
    if len(sys.argv) == 1:
        print("")
        exit()
    try:
        try:
            if len(sys.argv) > 2:
                raise AssertionError("more than one argument is provided")
            num = int(sys.argv[1])
            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError("argument is not an integer")
    except AssertionError as e:
        print(f"AssertionError: {str(e)}")
    except Exception as e:
        print(f"Unexpected error - {str(e)}")


if __name__ == "__main__":
    main()
