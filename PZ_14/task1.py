"""В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
фразу «Министерства образования Ростовской области», посчитать количество
произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.
"""

import re

with open('PZ_14/hotline.txt', 'r', encoding='utf-8') as file:
    content = file.read()

    text = " Министерства образования Ростовской области"
    
# 1-2)
    count_dobavka = len(re.findall(r'Горячая линия', content))

    text_file = re.sub(r'(Горячая линия)', r'\1' + text, content)
    

with open('PZ_14/hotline.txt', 'r', encoding='utf-8') as file:
    content_nomer = file.readlines()
    
# 3)
    list_texta = []
    for element in content_nomer:
        split_elem = element.split()
        list_texta.append(split_elem)

    list_texta.pop()
    phone = []
    for i in range(len(list_texta)):
        phone.append(list_texta[i][-1])

    phone_number_03_50 = []
    for number in phone:
        if re.search(r'\d{2}(03|50)\b', number):
            phone_number_03_50.append(number)
    print("\nНомера:", *phone_number_03_50, "\n")

# 4)
    list_text_ege = [] 
    for ege in content_nomer:
        if 'ЕГЭ' in ege:
            list_text_ege.append(ege)
            
    list_split_ege = []
    for element in list_text_ege:
        split_elem_ege = element.split()
        list_split_ege.append(split_elem_ege)

    phone_ege = []
    for i in range(len(list_split_ege)):
        phone_ege.append(list_split_ege[i][-1])
        
    print("Номера телефона ЕГЭ/ГИА:", *phone_ege, "\n")
    
with open('PZ_14/new_hotline.txt', 'w', encoding='utf-8') as file:
    file.write(
        f"{text_file}\n\n"
        f"Количество произведённых Добавлений: {count_dobavka}"
        f"\nКоличество номеров: {len(phone)}"
        f"\nКоличество номеров на «03» и «50»: {len(phone_number_03_50)}"
        f"\nНомера телефонов горячих линий, связанных с ЕГЭ/ГИА: {len(phone_ege)}"
    )
