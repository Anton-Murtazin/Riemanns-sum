print('Введите количество точек разбиения')
n = int(input())
print('Выберите способ выбора точки внутри промежутка: левые, правые или центральные')
spo = input()
a = 1
b = 2
p = (b-a)/n
k = 1
sum = 0
ksi = 0
while k<=n:
    delx = 2 ** (k*p) - 2 ** ((k - 1)*p)
    if "правые" in spo:
        ksi = 2 ** (k*p)
    if "центральные" in spo:
        ksi = 2 ** ((k - 1)*p) + (- 2 ** ((k - 1)*p) + 2 ** (k*p))/2
    if "левые" in spo:
        ksi = 2 ** ((k - 1)*p)
    sum = sum + (1/ksi)*delx
    k = k + 1
print('Значение суммы Римана при выбранных параметрах составляет:',sum)
