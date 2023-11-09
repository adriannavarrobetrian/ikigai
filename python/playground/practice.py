"""
This module contains a function to convert a decimal
number to octal using print() output formatting.
"""
def decimal_to_octal():
    """
    Converts a decimal number to octal using print() output formatting.
    
    Prompts the user to enter a decimal number, converts it to octal, and
    prints the result using the print() function...
    """
    decimal_number = int(input("Enter a decimal number: "))
    octal_number = oct(decimal_number)
    print("The octal value of", decimal_number, "is", octal_number[2:])


if __name__ == '__main__':
    decimal_to_octal()
