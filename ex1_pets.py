# Задача № 1
# Для создания мини-базы данных и словаря в приложении для приюта
# для животных выполните следующие шаги:
# Создайте словарь с тремя ключами: кошки, собаки и иные.
# Разбейте информацию о животных из базы данных приюта на
# категории: кличка, возраст и порода.
# Разместите информацию о каждом животном внутри словаря,
# используя соответствующие ключи: кошка, собака или иной.
# Внутри каждого ключа создайте подпункты для хранения
# информации о кличке, возрасте и породе животного.
# Добавьте возможность поиска животных по кличке,
# возрасту или породе.
bd = []
with open('bd_pets.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if '\n' in line:
            bd.append(line[:-1])
        else:
            bd.append(line)


pets = {'кошки': [], 'собаки': [], 'иные': []}

for animal in bd:
    found = animal.split('-')
    name, age, breed = found[1].split(', ')
    if found[0].strip().lower() in ('кошка', 'кот'):
        pets['кошки'].append({'имя': name, 'возраст': age, 'порода': breed})
    elif found[0].strip().lower() in ('собака', 'пес'):
        pets['собаки'].append({'имя': name, 'возраст': age, 'порода': breed})
    else:
        pets['иные'].append({'имя': name, 'возраст': age, 'порода': found[0]+breed})

for key in pets:
    print(key)
    for data in range(len(pets[key])):
        for inf in pets[key][data]:
            print(pets[key][data][inf], end=' ')
        print()
    print()


found_pet = input('Введите информацию: ')
for key in pets:
    for data in range(len(pets[key])):
        for inf in pets[key][data]:
            if pets[key][data][inf].strip() == found_pet.strip():
                res = [pets[key][data][d] for d in pets[key][data]]
                print(', '.join(res).strip())

