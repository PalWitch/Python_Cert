######################
# Exception Handling #
######################
'''NIEMALS BaseExceptions fangen!'''

# ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Fehler: {e}")  # Fehler: division by zero

# IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"Fehler: {e}")  # Fehler: list index out of range

# KeyError
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
except KeyError as e:
    print(f"Fehler: {e}")  # Fehler: 'c'

# ValueError
try:
    num = int("abc")
except ValueError as e:
    print(f"Fehler: {e}")  # Fehler: invalid literal for int() with base 10: 'abc'

# TypeError
try:
    result = "5" + 3
except TypeError as e:
    print(f"Fehler: {e}")  # Fehler: can only concatenate str (not "int") to str

# FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Fehler: {e}")  # Fehler: [Errno 2] No such file or directory: 'non_existent_file.txt'