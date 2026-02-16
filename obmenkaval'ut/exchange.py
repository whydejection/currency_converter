from currency import Currency

class ExchangeRate:
    def __init__(self):
        self.currencies = {}

    def add_currency(self, currency: Currency):
        """Задача 1: Добавить валюту"""
        if currency.code in self.currencies:
            print(f"Валюта {currency.code} уже существует.")
        else:
            self.currencies[currency.code] = currency
            print(f"Валюта {currency.name} ({currency.code}) добавлена с курсом {currency.rate}.")

    def update_rate(self, code, new_rate):
        """Задача 2: Обновить курс"""
        if code in self.currencies:
            self.currencies[code].rate = new_rate
            print(f"Курс для {code} обновлен: {new_rate}")
        else:
            print(f"Ошибка: Валюта {code} не найдена.")

    def get_currency(self, code):
        """Получение объекта валюты по коду"""
        return self.currencies.get(code)

    def show_rates(self):
        """Задача 5: Вывести текущие курсы"""
        print("\n--- Текущие курсы валют ---")
        for code, currency in self.currencies.items():
            print(currency)
        print("---------------------------")