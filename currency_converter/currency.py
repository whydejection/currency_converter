"""
Модуль currency.py
Описывает структуру данных одной валюты.
"""

class Currency:
    def __init__(self, code: str, name: str, rate: float):
        """
        Инициализация объекта валюты.

        :param code: Код валюты (например, 'USD', 'EUR').
        :param name: Полное название валюты (например, 'Доллар США').
        :param rate: Текущий курс валюты по отношению к базовой валюте.
        """
        self.code = code
        self.name = name
        self.rate = rate

    def __str__(self):
        """Возвращает строковое представление валюты."""
        return f"{self.name} ({self.code}): {self.rate}"

# Обозначение главного тела (для тестирования модуля отдельно)
if __name__ == "__main__":
    c = Currency("USD", "Test Dollar", 100.0)
    print(c)

