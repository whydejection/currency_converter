
class Currency:
    def __init__(self, code, name, rate):
        """
        Инициализация валюты.
        :param code: Код валюты (например, 'USD')
        :param name: Название валюты (например, 'Доллар США')
        :param rate: Курс валюты по отношению к базовой валюте (например, к рублю)
        """
        self.code = code
        self.name = name
        self.rate = rate

    def __str__(self):
        return f"{self.name} ({self.code}): {self.rate}"