from tkinter import IntVar


class ValueOperations:

    @staticmethod
    def value_in_range(value: int, lower_bound: int, upper_bound: int) -> bool:
        return lower_bound <= value <= upper_bound

    @staticmethod
    def add_value_to_entry_var_if_new_val_in_range(variable: IntVar, value: int, lower_bound: int, upper_bound: int):
        if not ValueOperations.value_in_range(variable.get() + value, lower_bound, upper_bound):
            return

        variable.set(variable.get() + value)
