from datetime import datetime

def get_upcoming_birthdays(users: list) -> list:
    '''
        Функція повернутає список всіх, у кого день народження вперед на 7 днів включаючи поточний день, 
        з перенесенням вихідних.
    '''
    today = datetime.today().date()
    congrats_list = []
    # Проходимося по списку та аналізуємо дати народження кожного користувача
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday_this_year = user_birthday.replace(year = today.year)
        # Перевіряємо, чи вже минув день народження в цьому році
        if user_birthday_this_year < today:
            user_birthday_this_year = user_birthday.replace(year = today.year + 1)
        # Визначаємо різницю між днем народження та поточним днем
        days_to_user_birthday_this_year = user_birthday_this_year.toordinal() - today.toordinal()
        # Перевіряємо, чи день народження припадає на вихідний
        if user_birthday_this_year.weekday() == 5:
            days_to_user_congrats = days_to_user_birthday_this_year + 2
        elif user_birthday_this_year.weekday() == 6:
            days_to_user_congrats = days_to_user_birthday_this_year + 1
        # Відбираємо тих, чий день народження відбувається протягом наступного тижня
        if days_to_user_birthday_this_year < 7:
            user_congrats_day = user_birthday_this_year.replace(day = today.day + days_to_user_congrats)
            user_congrats_day = user_congrats_day.strftime("%Y.%m.%d")
            congrats_list.append({"name": user["name"], "congratulation_date": user_congrats_day})
        
    if congrats_list:
        return f"Список іменинників на наступні 7 днів: \n{congrats_list}"
    else:
        return "В найближчі 7 днів немає іменинників!"


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alexander", "birthday": "1985.03.09"},
    {"name": "Artur", "birthday": "1990.03.10"},
    {"name": "Igor", "birthday": "1990.03.15"},
]
print(get_upcoming_birthdays(users))