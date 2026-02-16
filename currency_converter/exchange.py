"""
Модуль exchange.py
Управляет списком доступных валют и их курсами.
"""
from .currency import Currency

class ExchangeRate:
    def __init__(self):
        """
        Инициализация системы обмена.
        Создает пустое хранилище для валют.
        """
        self.currencies = {}

    def add_currency(self, currency: Currency):
        """
        Добавляет новую валюту в систему.

        :param currency: Объект класса Currency, который нужно добавить.
        """
        if currency.code in self.currencies:
            print(f"Валюта {currency.code} уже существует.")
        else:
            self.currencies[currency.code] = currency
            print(f"Валюта {currency.name} ({currency.code}) добавлена.")

    def update_rate(self, code: str, new_rate: float):
        """
        Обновляет курс существующей валюты.

        :param code: Код валюты (например, 'USD').
        :param new_rate: Новое значение курса (тип float).
        """
        if code in self.currencies:
            self.currencies[code].rate = new_rate
            print(f"Курс для {code} обновлен: {new_rate}")
        else:
            print(f"Ошибка: Валюта {code} не найдена.")

    def get_currency(self, code: str) -> Currency:
        """
        Получает объект валюты по её коду.

        :param code: Код искомой валюты.
        :return: Объект Currency или None, если валюта не найдена.
        """
        return self.currencies.get(code)

    def show_rates(self):
        """Выводит список всех валют и их текущих курсов."""
        print("\n--- Текущие курсы валют ---")
        for currency in self.currencies.values():
            print(currency)
        print("---------------------------")

if __name__ == "__main__":
    # Тест модуля
    ex = ExchangeRate()
    ex.add_currency(Currency("TST", "Test", 1.0))
    ex.show_rates()