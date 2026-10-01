"""Міні-магазин в консолі """

ADMIN_PASSWORD = "admin123"

# Каталог: id -> назва, ціна, залишок на складі
catalog = {
    1: {"name": "Ноутбук", "price": 25999.99, "stock": 5},
    2: {"name": "Мишка", "price": 450.50, "stock": 20},
    3: {"name": "Клавіатура", "price": 1299.00, "stock": 10},
    4: {"name": "Навушники", "price": 899.90, "stock": 2},
    5: {"name": "Монітор", "price": 7999.00, "stock": 7},
}

# Кошик: id товару -> кількість
cart = {}

# --- lambda функції ---------------------------------------------------------
# Ціна у форматі ххх.ххгрн
format_price = lambda price: f"{price:.2f}грн"

# Словник лямбд для обчислень (як dict з лекції)
calc = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
}

# Сума за один рядок кошика: (id, кількість) -> ціна * кількість
line_total = lambda item: calc["mul"](catalog[item[0]]["price"], item[1])


# --- допоміжні функції ------------------------------------------------------
def read_int(text: str) -> int | None:
    """Зчитує ціле число, повертає None якщо ввели не число."""
    try:
        return int(input(text))
    except ValueError:
        print("Помилка: потрібно ввести ціле число!")
        return None


def get_total(*args: tuple) -> float:
    """Загальна сума кошика. Через *args можна передати свої рядки (id, к-сть)."""
    items = args if args else cart.items()
    return sum(map(line_total, items))


# --- каталог ----------------------------------------------------------------
def show_catalog(admin: bool = False) -> None:
    """Показує каталог. Для адміністратора додатково показує залишки."""
    print("\n=== КАТАЛОГ ===")
    for pid, p in catalog.items():
        line = f"{pid}. {p['name']:<12} {format_price(p['price'])}"
        if admin:
            line += f"   залишок: {p['stock']} шт."
        print(line)


# --- кошик ------------------------------------------------------------------
def add_to_cart(product_id: int, qty: int = 1) -> bool:
    """Додає товар у кошик. Повертає True, якщо вдалося."""
    if product_id not in catalog:
        print("Такого товару немає!")
        return False
    if qty <= 0:
        print("Кількість має бути більшою за 0!")
        return False
    already = cart.get(product_id, 0)
    if already + qty > catalog[product_id]["stock"]:
        print(f"Недостатньо на складі! Доступно: {catalog[product_id]['stock']} шт.")
        return False
    cart[product_id] = already + qty
    print(f"Додано: {catalog[product_id]['name']} x{qty}")
    return True


def remove_from_cart(product_id: int, qty: int = 1) -> bool:
    """Видаляє товар (або його частину) з кошика."""
    if product_id not in cart:
        print("Цього товару немає в кошику!")
        return False
    if qty <= 0:
        print("Кількість має бути більшою за 0!")
        return False
    cart[product_id] -= qty
    if cart[product_id] <= 0:
        del cart[product_id]
    print(f"Видалено: {catalog[product_id]['name']}")
    return True


def show_cart() -> None:
    """Показує вміст кошика та загальну суму."""
    print("\n=== КОШИК ===")
    if not cart:
        print("Кошик порожній")
        return
    for pid, qty in cart.items():
        p = catalog[pid]
        print(f"{pid}. {p['name']:<12} {format_price(p['price'])} x{qty} "
              f"= {format_price(line_total((pid, qty)))}")
    print(f"РАЗОМ: {format_price(get_total())}")


def checkout() -> None:
    """Купує товари з кошика: списує залишки та очищає кошик."""
    if not cart:
        print("Кошик порожній, купувати нічого!")
        return
    show_cart()
    if input("Підтвердити покупку? (т/н): ").lower() != "т":
        print("Покупку скасовано")
        return
    for pid, qty in cart.items():
        catalog[pid]["stock"] -= qty
    print(f"Дякуємо за покупку! Сплачено: {format_price(get_total())}")
    cart.clear()


# --- адміністратор ----------------------------------------------------------
def admin_menu() -> None:
    """Меню адміністратора: залишки, малі залишки, поповнення складу."""
    if input("Пароль: ") != ADMIN_PASSWORD:
        print("Невірний пароль!")
        return
    while True:
        print("\n--- АДМІНІСТРАТОР ---")
        print("1. Показати залишки\n2. Товари, що закінчуються (<=3)\n"
              "3. Поповнити склад\n0. Вийти з режиму адміністратора")
        choice = input("Ваш вибір: ")
        if choice == "1":
            show_catalog(admin=True)
        elif choice == "2":
            low = filter(lambda item: item[1]["stock"] <= 3, catalog.items())
            for pid, p in sorted(low, key=lambda item: item[1]["stock"]):
                print(f"{pid}. {p['name']} - {p['stock']} шт.")
        elif choice == "3":
            pid = read_int("ID товару: ")
            qty = read_int("Скільки додати: ")
            if pid in catalog and qty and qty > 0:
                catalog[pid]["stock"] += qty
                print("Склад поповнено")
            else:
                print("Некоректні дані!")
        elif choice == "0":
            break
        else:
            print("Невідома команда!")


# --- головна функція --------------------------------------------------------
def main() -> None:
    while True:
        print("\n===== МІНІ-МАГАЗИН =====")
        print("1. Переглянути каталог\n2. Додати товар в кошик\n"
              "3. Видалити товар з кошика\n4. Переглянути кошик\n"
              "5. Купити товари з кошика\n6. Увійти як адміністратор\n0. Вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            show_catalog()
        elif choice == "2":
            show_catalog()
            pid = read_int("ID товару: ")
            qty = read_int("Кількість: ")
            if pid is not None and qty is not None:
                add_to_cart(pid, qty)
        elif choice == "3":
            show_cart()
            pid = read_int("ID товару для видалення: ")
            qty = read_int("Кількість: ")
            if pid is not None and qty is not None:
                remove_from_cart(pid, qty)
        elif choice == "4":
            show_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            admin_menu()
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невідома команда!")


if __name__ == "__main__":
    main()
