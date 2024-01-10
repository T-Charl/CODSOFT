import random

def password_parameters():
    length = input("Specifiy password character length: ").strip().lower()
    complexity = input("Specify password complexity ('Easy', 'Medium', 'Hard')").strip().lower()