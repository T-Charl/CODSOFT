import sys
from typing import Tuple
from random import choice

"""
Program that allows users to play rock paper scissors game against the computer.
Game allows users the option to play a set number of rounds (number of games) or
alternatively input how many rounds they would like to play. When playing more 
than 1 game the user can request to view how many games they have played thus 
far and what the results of those games are.
"""


def main():
    """
    Entry function that starts the program and executes commands to bring in
    the defined helper functions and play the game
    """

    draw, win, lose = 0, 0, 0
    rules()
    while True:
        option = input("Enter Game option: ").strip().lower()
        if option in ["exit", "done", "quit"]:
            sys.exit("Thank you for playing.\nLet's play again soon.\n")
        elif option == "tally":
            tally(draw, win, lose)
        elif option == "rules":
            rules()
        elif option == "1":
            best_of_n(draw, win, lose, 1)
        elif option == "2":
            best_of_n(draw, win, lose, 3)
        elif option == "3":
            my_choice(draw, win, lose)
        elif option == "4":
            print("Let's play to your heart's content\n")
            while True:
                draw, win, lose = game(draw, win, lose)
        print(
            """Please enter a game option.
Alternatively type 'Rules' to view options. \n"""
        )


def computer_choice() -> str:
    """
    Function that uses the random module to select a choice for the computer'

     :returns:
    - computer_choice (str)
    """
    computer_choice = choice(["rock", "paper", "scissors"])
    return computer_choice


def get_user_choice(draw: int, win: int, lose: int) -> str:
    """Function that gets for user choice of rock, paper, or scissors and
    validates it. r, p and s are supported in lieu or the full words. If choice
    is not valid user is re-prompted for choice. Function supports tally functions
    and will exit the program if user inputs any of the exit commands.

     :params:
    - draw (int): number of draws
    - win (int): number of wins
    - lose (int): number of losses

     :return:
    -user_choice (str): valid choice made by user
    """

    user_choice = input("Make a choice, (rock, paper, or scissors): ").strip().lower()
    while True:
        if user_choice in ["exit", "done", "quit"]:
            sys.exit("Thank you for playing.\nLet's play again soon.\n")
        elif user_choice.lower() == "rules":
            rules()
        elif user_choice.lower() == "tally":
            tally(draw, win, lose)
        elif user_choice in ["rock", "paper", "scissors", "r", "p", "s"]:
            if user_choice == "r":
                user_choice = "rock"
            elif user_choice == "p":
                user_choice = "paper"
            elif user_choice == "s":
                user_choice = "scissors"

            return user_choice
        user_choice = (
            input("Make a choice, (rock, paper, or scissors): ").strip().lower()
        )


def determine_winner(user: str, computer: str) -> str:
    """
    Function that compares user choice against computer's and returns the
    winning choice based on the game rules.

     :params:
    -user (str): valid user choice.
    -computer (str): valid computer choice

     :return:
    - both (str) : if choices are equal
    - user (str): if user choice wins
    - comp (str): if computer choice won
    """

    outcomes = {
        ("rock", "scissors"): "user",
        ("rock", "paper"): "comp",
        ("scissors", "paper"): "user",
        ("scissors", "rock"): "comp",
        ("paper", "rock"): "user",
        ("paper", "scissors"): "comp",
    }

    if user == computer:
        return "both"

    return outcomes.get((user, computer))


def results(result: str, user: str, computer: str):
    """
    Function that prints the results of the game.

     :params:
    - result (str): result of choice comparison
    - user (str): user's choice
    - computer (str): computer's choice
    """

    if result == "both":
        print(
            f"DRAW!!!\nYour choice: {user.upper()}\nComputer choice: {computer.upper()}\n"
        )
    elif result == "user":
        print(
            f"You WIN!!!\nYour choice: {user.upper()}\nComputer choice: {computer.upper()}\n"
        )
    else:
        print(
            f"You LOSE!!!\nYour choice: {user.upper()}\nComputer choice: {computer.upper()}\n"
        )


def tally(draw: int, win: int, lose: int):
    """
    Function that tallies up the results of the game when more than one round
    is being played.

     :params:
    - draw (int): number of draws
    - win (int): number of wins
    - lose (int): number of losses
    """

    if (draw, win, lose) == (0, 0, 0):
        return "Pass"
    else:
        print(
            f"""\nPlayed {sum([draw,win,lose])} games
              
Won: {win} 
Losses: {lose} 
Draws: {draw}\n """
        )


def game(draw: int, win: int, lose: int) -> Tuple[int, int, int]:
    """
    Function that calls for computer and user choices and passes them into the
    choice comparison function and updates the draw, win and lose variables.

     :params:
    - draw (int): number of draws
    - win (int): number of wins
    - lose (int): number of losses

     :returns:
    - draw (int): number of draws
    - win (int): number of wins
    - lose (int): number of losses"""

    computer = computer_choice()
    user = get_user_choice(draw, win, lose)
    result = determine_winner(user, computer)
    if result == "both":
        draw += 1
    elif result == "user":
        win += 1
    elif result == "comp":
        lose += 1
    results(result, user, computer)
    return draw, win, lose


def rules():
    """
    Function that prints the game options and rules
    """
    print("\nWelcome to Rock, Paper, Scissors\n")
    print(
        """
The Rules are simply as follows:

Rock beats Scissors, 
Scissors beats Paper, 
Paper beats Rock. 

Game Options:

1 = Single round (1 round, winner takes all).
2 = Best of 3 (2 of 3 wins to be declared winner).
3 = My choice (Specify number or rounds to play)
4 = All day long (Play as many rounds until you want to exit)
Tally = Shows score for games played
Exit = enter any of the following commands:
        'Exit' , 'Done', 'Quit'
"""
    )


def best_of_n(draw: int, win: int, lose: int, n: int):
    """
    Function that plays the game for n amount of rounds and exits the program
    when the number of rounds has been satisfied.

     :params:
    - draw (int): number of draws
    - win (int): number of wins
    - lose (int): number of losses
    - n (int): number of rounds to be played

    """
    for i in range(n):
        print(f"\nGame {i+1}\n")
        draw, win, lose = game(draw, win, lose)
    tally(draw, win, lose)
    sys.exit("Thank you for playing.\nLet's play again soon.\n")


def my_choice(draw, win, lose):
    """
    Function that plays the game for n number of rounds with n being specified
    by the user.

     :params:
    - draw (int): number of draws
    - win (int): number of wins
    - lose (int): number of losses
    """
    rounds = input("How many rounds would you like to play? ").strip()
    while True:
        if rounds.lower() in ["exit", "done", "quit"]:
            sys.exit("Thank you for playing.\nLets play again soon.\n")
        elif rounds.lower() == "rules":
            rules()
        else:
            try:
                n = int(rounds)
                break
            except ValueError:
                if rounds.lower() == "tally":
                    tally(draw, win, lose)
                rounds = input(
                    "Enter a valid number. \nHow many rounds would you like to play? "
                ).strip()
    best_of_n(draw, win, lose, n)


if __name__ == "__main__":
    main()
