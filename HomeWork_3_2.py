import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    '''
        Функція генерує набір унікальних випадкових чисел для лотерей у межах заданих параметрів.
        min - мінімальне можливе число у наборі (не менше 1).
        max - максимальне можливе число у наборі (не більше 1000).
        quantity - кількість чисел, які потрібно вибрати (значення між min і max).
    '''
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
        
        # Блок перевірки введених даних на відповідність заданим кретеріям
        if min < 1 or min > 1000:
            print("Введене значення початку діапазону має бути в межах від 1 до 1000!")
            return
        if max < 1 or max > 1000:
            print("Введене значення кінця діапазону має бути в межах від 1 до 1000!")
            return
        if min > max:
            print("Початок та кінець діапазону були переплутані місцями, тому виконане коригування!")
            min, max = max, min
        if quantity > (max - min + 1):
            print("Введене значення кількості чисел, які потрібно вибрати, не може перевищувати кількості можливих значень діапазону!")
            return 
        if quantity < 0 :
            print("Введене значення кількості чисел, які потрібно вибрати, не може бути від'ємним!")
            return 
        
        # Через властивість множини не містити повторень, генеруємо випадкові числа з нашого діапазону саме в множину
        # щоб уникнути повторень без використання вкаладеного циклу для перевырки раныше вже випавших значень
        lottery_win_numbers = set()
        while len(lottery_win_numbers) < quantity:
            lottery_win_numbers.add(random.randrange(min, max + 1))
        lottery_win_numbers = sorted(list(lottery_win_numbers))
        return lottery_win_numbers
    except Exception as e:
        print(f"Виникла помилка при введенні значень - <<{e}>>!\nБудь ласка, повторіть введення числових значень в форматі 'min max quantity'!")


try:
    min, max, quantity = input("Введіть межі діапазону лотереї та кількість виграшних чисел \
(від 1 до 1000) в форматі 'min max quantity':").split()
    print(f"Виграшна комбінація чисел в заданому діапазоні: {get_numbers_ticket(min, max, quantity)}")
except Exception as e:
    print(f"Виникла помилка при введенні значень - <<{e}>>!\nБудь ласка, повторіть введення числових значень в форматі 'min max quantity'!")

print(f"Виграшна комбінація чисел в лотереї 5 із 36: {get_numbers_ticket(1, 36, 5)}")
print(f"Виграшна комбінація чисел в лотереї 6 із 49: {get_numbers_ticket(1, 49, 6)}")