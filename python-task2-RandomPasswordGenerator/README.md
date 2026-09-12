# Random Password Generator

A customizable, command-line random password generator built using Python. The application generates secure passwords based on user-specified criteria, including length and character variety.

## Features

* **Custom Password Length:** Allows users to set a preferred length, enforcing a minimum of 8 characters.
* **Flexible Character Types:** Supports uppercase letters, lowercase letters, numbers, and symbols (enforces selecting at least two types).
* **Input Validation:** Handles non-numeric inputs and enforces criteria requirements with clear error prompts.
* **Repeat Option:** Allows generating additional passwords without needing to restart the program.

## Tech Stack

* Python 3
* `random` module
* `string` module

## How to Run

1. Ensure Python is installed on your system.
2. Open a terminal or command prompt in the project directory.
3. Run the script:
   ```bash
   python password.py