#Author-Ryan Rinvil
def greeting():
    """
    This function prints 'Hello World' on one line.
    """
    print("Hello World!")
    return greeting.__doc__

greeting()

print(greeting())
# Test cases
# Test case 1: Verify that the function returns the docstring
# Test case 2: Verify the return value matches the docstring
# Test case 3: Verify the function prints "Hello World!"
# Test case 4: Verify the function works

