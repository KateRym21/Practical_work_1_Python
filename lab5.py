"""Ігровий цикл."""
import config
import alchemy
import shop
import daily
import ending
import ui
import save_system
from data import POTIONS
from exceptions_game import GameError


def show_status(player):
    print(f"\n=== День {player.day}/{config.MAX_DAYS} | Золото: {player.gold}/{config.DEBT} ===")


def show_recipes():
    print("\n--- Книга рецептів (по 1 інгредієнту кожної категорії) ---")
    for name, info in POTIONS.items():
        print(f"{name} — {info['price']} зол.: {', '.join(info['recipe'])}")


def craft_menu(player):
    options = alchemy.craftable_potions(player)
    if not options:
        print("З наявних інгредієнтів нічого зварити. Дочекайся нового дня.")
        return
    print("\nМожна зварити:")
    for i, name in enumerate(options, 1):
        print(f"  {i}. {name} (база {POTIONS[name]['price']} зол.)")
    print("  0. Назад")
    choice = ui.ask_int("Що варимо? ", 0, len(options))
    if choice == 0:
        return
    used = alchemy.craft_potion(player, options[choice - 1])
    print(f"Готово: {options[choice - 1]}! Витрачено: {', '.join(used)}")


def sell_menu(player, multiplier):
    while True:
        player.potions.show()
        if not player.potions.slots:
            return
        print("1. Продати все  2. Продати зі слота  0. Нічого не продавати / далі")
        choice = ui.ask_int("> ", 0, 2)
        try:
            if choice == 0:
                return
            if choice == 1:
                total, sold, average = shop.sell_all(player, multiplier)
                print(f"Продано {sold} шт. за {total} зол. (середня ціна {average})")
            else:
                number = ui.ask_int("Номер слота: ", 1, 999)
                name, count = player.potions.item_at(number)     # IndexError, якщо слота нема
                amount = ui.ask_int(f"Скільки (1-{count}): ", 1, count)
                print(f"Виручка: {shop.sell(player, name, amount, multiplier)} зол.")
        except IndexError:
            print("Такого слота немає")
        except GameError as e:
            print(f"⚠ {e}")
        finally:
            print(f"Золото: {player.gold}")


def end_day(player):
    """Продаж зілля, перехід на новий день. Повертає "win"/"lose"/None."""
    multiplier = shop.market_multiplier()
    print(f"\nВечір. Ринковий коефіцієнт цін сьогодні: x{multiplier}")
    sell_menu(player, multiplier)

    result = ending.check_ending(player)
    if result:
        return result
    player.day += 1
    result = ending.check_ending(player)
    if result:
        return result
    daily.give_daily_ingredients(player)
    return None


def run_game(player):
    while True:
        show_status(player)
        print("1. Інвентар  2. Книга рецептів  3. Варити зілля")
        print("4. Закінчити день (продаж)  5. Зберегти  0. Вийти")
        try:
            choice = ui.ask_int("> ", 0, 5)
            if choice == 0:
                print("Вихід з гри")
                return
            elif choice == 1:
                player.ingredients.show()
                player.potions.show()
            elif choice == 2:
                show_recipes()
            elif choice == 3:
                craft_menu(player)
            elif choice == 4:
                result = end_day(player)
                if result:
                    ending.show_ending(result, player)
                    return
            elif choice == 5:
                save_system.save_game(player)
        except GameError as e:
            print(f"⚠ {e}")
