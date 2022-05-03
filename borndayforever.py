true_year = 1837  # Правильный год рождения Пушкина А.С.
true_day = '6 июня'  # Правильный день рождения Пушкина А.С.

born_year = int(input("Введите год рождения Пушкина А.С.: "))
while born_year != true_year:
    born_year = int(input("Введите год рождения Пушкина А.С.: "))

born_day = input("Введите день рождения Пушкина А.С. в формате 8 августа : ")
while born_day != true_day:
    born_day = input("Введите день рождения Пушкина А.С. в формате 8 августа : ")

print("Верно")
print("End")