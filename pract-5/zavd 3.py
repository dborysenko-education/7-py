integer = int(input("input an integer: "))

# def exclude_starting_zeroes(digit): 
#     digit = str(digit)
#     while "0" in digit[0]:
#         digit = digit[1:]
#     return int(digit)

# integer = exclude_starting_zeroes(integer)   

integer = str(integer)
while "0" in integer[0]:
    integer = integer[1:]


str_int = str(integer)
#print(str_int)
#print(integer)
len_int = len(str_int)
#print(len_int)
total = []

dividers = []
for divider in range(0, len_int):
    divider = "1" + "0" * divider
    dividers.append(divider)
dividers = dividers[::-1]
#print(dividers)

result = []
for i in range(0, len_int): 
    result.append(str_int[i] + "*" + dividers[i])
    

print(str_int+" = "+"+".join(result))

