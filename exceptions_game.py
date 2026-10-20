"""Власні виняткові ситуації гри."""


class GameError(Exception):
    """Базовий клас усіх ігрових помилок."""


class InventoryFullError(GameError):
    """В інвентарі немає місця."""


class NotEnoughItemError(GameError):
    """Не вистачає предметів (інгредієнтів або зілля)."""


class UnknownItemError(GameError):
    """Такого предмета або рецепта не існує."""
