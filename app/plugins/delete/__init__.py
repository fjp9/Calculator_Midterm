import logging
from app.commands import Command
from calculator.calculations import Calculations


class DeleteCommand(Command):
    def execute(self):
        history = Calculations.get_history()
        if not history.empty:
            print(history)
            row = int(input("Enter the row number to delete: "))
            logging.info(f"History index {history.iloc[row]} deleted.")
            Calculations.delete_record(row)
            print(f"History index {row} deleted.")
        else:
            print("No history to delete.")
        return