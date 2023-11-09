from num2words import num2words

# Напишем сумму в рублях в слова с указанием валюты
def format_money(total):
    rub = int(total)
    rub_words = num2words(rub, lang='ru').capitalize()
    
    rub_str = str(rub)
    number = int(rub_str[-1])
    two_numbers = int(rub_str[-2:]) if len(rub_str) >= 2 else None

    if two_numbers in [11, 12, 13, 14] or number in [0, 5, 6, 7, 8, 9]:
        rub_word = 'рублей'
    elif number == 1:
        rub_word = 'рубль'
    else:
        rub_word = 'рубля'

    return f'{rub_words} {rub_word}'

def sum_min(N, distances, tariffs):
    # Создаем список с индексами такси для каждого сотрудника
    taxi = [0] * N

    # Сортируем тарифы такси по возрастанию
    sorted_tariffs = sorted(enumerate(tariffs), key=lambda x: x[1], reverse=True)

    # Распределяем сотрудников по такси с учетом минимальных затрат
    for i, distance in enumerate(distances):
        # Выбираем такси с наибольшим тарифом
        taxi_index, _ = sorted_tariffs[0]
        taxi[i] = taxi_index

        # Удаляем выбранное такси из списка доступных
        sorted_tariffs.pop(0)

    # Вычисляем общие затраты на такси
    total_expenses = sum(tariffs[taxi[i]] * distances[i] for i in range(N))

    return taxi, total_expenses

def main():
    # Ввод данных
    N = int(input("Введите количество сотрудников: "))
    while N < 1 or N > 1000:
        print("Количество сотрудников должно быть в диапазоне от 1 до 1000")
        N = int(input("Введите количество сотрудников: "))
    distances = []
    tariffs = []

    print("Введите расстояния до домов сотрудников:")
    for _ in range(N):
        distance = int(input())
        distances.append(distance)

    print("Введите тарифы за проезд в такси:")
    for _ in range(N):
        tariff = int(input())
        tariffs.append(tariff)

    # Вычисление минимальных затрат и рассадки сотрудников
    taxi, total = sum_min(N, distances, tariffs)

    # Вывод результатов
    print("Рассадка сотрудников по такси:")
    for i, taxi_index in enumerate(taxi):
        print(f"Сотрудник {i+1} - Такси {taxi_index+1}")

    formatt_money = format_money(total)
    print("Сумма затрат:", total ,"(", formatt_money, ")")


if __name__ == "__main__":
    main()
