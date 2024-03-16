"""
В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
фразу «Министерства образования Ростовской области», посчитать количество
произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.
"""

with open('PZ_14/hotline.txt', 'r', encoding='utf-8') as fail:
    content = fail.readlines()
    
contener = 0

with open('PZ_14/new_hotline.txt', 'w', encoding='utf-8') as fail:
    
    for slova in content:
        if "Горячая линия" in slova:
            split_slova = slova.split("Горячая линия")
            
            fail.write(split_slova[0] + "Горячая линия Министерства образования Ростовской области" + split_slova[1])
        
            contener += 1
    fail.write(f"\n\nКоличество Добавлений: {contener}")
    
    list_my = []
    for element in content:
        split_elem = element.split()
        list_my.append(split_elem)

    nomer_list = []
    
    list_my.pop()
    for list_slesh in list_my:
        print(list_slesh)
        
    for nomer in range(len(list_my)):
        print(list_slesh[-1])
        
    
