"""
Даны две последовательности. Найти элементы, различные для двух
последовательностей и их среднее арифметическое.
"""

one_list_numbers = [i for i in range(1, 6)]
two_list_numbers = [j for j in range(5, 10)]

unique_elements = list(set(one_list_numbers + two_list_numbers))

print(
    "\nРазличные элементы:",
    *unique_elements,
    f"\nСреднее арифметическое: {sum(unique_elements) / len(unique_elements)}"
)
