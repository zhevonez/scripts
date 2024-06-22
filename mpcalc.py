import math

mp = float(input("Введите вашу MP: "))
otvet = 29.97 * (math.log(0.0019 * mp + 1)) ** 1.2
print("Ваш множитель статистики:", otvet)