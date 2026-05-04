class ConsoleView:
    @staticmethod
    def show_menu():
        print("\n--- Password Manager ---")
        print("1. Показать все пароли")
        print("2. Добавить новый пароль")
        print("3. Сгенерировать пароль")
        print("4. Удалить запись")
        print("5. Выход")
        return input("Выберите действие: ")

    @staticmethod
    def display_records(records):
        if not records:
            print("\nСписок пуст.")
        for i, r in enumerate(records):
            print(f"{i}. [{r.service}] User: {r.username} | Pass: {r.password} (Дата: {r.created_at})")