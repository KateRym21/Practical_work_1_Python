"""Кінцівка гри.

Сюжет: алхімік заборгував гільдії DEBT золота і має MAX_DAYS днів, щоб розрахуватись.
Виграш  — назбирав DEBT золота: гільдія повертає тобі майстерню і звання майстра.
Програш — дні закінчились, а боргу не віддано: майстерню забрали за борги.
"""
import config


def check_ending(player):
    """Повертає "win", "lose" або None, якщо гра триває."""
    if player.gold >= config.DEBT:
        return "win"
    if player.day > config.MAX_DAYS:
        return "lose"
    return None


def show_ending(result, player):
    print("\n" + "=" * 50)
    if result == "win":
        print("🏆 ПЕРЕМОГА!")
        print(f"Ти зібрав {player.gold} золота за {player.day} дн. і розрахувався з гільдією.")
        print("Тебе проголошують Верховним алхіміком королівства!")
    else:
        print("💀 ПОРАЗКА")
        print(f"Термін вийшов. У тебе лише {player.gold} із {config.DEBT} золота.")
        print("Гільдія забирає твою майстерню, а казани йдуть з молотка...")
    print("=" * 50)
