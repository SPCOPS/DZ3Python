# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3
# -> 1

n = abs(int(input('Введите количество элементов массива: ')))
a = input("Введите через пробел элементы массива: ").split()
b = list(map(int, a))
print(b)
if len(b) != n:
    print('Введите верное количество чисел!')
else:
    X = int(input('Введите число для поиска: '))
    count = 0
    for i in range(n):
        if b[i] == X:
            count += 1
    print(f'Число {X} встречается в массиве {count} раз') 


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

n = abs(int(input('Введите количество элементов массива: ')))
a = input("Введите через пробел элементы массива: ").split()
b = list(map(int, a))
if len(b) != n or n == 0:
    print('Введите верное количество чисел!')
else:
    X = int(input('Введите число для сравнения: '))
    min = abs(X - b[0])
    index = 0
    for i in range(1, n):
        count = abs(X - b[i])
        if count < min:
            min = count
            index = i
    print(f'Число {b[index]} в массиве ближе к {X}, расстояние: {abs(X - b[index])}')


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.
# Ввод: ноутбук
# Вывод: 12

en = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
ru = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
n = abs(int(input('Введите 1, если русское слово; введите 2, если английское слово: ')))
word = input('Введите слово: ').upper()
if n == 1:
	print('Это слово стоит', sum([k for i in word for k, v in en.items() if i in v]), 'очков')
elif n == 0:
	print('Это слово стоит', sum([k for i in word for k, v in ru.items() if i in v]), 'очков')
else:
    print('Введите 1 или 2.')