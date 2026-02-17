"""
Модуль converter.py
Отвечает за логику конвертации, расчет комиссии и сохранение истории в файл.
"""
import json  # Для работы с файлами
import os    # Для проверки существования файла
from datetime import datetime
from .exchange import ExchangeRate

class Converter:
    """
    Класс для конвертации валют с учетом комиссий и ведением истории операций.
    Атрибуты:
        exchange_system (ExchangeRate): Система получения курсов валют.
        commission_percent (float): Процент комиссии за конвертацию.
        history_file (str): Имя файла для сохранения истории.
        history (list): Список словарей с записями о транзакциях.
    """

    def __init__(self, exchange_system: ExchangeRate, commission_percent: float = 1.0):
        """
        Инициализирует конвертер и загружает существующую историю.
        Args:
            exchange_system (ExchangeRate): Объект, содержащий данные о валютах.
            commission_percent (float): Процент комиссии (по умолчанию 1.0).
        """
        self.exchange_system = exchange_system
        self.commission_percent = commission_percent
        self.history_file = "history.json"
        self.history = self.load_history()

    def load_history(self):
        """
        Загружает историю транзакций из JSON-файла.
        Returns:
            list: Список транзакций. Если файл пуст, поврежден или отсутствует, возвращает [].
        """
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, ValueError):
                return []
        return []

    def save_history(self):
        """
        Сохраняет текущую историю транзакций в JSON-файл.
        Использует форматирование indent=4 для читаемости.
        """
        try:
            with open(self.history_file, "w", encoding="utf-8") as f:
                json.dump(self.history, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Ошибка при сохранении истории: {e}")

    def calculate_commission(self, amount: float) -> float:
        """
        Рассчитывает сумму комиссии от указанной суммы.
        Args:
            amount (float): Сумма для расчета.
        Returns:
            float: Размер комиссии.
        """
        return amount * (self.commission_percent / 100)

    def convert(self, amount: float, from_code: str, to_code: str) -> dict:
        """
        Выполняет конвертацию валюты, рассчитывает комиссию и сохраняет результат в историю.
        Args:
            amount (float): Сумма для конвертации.
            from_code (str): Код исходной валюты.
            to_code (str): Код целевой валюты.
        Returns:
            dict: Данные операции (сумма, валюты, комиссия, итог) или None при ошибке.
        """
        curr_from = self.exchange_system.get_currency(from_code)
        curr_to = self.exchange_system.get_currency(to_code)

        if not curr_from or not curr_to:
            print("Ошибка: Одна из валют не найдена.")
            return None

        # Расчет через базовую валюту
        base_amount = amount * curr_from.rate
        converted_amount = base_amount / curr_to.rate

        commission = self.calculate_commission(converted_amount)
        final_amount = converted_amount - commission

        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "initial_amount": amount,
            "from": from_code,
            "to": to_code,
            "converted_raw": converted_amount,
            "commission": commission,
            "final_amount": final_amount
        }

        self.history.append(result)
        self.save_history()

        return result

    def get_history(self):
        """
        Возвращает накопленную историю транзакций.
        Returns:
            list: Список всех проведенных операций.
        """
        return self.history

