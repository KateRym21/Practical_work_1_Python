"""Головний герой — алхімік."""
import config
from inventory import Inventory


class Player:
    def __init__(self):
        self.gold = config.START_GOLD
        self.day = 1
        self.ingredients = Inventory("Інгредієнти", config.MAX_INGREDIENT_SLOTS, config.INGREDIENT_STACK)
        self.potions = Inventory("Зілля", config.MAX_POTION_SLOTS, config.POTION_STACK)

    def to_dict(self):
        return {
            "gold": self.gold,
            "day": self.day,
            "ingredients": self.ingredients.to_list(),
            "potions": self.potions.to_list(),
        }

    @classmethod
    def from_dict(cls, data):
        player = cls()
        player.gold = data["gold"]          # KeyError, якщо файл пошкоджений
        player.day = data["day"]
        player.ingredients.load_list(data["ingredients"])
        player.potions.load_list(data["potions"])
        return player
