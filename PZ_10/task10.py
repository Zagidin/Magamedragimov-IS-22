"""
В озере водится несколько видов рыб. Три рыбака поймали рыб некоторых их имеющихся
в озере видов. Определить, рыб каких видов поймал каждый рыбак и рыб каких видов,
имеющихся в озере, не выловил ни один из рыбаков.
"""

type_fish = {
    "Тунец",
    "Сазан",
    "Белуга",
    "Окунь",
    "Сельди"
}
# "Щука",
# "Лещ",
# "Осетра"

fisherman_1 = {
    "Сазан",
    "Окунь",
    "Сельди",
    "Тунец"
}

fisherman_2 = {
    "Тунец",
    "Сазан",
    "Белуга"
}

fisherman_3 = {
    "Белуга",
    "Окунь"
}

dont_fish = type_fish - (fisherman_1 | fisherman_2 | fisherman_3)

if dont_fish == set():
    print(
        f"Первый рыбак поймал такие рыбы: {fisherman_1}\n"
        f"Второй рыбак: {fisherman_2}\n"
        f"Третий рыбак: {fisherman_3}\n"
        f"Рыбы, который не выловили ни один из рыбаков: <<НЕТ ТАКИХ РЫБ>>"
    )
else:
    print(
        f"Первый рыбак поймал такие рыбы: {fisherman_1}\n"
        f"Второй рыбак: {fisherman_2}\n"
        f"Третий рыбак: {fisherman_3}\n"
        f"Рыбы, который не выловили ни один из рыбаков: {dont_fish}"
    )
