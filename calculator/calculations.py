import pandas as pd
import logging
from decimal import Decimal
from typing import Callable, List
from calculator.operations import add, subtract, multiply, divide

from calculator.calculation import Calculation

class Calculations:
    history = pd.DataFrame(columns=['a', 'b', 'operation', 'result'])

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        new_entry_data = {
            'a': calculation.a,
            'b': calculation.b,
            'operation': calculation.operation.__name__,
            'result': calculation.perform()
        }
        new_entry = pd.DataFrame([new_entry_data])
        cls.history = pd.concat([cls.history, new_entry], ignore_index=True)

    @classmethod
    def get_history(cls) -> pd.DataFrame:
        display_history = cls.history.copy()
        display_history['operation'] = display_history['operation'].apply(lambda op: op.__name__ if callable(op) else op)
        return display_history


    @classmethod
    def clear_history(cls):
        cls.history = cls.history.iloc[0:0]
    
    @classmethod
    def delete_record(cls, index: int):
        cls.history = cls.history.drop(index)
        cls.history = cls.history.reset_index(drop=True)

    @classmethod
    def get_latest(cls) -> Calculation:
        if not cls.history.empty:
            latest_entry = cls.history.iloc[-1]
            operation = globals()[latest_entry['operation']]
            return Calculation(
                Decimal(latest_entry['a']),
                Decimal(latest_entry['b']),
                operation
            )
        return None
    
    @classmethod
    def save_history(cls, filename: str):
        # Ensure the operation column is stored as strings
        cls.history['operation'] = cls.history['operation'].apply(lambda op: op.__name__ if callable(op) else op)
        cls.history.to_csv(filename, index=False)
    
    @classmethod
    def load_history(cls, filename: str):
        cls.history = pd.read_csv(filename)
        logging.info(f"History loaded:\n{cls.history}")
        cls.history['a'] = cls.history['a'].apply(Decimal)
        cls.history['b'] = cls.history['b'].apply(Decimal)
        cls.history['operation'] = cls.history['operation'].apply(globals().__getitem__)
        cls.history['result'] = cls.history['result'].apply(Decimal)
