import logging
from app.commands import Command
from calculator.calculations import Calculations


class HistoryCommand(Command):
    def execute(self):
        logging.info("History command called.")
        history = Calculations.get_history()
        if not history.empty:
            print(history)
        else:
            print("No history to display.")
        return