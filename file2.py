
#циклы while и for in, вложенные циклы
count = 0 #переменная-счетчик
number = int(input('enter number:'))

while count < 500:
    count += number
    number += 1
    print(count)
print(number - 1)

while True:
    print('Hello world')
    number+=1 #бесконечный цикл
    if number > 10:
        break #оператор break для принудительной остановки цикла

while (1000 * 1.08) < 3000:
    number += 1
print(number+1)

employee = 5
while number < employee:
    if 1 < number:
        print(number, 'people in the departament')
    if 1 == number:
        print(number, 'people in the departament')
    number +=1


for i in range(1, number + 1):
    count += i
    print('sum value after addition:', count)

for i in range(number+1):
    star = i*'*'
    print(star)

matrix = [[1,2],
          [3,4],
          [5,6]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

rows = 3
cols = 2
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

min_value_rows = []
min_index_rows =[]
random_matrix = [
   [9, 2, 1],
   [2, 5, 3],
   [4, 8, 5]
]

for row in random_matrix:
    min_index = 0
    min_value = row[min_index]
    for element in range(len(row)):
        if row[element]<min_value:
            min_value = row[element]
            min_index = element
    min_index_rows.append(min_index)
    min_value_rows.append(min_value)
print(min_index_rows)
print(min_value_rows)

max_value_row = []
max_index_row = []
random_matrix = [
   [9, 266, 1],
   [233, 5, 3],
   [4, 8, 566]
]
for row in random_matrix:
    max_index = 0
    max_value = row[max_index]
    for element in range(len(row)):
        if row[element] > max_value:
            max_value = row[element]
            max_index = element
    max_index_row.append(max_index)
    max_value_row.append(max_value)
print(max_index_row)
print(max_value_row)

list_ = [34, -23, 0, 123, 12, -34, 2]
negative_index = None

for index, value in enumerate(list_):
    if value < 0:
        negative_index = index
print(negative_index)

text = '''
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
'''
text = text.replace("\n", "")
text = text.lower()
text =  text.replace(" ", "") 
count = {}
for count_text in text:
    if count_text in count:
        count[count_text] += 1
    else:
        count[count_text] = 1
for char, cnt in count.items():
    print(f'element {char} met in the text {cnt}')

text = text.lower()
text = text.replace('\n', ' ')
text = text.split()
count_words = {}
for count_word in text:
    if count_word in count_words:
        count_words[count_word] +=1
    else:
        count_words[count_word] =1
for a, b in count_words.items():
    print(f'{a} in {b}')


heads = 35
legs = 94

for r in range(heads + 1):
    for ph in range(heads + 1):
        if (r+ph)> 35 or \
            (r * 4 + ph * 2) > 94:
                continue
        if (r+ph) == 35 and  (r * 4 + ph * 2) == 94:
             print('value rabbit:', r)
             print('value phazan:', ph)

numbers = int(input('enter number:'))

while numbers // 10:
    if numbers % 10 == 5:
        print('в введенном числе есть цифра 5')
        numbers //= 10
        continue
    elif numbers % 10 == 7:
        print('в введенном числе есть цифра 7')
        numbers //= 10
    elif numbers % 10 == 9:
        print('в введенном числе есть цифра 9')
        numbers //= 10
    numbers = numbers // 10
    if numbers < 1:
        break