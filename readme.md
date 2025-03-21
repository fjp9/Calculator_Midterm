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
4. Create a .env file in the root folder and create the following variables:
    ```sh
    ENVIRONMENT= DEVELOPMENT
    HISTORY_FILEPATH= ./data/history.csv
    ```
    The ENVIRONMENT variable can be set to either DEVELOPMENT, TESTING, or PRODUCTION.
    The HISTORY_FILEPATH recommended value is ./data/history.csv but may be changed if the user would like to export their history to a different location.

## Usage
In the project directory use the command `python main.py` to enter the program. Then enter one of the listed commands below.

### Features
This project uses a plugin architecture. The following are the current list of command plugins. 
- add: Adds two numbers
- clear: Clears the history stored in memory
- delete: delete one of the history records stored in memory
- divide: Divides two numbers
- exit: exits the REPL
- history: displays the history of calculations stored in memory
- load: loads history from the file path designated in the HISTORY_FILEPATH environment variable
- menu: Lists loaded plugins
- multiply: Multiplies two numbers
- save: saves the current history into the file path designated in the HISTORY_FILEPATH environment variable (This command will override any previously stored file)
- subtract: Subtracts two numbers

### Examples
The following are some examples of how to use the above commands:
```
$ python main.py
>>> add
Enter two numbers separated by space: 2 2
The result of 2 add 2 is equal to 4
```
```
$ python main.py
>>> subtract
Enter two numbers separated by space: 2 2
The result of 2 subtract 2 is equal to 0
```

## Testing
When pushing to `main` and the `gitHubActions` branches GitHubActions will run `pytest --pylint --cov`. `pytest` will run tests in the tests folder.

## Design Methodology  

### "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) Implementation
The divide function implements a "Look Before You Leap" (LBYL) design strategy. In the [following function](calculator/operations.py) the program check to ensure the user is dividing by a valid number and then if not the program will return a cannot divide by zero error.  
```python
def divide(a: Decimal, b: Decimal) -> Decimal:
if b == 0:
    raise ValueError("Cannot divide by zero")
return a / b
```

The AddCommand class implements a "Easier to Ask for Forgiveness than Permission" (EAFP) design strategy. [In this case](app/plugins/add/__init__.py) we expect the user to be able to follow the instructions on the screen but in the case they do not the program handles the incorrect input and informs the user that they have made a mistake.
```python
class AddCommand(Command):
def execute(self):
    try:
        a, b = input("Enter two numbers separated by space: ").split()
        logging.info(f"Add command called with {a} and {b}")
        CommandHandler.calculate_and_print(a, b, 'add')
    except ValueError:
        print("Please enter two numbers separated by space.")
        logging.error("Invalid input.")
    return
```

### Design Patterns

#### Facade Pattern
```calculator.calculations``` uses a Facade design pattern to offer a simple interface for any Pandas data manipulation. Each of the methods in the Calculations class use a set of Pandas methods to manipulate the data to perform a specific task. These methods in the Calculations class can then be used within their respective commands to easily perform the data manipulation. This leave the code within the command very easy to read and understand what the intent of the command is. Avoiding the designer to have to decipher what purpose of data manipulation is.

Here is where the Facade Pattern is implemented: [calculations.py](calculator/calculations.py)

#### Command Pattern
The command pattern is implemented in this app to make a easy to use user interface to interact with the calculator. This also allows for the designer to follow the Single Responsibility Principle. Ensuring that each class is only responsible for solving one problem. Each new command can be introduced to solve a new problem. It also aligns with Open/Closed Principle since we can load the commands using a plugin structure allowing the designer to seamlessly create new functionality for the program without modifying existing code.

The [add](app/plugins/add/__init__.py) command is a example of a plugin used for the command pattern.

#### Factory Method
`calculator.calculation.create` is the factory method for the Calculation class. Using this method we can easily create new instances of the Calculation class as needed.

[calculation.py](calculator/calculation.py) is where the factory method for the Calculation class is located.

#### Environment Variables
To manage the location of their history csv file the user must specify a file location in their `.env` file. This allows each user to modify the functionally of the program without having to modify the code within the function itself.

The [load](app/plugins/load/__init__.py) command makes use of the HISTORY_FILEPATH environment variable to load saved history from a csv file.

#### Logging
In this program logging is used to provide insight as to what is happening behind the scenes. This allows the developer to monitor the program for abnormal behavior. A very useful case where logging has been implemented is when loading the plugins. [Here](app/__init__.py) logging lets the developer know what plugins have been loaded into the program. This can help if experiencing unexpected behavior. There my be an instance where a command that the developer is calling is returning a logging error stating that the command does not exist. Then the developer sees that the command has been loaded through the logging.info message. This means they can narrow down where to look to fix the bug and hopefully resolve the issue much faster.

## Video Demonstration

https://github.com/user-attachments/assets/2daa38c2-f72d-41f9-8bf4-c8321835c4ec
