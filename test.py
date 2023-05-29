# with open('test.txt', 'a', encoding='utf-8') as file:
#     file.write('Привет, Мир!')
# with open('test.txt', 'a', encoding='utf-8') as file:
#     file.write('\nПривет, Мир!')

# Замена строки одной на другую (readlines - команда возвращает список со строками)
with open('test.txt', 'r', encoding='utf-8') as file: 
    data = file.readlines()

# по индексу поменяли второй элемент
    data[1] = 'Новая строка\n' 

with open('test.txt', 'w', encoding='utf-8') as file: 
    file.writelines(data)

        