from exchange import ExchangeRate

class Converter:
    def __init__(self, exchange_system: ExchangeRate, commission_percent=1.0):
        """
        :param exchange_system: Объект системы обменных курсов
        :param commission_percent: Процент комиссии (по умолчанию 1%)
        """
        self.exchange_system = exchange_system
        self.commission_percent = commission_percent

    def calculate_commission(self, amount):
        """Задача 4: Рассчитать комиссию"""
        return amount * (self.commission_percent / 100)

    def convert(self, amount, from_code, to_code):
        """Задача 3: Перевести сумму"""
        curr_from = self.exchange_system.get_currency(from_code)
        curr_to = self.exchange_system.get_currency(to_code)

        if not curr_from or not curr_to:
            print("Ошибка: Одна из валют не найдена.")
            return None

        base_amount = amount * curr_from.rate
        converted_amount = base_amount / curr_to.rate

        commission = self.calculate_commission(converted_amount)
        final_amount = converted_amount - commission

        return {
            "initial_amount": amount,
            "from": from_code,
            "to": to_code,
            "converted_raw": converted_amount,
            "commission": commission,
            "final_amount": final_amount
        }