# 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток:
# <h> час <m> мин <s> сек; * в остальных случаях:
# <d> дн <h> час <m> мин <s> сек.


class SecondsConverter:
    def __init__(self):
        self._SECOND = 1
        self._MINUTES_SECONDS = self._SECOND * 60
        self._HOURS_SECONDS = self._MINUTES_SECONDS * 60
        self._DAYS_SECONDS = self._HOURS_SECONDS * 24
        # так вроде объявляются константы в пайтон, не нарушаю snake_case

    def convert_secs(self, input_seconds):
        if not type(input_seconds) is int and not type(input_seconds) is float:
            return "Введены некорректные данные"
        if input_seconds >= self._DAYS_SECONDS:
            return self._days_convert(input_seconds)
        elif input_seconds >= self._HOURS_SECONDS:
            return self._hours_convert(input_seconds)
        elif input_seconds >= self._MINUTES_SECONDS:
            return self._minutes_convert(input_seconds)
        elif input_seconds >= 0:
            return f"{input_seconds} сек"  # output переменная не создается по причине отсутствия необходимости
        else:
            return "Введено некорректное количество секунд"

    def _minutes_convert(self, input_seconds):
        output_minutes = input_seconds // self._MINUTES_SECONDS
        output_seconds = input_seconds % self._MINUTES_SECONDS
        return f"{output_minutes} мин {output_seconds} сек"

    def _hours_convert(self, input_seconds):
        output_hours = input_seconds // self._HOURS_SECONDS
        seconds_left = input_seconds % self._HOURS_SECONDS
        return f"{output_hours} час " + self._minutes_convert(seconds_left)

    def _days_convert(self, input_seconds):
        output_days = input_seconds // self._DAYS_SECONDS
        seconds_left = input_seconds % self._DAYS_SECONDS
        return f"{output_days} дн " + self._hours_convert(seconds_left)


if __name__ == "__main__":
    converter = SecondsConverter()
    print(converter.convert_secs(90000))
