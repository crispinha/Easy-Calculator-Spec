# Easy Calculator Spec #

This will likely be your first project, especially if you are following my guide for starting programming. I will provide in this document the specs to create a simple calculator, various examples of how this program would run, and a Python 3 implementation of this program.

##The Specs##

Your program must take input from the user in three different places.
The first of which is determining which operation the user wishes to perform. The user must pick from 'add', 'subtract', 'multiply', or 'divide', with what each input does fairly self-explanatory. The code **must** describe the error and end the program, as demonstrated below.
The second and third inputs are the two numbers to be entered into the equation. After these inputs are taken, the chosen mathematical operation shall be completed with all the inputs taken into account, and the result displayed to the user.
I understand that my description might be hard to follow, so I recommend looking at the sample program outputs below before you embark on this project.

##Program Output##

A successful output:

       Calculator
    Enter one of 'add', 'subtract', 'multiply', or 'divide'.
    > add
    Please put in your first number to be operated on.
    > 1
    Please put in your second number to be operated on.
    > 3
    Your final number is 4

A failed output:

    Enter one of 'add', 'subtract', 'multiply', or 'divide'.
    > aff
    Please put in your first number to be operated on.
    > 1
    Please put in your second number to be operated on.
    > 3
    Please put in a proper operation type
##Gotchas##

 - Depending on the language used, you might need to convert either the user's input or the end result between strings and numbers to calculate or display them.
 - If you feel like I've missed something, which I probably have, then feel free to open an issue and let me know.

##The Code##
Before I begin this, I'd like to say that this isn't particularly well-written code, both because I wrote it quickly and because I tried to keep it simple. I'd also really recommend that you have a go at writing it yourself before you look at my code, as you'll learn more if you try to do it yourself first. Anyway, onto the code.

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

