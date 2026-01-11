# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter='|'):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим пересечение двух множеств
    common_participants = participants1.intersection(participants2)

    # Возвращаем результат в виде строки, разделенной заданным разделителем
    return delimiter.join(common_participants)
# Данные для тестирования
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции
common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")