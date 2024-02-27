integer = input("input an integer: ")

# визначаємо позитивне чи негативне число ввів користувач
negative = False
if integer[0] == "-":
    integer = integer[1:]
    negative = True

# відфільтровуємо все, що не є виключно цілочисленними значеннями
if integer.isdigit() == False:
    exit("Only numbers are accepted!")

# прибраємо всі 0 на початку числа: 
zeroes = 0
for i in range(0, len(integer)): 
    if integer[i] == "0": 
        zeroes += 1

if len(integer) == zeroes: 
    exit("you entered only zeroes")

while "0" in integer[0]:
    integer = integer[1:]

len_int = len(integer) # кількістсь символів 

if len_int != 4: 
    exit(f"Only 4-digit integers accepted, your integer has {len_int} digits!")

chars_number = range(0, len_int)

# визначаємо кількість дільників та кожен окремий дільник
dividers = [] 
for divider in chars_number: 
    divider = "1" + "0" * divider # визнначаємо "розряд" кожного дільника
    dividers.insert(0, divider) # записуємо в масив всі дільники (автоматично записується від 1 до найбільшого )

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