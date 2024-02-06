import sys


def main():
    calculator_supported()
    while True:
        user_input = input('Enter an arithmetic expression: \n').strip().lower()
        if input_eval(user_input):
            answer = arithmetic_eval(user_input)
            if type(answer) == int:
                print("The answer to your expression is:", answer, '\n')
            else:
                print(f"{answer}\nPlease double check your arithmethic expression""")
        else:
            print('Please double check your arithmethic expression')


def input_eval(user_input):
    safe_chars = set("0123456789/*-+()%")
    if user_input.lower() == 'off':
        sys.exit("Goodbye!!\nLet's do more math next time.")
    elif user_input == '':
        return False
    elif any(i not in safe_chars for i in user_input):
        return False
    else:
        return True
        


def arithmetic_eval(input):
    try:
        return eval(input)    
    except(ZeroDivisionError):
        return 'Cannot divide by zero'
    except(TypeError, SyntaxError, Exception ):
        return "Cannot evaluate expression"
 

def calculator_supported():
    print("WELCOME TO THE SIMPLE ARITHMETIC CALCULATOR\n")
    print("""This calculator supports the following operations:\n
+ Addition (returns sum of given integers).
- Subtraction (returns the difference between integers).
* Multiplication (returns the repeated addition of integers of equal sizes).
/ Division (returns the sharing of an integer into equal-sized groups).
% Modulus (returns the remainder or signed remainder of a division)
Off - Switches the calculator off and terminates the program\n""")


if __name__ == "__main__":
    main()

