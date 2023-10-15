
def calculate_factorial(n): #recursively calculates the factorial of a given number.
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

if __name__ == '__main__': #block, we take user input for the number for which the factorial needs to be calculated.
    try:
        number = int(input("Enter a number to calculate its factorial: ")) 
        if number < 0:
            print("Factorial is not defined for negative numbers.") #where the user enters a negative number or a non-integer input. 
        else: ##calculate and print the factorial of the input number.
            result = calculate_factorial(number)
            print(f"{number}! = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
