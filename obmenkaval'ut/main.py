from currency import Currency
from exchange import ExchangeRate
from converter import Converter


def print_menu():
    print("\n=== МЕНЮ ОБМЕННИКА ===")
    print("1. Добавить новую валюту")
    print("2. Обновить курс валюты")
    print("3. Показать все курсы")
    print("4. Конвертировать валюту")
    print("0. Выход")
    print("=======================")


def main():
    exchange = ExchangeRate()
    exchange.add_currency(Currency("RUB", "Российский рубль", 1.0))
    exchange.add_currency(Currency("USD", "Доллар США", 92.5))

    converter = Converter(exchange, commission_percent=2.0)

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            print("\n--- Добавление валюты ---")
            code = input("Введите код валюты (например, CNY): ").strip().upper()
            name = input("Введите название валюты: ").strip()

            try:
                rate_input = input("Введите курс к рублю: ")
                rate = float(rate_input)

                new_currency = Currency(code, name, rate)
                exchange.add_currency(new_currency)
            except ValueError:
                print("Ошибка: Курс должен быть числом (используйте точку для дробей).")

        elif choice == "2":
            code = input("Введите код валюты для обновления: ").strip().upper()
            if exchange.get_currency(code):
                try:
                    new_rate = float(input(f"Введите новый курс для {code}: "))
                    exchange.update_rate(code, new_rate)
                except ValueError:
                    print("Ошибка: Курс должен быть числом.")
            else:
                print("Такая валюта не найдена.")

        elif choice == "3":
            exchange.show_rates()

        elif choice == "4":
            print("\n--- Конвертация ---")
            from_code = input("Из какой валюты (код): ").strip().upper()
            to_code = input("В какую валюту (код): ").strip().upper()

            try:
                amount = float(input("Введите сумму: "))
                result = converter.convert(amount, from_code, to_code)

                if result:
                    print(f"\nРезультат операции:")
                    print(f"Исходная сумма: {result['initial_amount']} {result['from']}")
                    print(f"Сумма до комиссии: {result['converted_raw']:.2f} {result['to']}")
                    print(f"Комиссия: {result['commission']:.2f} {result['to']}")
                    print(f"На руки: {result['final_amount']:.2f} {result['to']}")
            except ValueError:
                print("Ошибка: Сумма должна быть числом.")

        elif choice == "0":
            print("Работа завершена.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    main()