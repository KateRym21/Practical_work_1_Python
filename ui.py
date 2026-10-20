"""Допоміжні функції введення."""


def ask_int(prompt, low, high):
    """Питає ціле число в діапазоні [low, high], поки не введуть правильно."""
    while True:
        try:
            value = int(input(prompt))
            if not low <= value <= high:
                raise ValueError(f"Число має бути від {low} до {high}")
        except ValueError as e:
            print(f"Некоректне введення: {e}")
        else:
            return value
