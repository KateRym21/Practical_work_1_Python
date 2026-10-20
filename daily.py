"""Щоденна видача інгредієнтів."""
import random
import config
from data import INGREDIENTS
from exceptions_game import InventoryFullError


def give_daily_ingredients(player):
    names = list(INGREDIENTS)
    print(f"\nНовий день! Ти отримуєш {config.DAILY_INGREDIENTS} інгредієнтів:")
    for _ in range(config.DAILY_INGREDIENTS):
        item = random.choice(names)
        try:
            player.ingredients.add(item, 1)
        except InventoryFullError:
            print(f"  ✗ {item} — немає місця, інгредієнт втрачено")
        else:
            print(f"  + {item}")
