"""
Главный файл запуска программы.
Демонстрирует работу библиотеки currency_converter.
"""

# Импортируем классы из нашей библиотеки (папки currency_converter)
from currency_converter import Currency, ExchangeRate, Converter


def print_menu():
    """Выводит текстовое меню на экран."""
    print("\n=== МЕНЮ ОБМЕННИКА ===")
    print("1. Добавить новую валюту")
    print("2. Обновить курс валюты")
    print("3. Показать все курсы")
    print("4. Конвертировать валюту")
    print("5. История транзакций")
    print("0. Выход")
    print("=======================")


def main():
    """Главная функция программы."""
    exchange = ExchangeRate()
    # Базовые валюты
    exchange.add_currency(Currency("RUB", "Российский рубль", 1.0))
    exchange.add_currency(Currency("USD", "Доллар США", 77.5))

    converter = Converter(exchange, commission_percent=2.0)

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            code = input("Код (USD): ").strip().upper()
            name = input("Название: ").strip()
            try:
                rate = float(input("Курс: "))
                exchange.add_currency(Currency(code, name, rate))
            except ValueError:
                print("Ошибка: Курс должен быть числом.")

        elif choice == "2":
            code = input("Код валюты: ").strip().upper()
            try:
                rate = float(input("Новый курс: "))
                exchange.update_rate(code, rate)
            except ValueError:
                print("Ошибка: Курс должен быть числом.")

        elif choice == "3":
            exchange.show_rates()


        elif choice == "4":
            print("\n--- Конвертация ---")
            print("Доступные валюты: RUB, USD (и другие добавленные)")
            f = input("Введите код валюты, ИЗ которой переводим (например, USD): ").strip().upper()
            t = input("Введите код валюты, В которую переводим (например, RUB): ").strip().upper()
            try:
                amt = float(input("Введите сумму перевода: "))
                res = converter.convert(amt, f, t)
                if res:
                    print(f"\nРезультат: {res['initial_amount']} {f} = {res['final_amount']:.2f} {t}")
                    print(f"(Комиссия составила: {res['commission']:.2f} {t})")
            except ValueError:

                print("Ошибка: Сумма должна быть числом.")

        elif choice == "5":
            history = converter.get_history()
            if not history:
                print("\nИстория пуста.")
            else:
                print("\n--- История операций ---")
                print(f"{'Время':<20} | {'Из':<5} | {'В':<5} | {'Сумма':<10} | {'Итог':<10}")
                print("-" * 65)
                for item in history:
                    print(f"{item['timestamp']:<20} | {item['from']:<5} | {item['to']:<5} | {item['initial_amount']:<10.2f} | {item['final_amount']:<10.2f}")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()