import sys


def error_message(message: str):

    print(f"AssertionError: {message}")


def punctuation_marks(char: str) -> bool:

    return char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


class Building:

    def __init__(self, string: str):
        self.string = string
        self.string_counter()

    def string_counter(self):
        upercase_letters = 0
        lowercase_letters = 0
        punctuation = 0
        spaces = 0
        digits = 0
        length = len(self.string)

        for char in self.string:
            if punctuation_marks(char):
                punctuation += 1
            elif char.isupper():
                upercase_letters += 1
            elif char.islower():
                lowercase_letters += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1

        self.upercase_letters = upercase_letters
        self.lowercase_letters = lowercase_letters
        self.punctuation = punctuation
        self.spaces = spaces
        self.digits = digits
        self.length = length
        return True

    def print_building(self):
        print(f"The test Contains {self.length} characters:")
        print(f"Upercase letters: {self.upercase_letters}")
        print(f"Lowercase letters: {self.lowercase_letters}")
        print(f"Punctuation: {self.punctuation}")
        print(f"Spaces: {self.spaces}")
        print(f"Digits: {self.digits}")
        return True


def main():
    if len(sys.argv) == 1:
        try:
            input_string = input("Enter a string: ")
            building = Building(input_string)
            building.print_building()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt")
            sys.exit(1)
        except EOFError:
            print("\nEOF")
            sys.exit(1)
        except Exception as e:
            error_message(e)
            sys.exit(1)
    elif len(sys.argv) == 2:
        try:
            building = Building(sys.argv[1])
            building.print_building()
        except Exception as e:
            error_message(e)
            sys.exit(1)
    else:
        error_message("Too many arguments")
        sys.exit(1)


if __name__ == "__main__":

    main()
