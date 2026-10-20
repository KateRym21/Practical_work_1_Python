"""Продаж зілля наприкінці дня."""
import random
from data import POTIONS
from exceptions_game import UnknownItemError


def market_multiplier():
    """Щодня ціни на ринку трохи інші."""
    return round(random.uniform(0.8, 1.3), 2)


def sell(player, potion_name, amount, multiplier):
    """Продає amount штук зілля, повертає виручку."""
    try:
        base_price = POTIONS[potion_name]["price"]
    except KeyError as e:
        raise UnknownItemError(f"Невідоме зілля: {potion_name}") from e

    player.potions.remove(potion_name, amount)   # може кинути NotEnoughItemError
    earned = int(base_price * multiplier) * amount
    player.gold += earned
    return earned


def sell_all(player, multiplier):
    """Продає все зілля. Повертає (виручка, продано штук, середня ціна)."""
    total = 0
    sold = 0
    for name in list({n for n, _ in player.potions.slots}):
        amount = player.potions.count(name)
        total += sell(player, name, amount, multiplier)
        sold += amount
    try:
        average = total // sold
    except ZeroDivisionError:
        average = 0
    return total, sold, average
