# найти сумму отрицательных чисел
# (подсказка) вы должны только расматривать только отрицательные числа
# рушить нужно двумя способами while, for
my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15, -18]
total = 0
i = -4
while my_list[i] < 0:
    total += my_list[i]
    i += 1
total1 = 0
for e in my_list:
    if e < 0:
        total1 += e
print(total)
print(total1)
