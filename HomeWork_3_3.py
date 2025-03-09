
import re
import time

def normalize_phone(phone_numbers: list) -> list:
    '''
         функція, яка автоматично нормалізує номери телефонів до потрібного формату, 
         идаляючи всі зайві символи та додаючи міжнародний код країни, якщо потрібно.
    '''
    normalized_phone_numbers = []
    # Створюємо патерн регулярного виразу
    pattern = r"[+0-9]"
    for phone in phone_numbers:
        match = re.findall(pattern, phone)
        phone = ''.join(match)
        # Додаємо код країни (або умовними операторами або через зріз, що коротше та вірніше)
        match phone[0]:
            case "0":
                phone = "+38" + phone
            case "8":
                phone = "+3" + phone
            case "3":
                phone = "+" + phone
        # or phone = "+38" + phone[len(phone)-10:]
        # Додаємо виправлений номер до фінального списку
        normalized_phone_numbers.append(phone)
    return normalized_phone_numbers


def normalize_phone_without_re(phone_numbers: list) -> list:
    '''
        Теж саме, але без використання регулярних виразів.
    '''
    normalized_phone_numbers = []
    acceptable_symbols = "+0123456789"
    for phone in phone_numbers:
        # Видаляємо з номеру телефону всі потрібні нам символи
        trans_table = str.maketrans('', '', acceptable_symbols)
        unwanted_symbols = phone.translate(trans_table)
        # Видаляємо в номері телефону символи, які були виявлені та поміщені до unwanted_symbols
        for ch in unwanted_symbols:
            phone = phone.replace(ch, "")
        # Додаємо код країни (або умовними операторами або через зріз, що коротше)
        phone = "+38" + phone[len(phone)-10:]
        # Додаємо виправлений номер до фінального списку
        normalized_phone_numbers.append(phone)
    return normalized_phone_numbers


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


start_time = time.perf_counter()
print(normalize_phone(raw_numbers))
end_time = time.perf_counter()
print(f"Час виконання з регуляркою: {end_time - start_time} секунд")

start_time = time.perf_counter()
print(normalize_phone_without_re(raw_numbers))
end_time = time.perf_counter()
print(f"Час виконання без регулярки: {end_time - start_time} секунд")
# Здебільшого час виконання без регулярки швидший у 2 рази