# Дан треугольник со сторонами a, b и c. Определите, является ли он равнобедренным.
# Формат входных данных: дано три натуральных числа. Гарантируется, что отрезки с данными длинами образуют треугольник.
# Формат выходных данных: Выведите «YES», если треугольник равнобедренный, и «NO» в противном случае.

# TODO: your code here
a = int(input("Ввод cторона a: "))
b = int(input("Ввод cторона b: "))
с = int(input("Ввод сторона c: "))

if a==b or b==c or c==a:
    print("Yes")
else:
    print("No")
