i = 1
while i == 1: # Выполняем цикл, пока  i равно 1
    num_puhkin = 0  # обнуляем счетчик правильных ответов по Пушкину
    num_lermontov = 0  # обнуляем счетчик правильных ответов по Лермонтову
    num_nekrasov = 0  # обнуляем счетчик правильных ответов по Некрасову
    num_esenin = 0  # обнуляем счетчик правильных ответов по Есенину
    num_asadov = 0  # обнуляем счетчик правильных ответов по Асадову

    born_year_puhkin = int(input("Введите год рождения Пушкина А.С.: ")) # 1837
    if born_year_puhkin == 1837:
        num_puhkin = num_puhkin + 1 # Считаем количество правильных ответов по Пушкину

    born_year_lermontov = int(input("Введите год рождения Лермонтова М.Ю.: ")) # 1814
    if born_year_lermontov == 1814:
        num_lermontov = num_lermontov + 1 # Считаем количество правильных ответов по Лермонтову

    born_year_nekrasov = int(input("Введите год рождения Некрасова Н.А.: ")) # 1821
    if born_year_nekrasov == 1821:
        num_nekrasov = num_nekrasov + 1 # Считаем количество правильных ответов по Некрасову

    born_year_esenin = int(input("Введите год рождения Есенина С.А.: ")) # 1895
    if born_year_esenin == 1895:
        num_esenin = num_esenin + 1 # Считаем количество правильных ответов по Есенину

    born_year_asadov = int(input("Введите год рождения Асадова Э.А.: ")) # 1923
    if born_year_asadov == 1923:
        num_asadov = num_asadov + 1 # Считаем количество правильных ответов по Асадову

    # Вычисления и вывод результатов
    true_answer = num_puhkin + num_lermontov + num_nekrasov + num_esenin + num_asadov
    false_answer = 5 - true_answer
    print() # Пустая строка
    print("Количество правильных ответов : ", true_answer)
    print("Количество ошибок : ", false_answer)
    print("Процент правильных ответов : ", 100 * true_answer / 5)
    print("Процент ошибок : ", 100 * false_answer / 5)

    # Продолжение или Выход
    i= int(input("Для продолжения введите - 1, Для завершения - 0  "))

print("End") # Сообщаем, что программа завершила работу