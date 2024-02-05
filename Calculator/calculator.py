import sys


def main():
    calculator_supported()
    while True:
        user_input = input('Enter an arithmetic expression: \n').strip().lower()
        if input_eval(user_input):
            answer = arithmetic_eval(user_input)
            print("The answer to your expression is:", answer, '\n')

def input_eval(user_input):
    safe_chars = set("0123456789/*-+()")
    # user_input = input('Enter an arithmetic expression: ').strip().lower()
    if user_input.lower() == 'off':
        sys.exit("Goodbye!!\nLet's do more math next time.")
    elif user_input == '':
        return False
    elif any(i not in safe_chars for i in user_input):
        # user_input = input('Enter an arithmetic expression: ').strip().lower()
        return False
    else:
        return True
        


def arithmetic_eval(input):
    try:
        return eval(input)
    except (NameError, TypeError, SyntaxError,\
             ZeroDivisionError, Exception) as error:
        
        print(f""""An Error occured: {error}\n\
Please double check your arithmethic expression""")


# arithmetic_eval("input/0")
def calculator_supported():
    print("WELCOME TO THE SIMPLE ARITHMETIC CALCULATOR\n")
    print("""This calculator supports the following operations:\n
+ Addition (returns sum of given integers).
- Subtraction (returns the difference between integers).
* Multiplication (returns the repeated addition of integers of equal sizes).
/ Division (returns the sharing of an integer into equal-sized groups).
% Modulus (returns the remainder or signed remainder of a division)
Off - Switches the calculator off and terminates the program""")


# if __name__ == "__main__":
#     main()

print(arithmetic_eval('5+p'))