"""
Модуль converter.py
Отвечает за логику конвертации, расчет комиссии и сохранение истории в файл.
"""
import json  #Для работы с файлами
import os    #Для проверки существования файла
from datetime import datetime
from .exchange import ExchangeRate

class Converter:
    def __init__(self, exchange_system: ExchangeRate, commission_percent: float = 1.0):
        self.exchange_system = exchange_system
        self.commission_percent = commission_percent
        self.history_file = "history.json"  #Имя файла для сохранения
        self.history = self.load_history()  # <Загружаем историю при старте

    def load_history(self):
        """Загружает историю из файла JSON, если он существует."""
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, ValueError):
                return [] #Если файл поврежден, возвращаем пустой список
        return []

    def save_history(self):
        """Сохраняет текущую историю в файл JSON."""
        try:
            with open(self.history_file, "w", encoding="utf-8") as f:
                #indent=4 делает файл красивым и читаемым для человека
                #ensure_ascii=False позволяет сохранять русские буквы
                json.dump(self.history, f, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Ошибка при сохранении истории: {e}")

    def calculate_commission(self, amount: float) -> float:
        return amount * (self.commission_percent / 100)

    def convert(self, amount: float, from_code: str, to_code: str) -> dict:
        curr_from = self.exchange_system.get_currency(from_code)
        curr_to = self.exchange_system.get_currency(to_code)

        if not curr_from or not curr_to:
            print("Ошибка: Одна из валют не найдена.")
            return None

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
        self.save_history()  #Сохраняем сразу после добавления

        return result

    def get_history(self):
        return self.history