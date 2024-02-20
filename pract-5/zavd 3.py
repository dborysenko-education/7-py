integer = int(input("input an integer: "))

# спочатку потрібно прибрати всі 0 на початку числа: 
integer = str(integer)
while "0" in integer[0]:
    integer = integer[1:]

str_int = str(integer) # приведення до рядка числа без 0 на початку
len_int = len(str_int) # кількістсь символів до рядка

# визначаємо кількість дільників та кожен окремий дільник
dividers = [] 
for divider in range(0, len_int): 
    divider = "1" + "0" * divider # визнначаємо "розряд" кожного дільника
    dividers.append(divider) # записуємо в масив всі дільники (автоматично записується від 1 до найбільшого )
dividers = dividers[::-1] # змінюємо порядок дільникв

result = []
for i in range(0, len_int): 
    result.append(str_int[i] + "*" + dividers[i])

print(str_int+" = "+"+".join(result))

