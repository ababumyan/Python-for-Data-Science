import sys


def char_to_morse(char: str) -> str:
    """ Convert a character to its Morse code representation """
    nested_morse = {
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
        "7": "--..",
        "8": "--...",
        "9": "----.",
        "0": "-----",
        " ": "/"

    }
    return nested_morse.get(char, None)


def sos(string: str) -> str:
    """ Convert a string to its Morse code representation """
    result = ""
    for char in string:
        if char.isalpha():
            result += char_to_morse(char.upper()) + " "
        elif char.isdigit():
            result += char_to_morse(char) + " "
        elif char.isspace():
            result += "/" + " "
        else:
            return None
    return result


def main():
    if len(sys.argv) == 2:
        res = sos(sys.argv[1])
        print(res) if res else print("AssertionError: the arguments are bad")
        sys.exit(1)
    else:
        print("AssertionError: the arguments are bad")
        sys.exit(1)


if __name__ == "__main__":
    main()
