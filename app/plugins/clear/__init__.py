import logging
from app.commands import Command
from calculator.calculations import Calculations


class ClearCommand(Command):
    def execute(self):
        logging.info("Clear command called.")
        Calculations.clear_history()
        print("History cleared.")
        return