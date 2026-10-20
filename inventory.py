"""Універсальний інвентар зі слотами та стаками."""
from exceptions_game import InventoryFullError, NotEnoughItemError


class Inventory:
    def __init__(self, name, max_slots, stack_size):
        self.name = name
        self.max_slots = max_slots
        self.stack_size = stack_size
        self.slots = []  # список [назва, кількість]

    def count(self, item):
        return sum(c for n, c in self.slots if n == item)

    def free_space(self, item):
        """Скільки штук цього предмета ще можна покласти."""
        space = sum(self.stack_size - c for n, c in self.slots if n == item)
        space += (self.max_slots - len(self.slots)) * self.stack_size
        return space

    def add(self, item, amount=1):
        try:
            if amount <= 0:
                raise ValueError("Кількість має бути додатною")
        except TypeError as e:
            raise ValueError("Кількість має бути числом") from e

        if amount > self.free_space(item):
            raise InventoryFullError(f"Інвентар «{self.name}» заповнений: немає місця для «{item}»")

        left = amount
        for slot in self.slots:            # спочатку добиваємо наявні стаки
            if left == 0:
                break
            if slot[0] == item:
                put = min(self.stack_size - slot[1], left)
                slot[1] += put
                left -= put
        while left > 0:                    # потім відкриваємо нові слоти
            put = min(self.stack_size, left)
            self.slots.append([item, put])
            left -= put

    def remove(self, item, amount=1):
        if amount <= 0:
            raise ValueError("Кількість має бути додатною")
        if self.count(item) < amount:
            raise NotEnoughItemError(f"Не вистачає «{item}» (треба {amount}, є {self.count(item)})")

        left = amount
        for slot in reversed(self.slots):
            if slot[0] == item and left > 0:
                take = min(slot[1], left)
                slot[1] -= take
                left -= take
        self.slots = [s for s in self.slots if s[1] > 0]

    def item_at(self, number):
        """Предмет зі слота за номером (з 1). Кидає IndexError, якщо слота нема."""
        if number < 1:
            raise IndexError("Номер слота починається з 1")
        return self.slots[number - 1]

    def show(self):
        print(f"--- {self.name} ({len(self.slots)}/{self.max_slots} слотів) ---")
        if not self.slots:
            print("  (порожньо)")
        for i, (name, count) in enumerate(self.slots, 1):
            print(f"  [{i}] {name} x{count}/{self.stack_size}")

    def to_list(self):
        return [[n, c] for n, c in self.slots]

    def load_list(self, data):
        self.slots = [[n, c] for n, c in data]
