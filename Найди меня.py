import random
a = [random.randint(0,10) for i in range(10)]
print(a)
x = int(input("Введите число: "))
if x in a:
    a.index(x)
    print("Число", x, "Находится в списке по номером", a.index(x))
if x not in a:
    print("Этого числа нет в списке")