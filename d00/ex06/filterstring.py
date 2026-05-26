import sys


def error_message(message: str):
    """ Print an error message """
    print(f"AssertionError: {message}")


def filter_string(string: str, n: int):
    """ Filter the string using the length of the words """
    return [word for word in string.split() if len(word) > n]


def main():
    if len(sys.argv) == 3:
        try:
            string = sys.argv[1]
            n = int(sys.argv[2])
            print(filter_string(string, n))
        except ValueError:
            error_message("the arguments are bad")
            sys.exit(1)
    else:
        error_message("the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
