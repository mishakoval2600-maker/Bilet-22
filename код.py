def find_max_by_abs(arr):
    if not arr:
        return None
    max_element = arr[0]
    for element in arr:
        if abs(element) > abs(max_element):
            max_element = element
    return max_element


def sum_between_positives(arr):

    first_pos_idx = -1
    second_pos_idx = -1
    
    for i, element in enumerate(arr):
        if element > 0:
            if first_pos_idx == -1:
                first_pos_idx = i
            elif second_pos_idx == -1:
                second_pos_idx = i
                break
    

    if first_pos_idx != -1 and second_pos_idx != -1:
        suma = sum(arr[first_pos_idx + 1:second_pos_idx])
        return suma, first_pos_idx, second_pos_idx
    else:
        return None, first_pos_idx, second_pos_idx


def move_zeros_to_end(arr):
    
    non_zero = [x for x in arr if x != 0]
    zeros = [x for x in arr if x == 0]
    return non_zero + zeros

def main():
    print("=" * 60)
    print("ОБРОБКА ОДНОВИМІРНОГО МАСИВУ")
    print("=" * 60)
    
    print("\nВведіть елементи масиву через кому:")
    user_input = input("Наприклад: 3.5, -7.2, 0, 4.1, -2.3, 0, 5.6\n> ")
    
    try:
        array = [float(x.strip()) for x in user_input.split(',')]
    except ValueError:
        print("Помилка: Невірний формат вводу!")
        return
    
    print(f"\nВихідний масив: {array}")
    print(f"Кількість елементів: {len(array)}")
    
    max_abs_element = find_max_by_abs(array)
    print(f"\n{'─' * 60}")
    print(f"1. Максимальний за модулем елемент: {max_abs_element}")
    print(f"   Модуль: |{max_abs_element}| = {abs(max_abs_element)}")
    
    suma, first_idx, second_idx = sum_between_positives(array)
    print(f"\n{'─' * 60}")
    if suma is not None:
        print(f"2. Перший додатний елемент: {array[first_idx]} (індекс {first_idx})")
        print(f"   Другий додатний елемент: {array[second_idx]} (індекс {second_idx})")
        print(f"   Елементи між ними: {array[first_idx + 1:second_idx]}")
        print(f"   Сума елементів між ними: {suma}")
    else:
        print(f"2. Недостатньо додатних елементів для обчислення суми")
        if first_idx == -1:
            print(f"   Не знайдено жодного додатного елемента")
        else:
            print(f"   Знайдено тільки один додатний елемент: {array[first_idx]}")
    
    transformed_array = move_zeros_to_end(array)
    print(f"\n{'─' * 60}")
    print(f"3. Перетворений масив (нулі в кінці):")
    print(f"   До:  {array}")
    print(f"   Після: {transformed_array}")
    
    print(f"\n{'═' * 60}")
    print("Програма завершена успішно!")
    print(f"{'═' * 60}")


if __name__ == "__main__":
    main()