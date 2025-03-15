import logging
from app.commands import Command
from app.commands import CommandHandler
from calculator.calculations import Calculations
import os

class LoadCommand(Command):
    def execute(self):
        file_location = './data/history.csv'
        if file_location:
            Calculations.load_history(file_location)
            logging.info(f"History loaded from {file_location}")
            print(f"History loaded successfully from {file_location}")
        else:
            logging.error("HISTORY_FILEPATH is not set in the environment variables.")