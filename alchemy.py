"""Варіння зілля."""
from data import POTIONS, INGREDIENTS
from exceptions_game import GameError, InventoryFullError, NotEnoughItemError, UnknownItemError


def find_ingredients(player, potion_name):
    """Підбирає з інвентаря по одному інгредієнту на кожну категорію рецепта."""
    try:
        recipe = POTIONS[potion_name]["recipe"]
    except KeyError as e:
        raise UnknownItemError(f"Невідоме зілля: {potion_name}") from e

    chosen = []
    for category in recipe:
        for name, _count in player.ingredients.slots:
            if INGREDIENTS[name] == category:
                chosen.append(name)
                break
        else:
            raise NotEnoughItemError(f"Немає інгредієнта категорії «{category}»")
    return chosen


def craft_potion(player, potion_name):
    """Варить зілля. Повертає список витрачених інгредієнтів."""
    chosen = find_ingredients(player, potion_name)
    if player.potions.free_space(potion_name) < 1:
        raise InventoryFullError("В інвентарі зілля немає місця — продай зілля в кінці дня")
    for name in chosen:
        player.ingredients.remove(name, 1)
    player.potions.add(potion_name, 1)
    return chosen


def craftable_potions(player):
    """Список назв зілля, які можна зварити просто зараз."""
    result = []
    for potion_name in POTIONS:
        try:
            find_ingredients(player, potion_name)
        except GameError:
            continue
        else:
            result.append(potion_name)
    return result
