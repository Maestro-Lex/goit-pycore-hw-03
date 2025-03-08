from datetime import datetime

def get_days_from_today(date: str) -> int:
    '''
        Функція розраховує кількість днів між заданою датою і поточною датою.
    '''
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        date_in_days = date.toordinal() # Розраховуємо кількість повних днів від початку нашої ери до введеної дати
        today = datetime.today()
        today_in_days = today.toordinal() # Розраховуємо кількість повних днів від початку нашої ери до согодні
        print(f"Кількість днів між датою та сьогодні - {today_in_days - date_in_days}!")
        return today_in_days - date_in_days
    except Exception:
        date = input("Ви ввели некоректну дату. Прохання повторити введення в форматі РРРР-ММ-ДД (наприклад - 2020-10-09): ")
        get_days_from_today(date)
    

date = input("Введіть дату, яку треба обчислити, в форматі РРРР-ММ-ДД (наприклад - 2020-10-09): ")
get_days_from_today(date)