#Условные и логические операторы
numbers = input('Enter numbers:')
print('3' and '7' in numbers)
print(int(numbers[0])%2==0)
password = "dgh36gh7"
answer = input()

if password == answer:
    print("Пароль верен! Добро пожаловать.")
else:
    print("Вы ввели неверный пароль")
number = int(input('Enter number:'))
if number % 2 == 0 or number % 3 == 0:
    print('a multiple of two or tree')

one = int(input('Enter number:'))
two  = int(input('Enter number:'))

if one and two:
    result = True
else:
    result = False
x = int(input('enter number:'))
y = int(input('enter number:'))
if x > 0 and y > 0:
    print('First quarter')
if x > 0 and y < 0:
    print('Second quarter')
if x < 0 and y < 0:
    print('Three quarter')
if x < 0 and y > 0:
    print('fourth quarter')

season = int(input('enter month:'))
if season in [5, 4, 3]:
    print('spring')
elif season in [6, 7, 8]:
    print('summer')
elif season in [9, 10, 11]:
    print('autumn')
elif season [12, 1, 2]:
    print('winter')
wind = int(input('enter wind speed:'))
if wind <= 0:
    print('Error')
elif 1 >= wind <= 4:
    print('weak')
elif 5 >= wind <= 10:
    print('moderate')
elif 11 >= wind <= 18:
    print ('strong')
else:
    print('hurricane')

a = int(input())
b = int(input())
c = int(input())
print(True if (a < 45 and b >= 45 and c >= 45) or  (b < 45 and a >= 45 and c >= 45) or (c < 45 and b >= 45 and a >= 45) else False)

numberA = 1
print((numberA < -10 and numberA > -1) or (numberA<2 and numberA >15))

palindrome = list(input('check for palirome:'))
if palindrome == palindrome[::-1]:
    print('that palindrome')
else:
    print('that is not palindrome')

temperature = int(input('what is the temperature?'))
precipitation = input('is there any precipitation?')
if 20 < temperature < 30:
    if precipitation == 'yes':
        print('футболку,шорты и дождевик')
    elif precipitation == 'no':
        print('футболку и шорты')

else:
    if temperature < 0:
        print('пуховик')
    else:
        if precipitation == 'no':
            print('Пальто')
        else:
            is_rain_heavy = input('is it raining heavily outside?')
            if is_rain_heavy == 'yes':
                print('Пальто, резиновые сапоги и зонт')
            elif is_rain_heavy == 'no':
                print('Пальто и дождевик')


    