import time as t

# ax^2 + bx + c = 0 (старый коммент для себя)
equation = input("Введите квадратное уравнение в его стандартном виде: ax^2 + bx + c = 0\n"
                 "P.S: Комплексных корней не существует)\n")
parsed_equation = equation.split()

if len(parsed_equation) != 7 or parsed_equation[6] != "0":
    print("Нужно было вводить в стандартном виде...")
    t.sleep(5)
    print("Goodbye:)")
    exit()

a = ""
b = ""
c = parsed_equation[4]
b_sign = parsed_equation[1]
c_sign = parsed_equation[3]

previous_each_value = ""
for each in parsed_equation[0]:
    if previous_each_value == "^":
        continue

    try:
        if int(each) or each == '0':
            a += each
    except ValueError:
        pass

    previous_each_value = each


for each in parsed_equation[2]:
    try:
        if int(each) or each == '0':
            b += each
    except ValueError:
        pass

if a == "":
    a = 1

if b == "":
    b = 1

a = int(a)
b = int(b)
c = int(c)

if b_sign == "-":
    b = -b

if c_sign == "-":
    c = -c

discriminant = b**2 - 4 * a * c
if discriminant < 0:
    print("У данного уравнения нет корней -- дискриминант меньше нуля.")
elif discriminant == 0:
    x1 = -b / (2 * a)
    print(x1)
elif discriminant > 0:
    x1 = (-b + discriminant**(1/2)) / (2 * a)
    x2 = (-b - discriminant**(1/2)) / (2 * a)
    print("Корни:", x1, x2)
