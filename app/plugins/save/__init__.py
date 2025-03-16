import logging
from app.commands import Command
from app import App
from calculator.calculations import Calculations
import os

class SaveCommand(Command):
    def execute(self, test_filepath=None):
        file_location = test_filepath or os.getenv('HISTORY_FILEPATH')
        if file_location:
            Calculations.save_history(file_location)
            logging.info(f"History saved to {file_location}")
            print(f"History saved successfully to {file_location}")
        else:
            logging.error("HISTORY_FILEPATH is not set in the environment variables.")