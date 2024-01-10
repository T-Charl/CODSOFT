

# Random Password Generator

This Python program generates a randomly generated password based on 
user-specified length and complexity. It provides a flexible approach to 
password creation, allowing users to customize the length and complexity 
of their passwords.

## Features

- **Password Complexity Levels:**
  - **Easy:** Lowercase alphabetic characters only.
  - **Medium:** Alphabetic characters (both uppercase and lowercase).
  - **Extreme:** Alphanumeric characters (both uppercase and lowercase) with special symbols.

- **User Input Validation:** The program ensures that user inputs are valid, guiding users to make appropriate choices for password complexity and length.

## Usage

1. Run the program by executing the `main()` function.
2. Provide the desired password length.
3. Specify the desired complexity level (Easy, Medium, or Extreme).
4. Receive a randomly generated password based on your specifications.

## Example

```python
# Run the program
if __name__ == "__main__":
    main()
```

## Functions

### `get_password_length() -> int`

Asks the user to specify the length of the password and checks if the length 
is a valid positive integer.

### `get_password_complexity() -> str`

Asks the user to specify the complexity of the password to be generated.

### `generate_password(length: int, complexity: str) -> str`

Assembles a password by getting one random character at a time from the 
`get_character()` function.

### `get_character(complexity: str) -> str`

Randomly chooses one character based on the specified complexity level.

## License

