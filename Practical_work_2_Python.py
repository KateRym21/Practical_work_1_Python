import random

questions = [
    {
        "question": "Що належить до апаратного забезпечення комп'ютера?",
        "options": ["Процесор", "Операційна система", "Текстовий редактор", "Антивірусна програма"],
        "answer": 1
    },

    {
        "question": "Який пристрій використовується для довготривалого зберігання даних?",
        "options": ["Процесор", "SSD", "Оперативна пам'ять", "Монітор"],
        "answer": 2
    },

    {
        "question": "Для чого призначений процесор?",
        "options": ["Для зберігання файлів", "Для виконання команд та обробки даних", "Для друку документів", "Для введення тексту"],
        "answer": 2
    },

    {
        "question": "Який пристрій є пристроєм введення інформації?",
        "options": ["Монітор", "Принтер", "Клавіатура", "Проєктор"],
        "answer": 3
    },

    {
        "question": "Що таке операційна система?",
        "options": ["Апаратний компонент", "Системне програмне забезпечення", "Графічний редактор", "Пристрій введення"],
        "answer": 2
    }
]



users = {
    "taras": "1234",
    "ivan": "1111",
    "anna": "2222",
    "olena": "3333"
}



login = input("Введіть логін: ")
password = input("Введіть пароль: ")



if login in users and users[login] == password:

    print("\nВхід виконано успішно!")
    print("Ласкаво просимо,", login)

    right = 0

    for i in range(len(questions)):

        print("\n" + questions[i]["question"])

        # Виводимо варіанти відповідей
        for number, option in enumerate(questions[i]["options"], 1):
            print(number, option)

        answer = int(input("Оберіть правильний варіант (1 2 3 4): "))

        if answer == questions[i]["answer"]:
            print("Відповідь вірна!")
            right += 1
        else:
            print("Відповідь не вірна!")


    number_of_grades = random.randint(5, 12)

    # Випадкові оцінки від 1 до 4
    grades = []

    for i in range(number_of_grades):
        grades.append(random.randint(1, 4))


    print("\n--- Результат ---")
    print("Кількість оцінок:", number_of_grades)
    print("Оцінки:", grades)

    print(f"Ви відповіли правильно на {right} із {len(questions)} запитань.")

else:
    print("\nНеправильний логін або пароль!")



