# Получить ключ по значению
def get_symbol(sl, val):
    """Фукнция находит аргумент словаря по ключу

        Параметры функции:
            sl - словарь
            val - значение ключа

    """
    for a, b in sl.items():
        if val == b:
            return a