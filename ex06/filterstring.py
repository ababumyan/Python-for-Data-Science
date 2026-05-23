""" Part 2: The program
Create a program that accepts two arguments: a string (S) and an integer (N). The
program should output a list of words from S that have a length greater than N.
• Words are separated from each other by space characters.
• Strings do not contain any special characters (punctuation or invisible).
• The program must contain at least one list comprehension expression and one
lambda.
• If the number of arguments is different from 2, or if the type of any argument is wrong,
the program prints an AssertionError.
Expected outputs:
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
$> python filterstring.py 'Hello the World' 99
[]
$>
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
$> python filterstring.py
AssertionError: the arguments are bad """


import sys
def error_message(message: str):
    print(f"AssertionError: {message}")

def filter_string(string: str, n: int):
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