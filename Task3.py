'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
ценность. В случае с английским алфавитом очки распределяются так:
● A, E, I, O, U, L, N, S, T, R – 1 очко;
● D, G – 2 очка;
● B, C, M, P – 3 очка;
● F, H, V, W, Y – 4 очка;
● K – 5 очков;
● J, X – 8 очков;
● Q, Z – 10 очков.
А русские буквы оцениваются так:
● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
● Д, К, Л, М, П, У – 2 очка;
● Б, Г, Ё, Ь, Я – 3 очка;
● Й, Ы – 4 очка;
● Ж, З, Х, Ц, Ч – 5 очков;
● Ш, Э, Ю – 8 очков;
● Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только
английские, либо только русские буквы.

Ввод:
ноутбук

Вывод:
12
'''
scrabble = {1: 'АЕВИНОРСТAEIOULNSTR', 2: 'ДКЛМПУDG', 3: 'БГЁЬЯBCMP', 4: 'ЙЫFHVWY', 5: 'ЖЗХЦЧK', 8: 'ШЭЮJX', 10: 'ФЩЪQZ'}  
n = int(input('Введите 0, если играем в английской раскладке,либо 1, если в русской: '))
text = input('Введите слово: ').upper()
cost_word = 0
for key, value in scrabble.items(): # items() позволяет обращаться к ключам и значениям одновременно – 
    for letter in text:             # если очередная буква в слове входит в одно из значений, 
        if letter in value:         # генератор добавит ключ в список 
            cost_word += key
print(cost_word)                                          


