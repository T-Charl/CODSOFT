import re
from random import choice
from string import ascii_letters, digits, punctuation, ascii_lowercase

"""
Program that provides a randomly generated password based on the length and
complexity as provided by the user. """


def main():
    """
    Entry fucntion that gets password length from the user and passes it in
    the generate password function and prints the password
    """
    length = get_password_length()
    complexity = get_password_complexity()
    password = generate_password(length, complexity)
    print(f"Your randomly generated password is {password}")


def get_password_complexity() -> str:
    """
    Function that ask user to specifiy the complexity of the password to be
    generated

     :returns:
    - 'Easy' (str): for easy password.
    - 'Medium' (str): for medium complec password.
    - 'Extreme' (str): for extremely complex password
    """

    options = ["Easy", "Medium", "Extreme"]

    while True:
        complexity = input(
            """How complex should your passwords be?
1 - Easy
2 - Medium 
3 - Extreme
"""
        )
        if complexity.capitalize() in options:
            return complexity
        else:
            print("""Please selecta valid choice "Easy", "Medium", "Extreme".""")


def get_password_length() -> int:
    """
    Function that asks the user to specify the length of the password and
    checks if the length is a valid integer.

     :return:
    - n (int): integer specifying length of the password
    """

    while True:
        try:
            n = int(input("Provide password length: ").strip())
            if 0 < n <= 25:
                return n
            else:
                print("Please provide an integer between 0 - 25 for password length.")
        except ValueError:
            n = input("Please provide a digit for password length. ")


def generate_password(length: int, complexity: str) -> str:
    """
    Function that assembles password by getting 1 random character at a time
    from the get_character function.

     :param:
    - length (int): length of password.
    - complexity (str): complexity of the password.

     :returns:
    - password (str): randomly generated password.
    """

    password = ""
    for _ in range(length):
        password += get_character(complexity)
    return password


def get_character(complexity: str) -> str:
    """
    Function that randomly chooses one character and returns it. Character
    option availabilty differ based on complexity

     :param:
    - complexity (str): complexity of the password.
     :returns:
    - choice (str): random character
    """

    if complexity.capitalize() == "Easy":
        return choice(ascii_lowercase)
    elif complexity.capitalize() == "Medium":
        return choice(ascii_letters)  # if randint(0, 1) == 0 else str(randint(0, 9))
    elif complexity.capitalize() == "Extreme":
        return choice(ascii_letters + digits + punctuation)


# def generate_password(n):
#     """
#     Function that randomly generates password based on user specified length
#     and complexity.

#      :param:
#     - n (int): length of the password

#       :returns:
#     - password (str): randomly generated password
#     """

#     complexity = get_password_complexity()
#     char = ascii_letters + digits + punctuation
#     characters = re.sub(r"a?e?i?o?u?\[?\]?\(?\)?\{?\}?,?;?`?", "", char)
#     password = ""
#     while len(password) != n:
#         if complexity.capitalize() == "Easy":
#             char_choice = choice(ascii_lowercase)

#         elif complexity.capitalize() == "Medium":
#             char_choice = choice(ascii_letters)
#             if len(password) == n - 1:
#                 return password + str(randint(0, 9))

#         elif complexity.capitalize() == "Extreme":
#             char_choice = choice(characters)

#         if char_choice not in password:
#             password += char_choice
#     return password


if __name__ == "__main__":
    main()
