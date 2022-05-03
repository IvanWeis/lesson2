true_year = 1837  # Правильный год рождения Пушкина А.С.
true_day = '6 июня'  # Правильный день рождения Пушкина А.С.

born_year = int(input("Введите год рождения Пушкина А.С.: "))
if born_year != true_year:
    print("Неверный год рождения")
    print("End")
else:
    born_day = input("Введите день рождения Пушкина А.С. в формате 8 августа : ")
    if born_day != true_day:
        print("Неверный день рождения")
        print("End")
    else:
        print("Вы хорошо знаете дату рождения Пушкина А.С.")
        print("End")
