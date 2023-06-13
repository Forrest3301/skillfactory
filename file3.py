import time
#фунциии-итераторы/декораторы/генераторы
def print_2_add_2 ():
    print(2+2)
print_2_add_2()

def hello_world():
    print("Hello world")
hello_world()

def divider(n, a = 2):
    if n % a == 0:
        print(True)
    else:
        print(False)
divider(9, 3)
 
def stars(n):
    for i in range(n, 0, -1):
        print('*'*i)
stars(4)

def div(number):
    divider_ = 0
    for i in range(1, number+1):
        if number % i == 0:
            divider_ += 1
    return divider_
print(div (14))

def palindrome (word):
    word = word.lower()
    word = word.replace(' ','')
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome('Beb'))
    
x = 10
def func():
    'print(x)' #ошибка по попричине того, что переменная внутри функции вызывается до того, как ее обьявляют внутри функции
    'global x' #чтобы это исправить - необходимо дать понять программе, что мы используем глобальную переменную
    x = 5
    x += 23
    return x
print(func())

def get_mul_local_func(m):
    nonlocal_m = m
    def local_func(n):
        return nonlocal_m * n
    return local_func
two_mul = get_mul_local_func(5)
print(two_mul(2))

def adder (*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_
print(adder(10))

def adder_2 (*args):
    sum_ = 1
    for i in args:
        sum_ *= i
    return sum_
print(adder_2(5,6,99))

def correct_func(args=None):
    if args is None:
        args=[]
    args.append(1)
    return args
print(correct_func([6]))

def adder_recurs(num):
    if num == 1:
        return 1
    return num + adder_recurs(num - 1)
print(adder_recurs(3))

def str_recurs(str_):
    if len(str_)==0:
        return ''
    else:
        return str_[-1]+str_recurs(str_[:-1])
print(str_recurs('test'))

def reverse_num(N):
    if N < 10:
        return N
    else:
        return N % 10 + reverse_num(N // 10)
print(reverse_num(234))

def fib():
    a, b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
for num in fib():
    print(num, end=' ')

def itegers(start=1, step=1):
    counter = start
    while True:
        yield counter
        counter += step
for i in itegers():
    print(i)

def subsequence(sub_gen):
    list_value = sub_gen.copy()
    while True:
        value = list_value.pop(0)
        list_value.append(value)
        yield value
for i in subsequence([1,2,3]):
    print(i)


#Decorator

N = int(input('сколько раз повторить программу:'))
def dec_decorator(decorator):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        print('выполняюсь до основного вызова')
        decorator(*args, **kwargs)
        print('выполняюсь после основного вызова')
        dt = time.time() - t0
        print(f'функция выполнилась за {dt:.25f}')
        return dt
    return wrapper

@dec_decorator
def my_func():
    print('основной вызов')

my_func()

counter = 0
for i in range(N):
    counter += my_func()

print(f'функция{my_func} выполнилась {N} раз. Среднее время выполнения: {counter/N:.25f}')

def decorator(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        fn(*args, **kwargs)
        count += 1
        print(f'функция {fn} была вызвана {count}')
    return inner

@decorator
def func():
    print('проверка')

for i in range (10):
    func()

def f(arg):
    return arg * 123456789

def my_decorat(fn):
    count = {}
    def wrapper(args):
        nonlocal count
        if args not in count:
            count[args] = fn(args)
            print(f'Добавление результата в кэш{count[args]}')
        else:
            print(f'Возвращение результата в кэш{count[args]}')
        return count[args]
    return wrapper

f = my_decorat(f)
print(f(2))

