"""Точка входу. Запуск: python main.py"""
try:
    import config
    import data
    import game
    import daily
    import ui
    import save_system
    from player import Player
except ModuleNotFoundError as e:
    print(f"Не знайдено модуль гри: {e}. Усі .py файли мають лежати в одній папці.")
    raise SystemExit(1)


def check_pools():
    if len(data.INGREDIENTS) < config.MIN_INGREDIENT_POOL:
        raise ValueError("Пул інгредієнтів менший за 200")
    if len(data.POTIONS) < config.MIN_POTION_POOL:
        raise ValueError("Пул зілля менший за 50")


def new_or_load():
    player = save_system.load_game()
    if player is not None:
        print("Знайдено збереження. 1 — продовжити, 2 — нова гра")
        if ui.ask_int("> ", 1, 2) == 1:
            return player
    player = Player()
    print(f"Ти алхімік, що заборгував гільдії {config.DEBT} золота. Маєш {config.MAX_DAYS} днів!")
    daily.give_daily_ingredients(player)
    return player


def main():
    try:
        check_pools()
        player = new_or_load()
        game.run_game(player)
    except KeyboardInterrupt:
        print("\nГру перервано (Ctrl+C)")
    except EOFError:
        print("\nВведення закрито")
    except Exception as e:
        print(f"Неочікувана помилка: {type(e).__name__}: {e}")
    finally:
        print("Дякуємо за гру!")


if __name__ == "__main__":
    main()
