import sys

def error_message(message: str):
    print(f"AssertionError: {message}")

if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
        print(f"I'm Even.") if number % 2 == 0 else print(f"I'm Odd.")
    except ValueError:
        error_message("argument is not an integer")
        sys.exit(1)
else:
    error_message("more than one argument are provided")
    sys.exit(1)