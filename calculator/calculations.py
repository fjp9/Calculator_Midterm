import pandas as pd
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
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history = cls.history.iloc[0:0]

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
        cls.history.to_csv(filename, index=False)
    
    @classmethod
    def load_history(cls, filename: str):
        cls.history = pd.read_csv(filename)
        cls.history['a'] = cls.history['a'].apply(Decimal)
        cls.history['b'] = cls.history['b'].apply(Decimal)
        cls.history['operation'] = cls.history['operation'].apply(globals().__getitem__)
        cls.history['result'] = cls.history['result'].apply(Decimal)
