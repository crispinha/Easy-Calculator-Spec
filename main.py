#Under the latest version of the MIT licence as of the 15th of Janurary, 2016.
#Program written by Crispin Hitchings-Anstice

print("Calculator")

print("Enter one of 'add', 'subtract', 'multiply', or 'divide'.")
operationType = input('> ')

print("Please put in your first number to be operated on.")
num1 = int(input('> '))
print("Please put in your second number to be operated on.")
num2 = int(input('> '))

if operationType == "add":
    #Adding Code
    result = num1 + num2
    print("Your final number is " + str(result))
elif operationType == "subtract":
    #Subtracting Code
    result = num1 - num2
    print("Your final number is " + str(result))
elif operationType == "multiply":
    #Multplication Code
    result = num1 * num2
    print("Your final number is " + str(result))
elif operationType == "divide":
    #Division Code
    result = num1 / num2
    print("Your final number is " + str(result))
else:
    print("Please put in a proper operation type")
