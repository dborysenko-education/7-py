integer = input("input an integer: ")
# визначаємо позитивне чи негативне число ввів користувач
negative = False
if integer[0] == "-":
    integer = integer[1:]
    negative = True

# відфільтровуємо все, що не є виключно цілочисленними значеннями
if integer.isdigit() == False:
    print("Only numbers are accepted!")
    exit()

# прибраємо всі 0 на початку числа: 
while "0" in integer[0]:
    integer = integer[1:]

<<<<<<< Updated upstream
len_int = len(integer) # кількістсь символів у числі
int_chars = range(0, len_int)
# визначаємо кількість дільників та кожен окремий дільник
dividers = [] 
for divider in int_chars: 
=======
len_int = len(integer) # кількістсь символів до рядка
chars_number = range(0, len_int)

# визначаємо кількість дільників та кожен окремий дільник
dividers = [] 
for divider in chars_number: 
>>>>>>> Stashed changes
    divider = "1" + "0" * divider # визнначаємо "розряд" кожного дільника
    dividers.insert(0, divider) # записуємо в масив всі дільники (автоматично записується від 1 до найбільшого )

<<<<<<< Updated upstream
result = []
for i in int_chars: 
    result.append(integer[i] + "*" + dividers[i])
beautiful_result = '+'.join(result)

print(f"{integer} = {beautiful_result}")
=======

results = []
for i in chars_number: 

    if negative == True: 
        result = f"((-{integer[i]})*{dividers[i]})"
        minus = "-"
    else: 
        result = f"{integer[i]}*{dividers[i]}"
        minus = ""
    results.append(result)

beautiful_result = ' + '.join(results)

print(f"{minus}{integer} => {beautiful_result}")
>>>>>>> Stashed changes
