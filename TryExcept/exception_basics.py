# 1. ValueError Example
try:
    num = int("abc")
except ValueError:
    print("ValueError: Can't convert to integer.")
finally:
    print("Let's try another one...\n")

# 2. NameError Example
try:
    print(undeclared_variable)
except NameError:
    print("NameError: Variable is not defined.")
finally:
    print("Let's try another one...\n")

# 3. TypeError Example
try:
    result = "Number: " + 10
except TypeError:
    print("TypeError: Can't concatenate string with integer.")
finally:
    print("Let's try another one...\n")

# 4. SyntaxError Example
try:
    exec("if True print('Hello')")
except SyntaxError:
    print("SyntaxError: Invalid syntax.")
finally:
    print("Let's try another one...\n")
