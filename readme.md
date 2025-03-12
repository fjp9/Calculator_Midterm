# Midterm Project

## Overview
This project is part of the IS601 course midterm assignment. The goal is to demonstrate the skills and knowledge acquired throughout the course.

## Requirements
- Python 3.8+
- Any necessary libraries (listed in `requirements.txt`)

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/fjp9/Calculator_Midterm
    ```
2. Navigate to the project directory:
    ```sh
    cd Calculator_Midterm
    ```
3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
In the project directory use the command `python main.py` to enter the program. Then enter one of the listed commands below.

## Features
This project uses a plugin architecture. The following are the current list of command plugins. 
- add: Adds two numbers
- subtract: Subtracts two numbers
- divide: Divides two numbers
- multiply: Multiplies two numbers
- menu: Lists loaded plugins
- exit: Exits the program 

## Testing
When pushing to `main` and the `gitHubActions` branches GitHubActions will run `pytest --pylint --cov`. `pytest` will run tests in the tests folder.