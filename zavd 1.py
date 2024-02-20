
# завдання 1: 
#1 рекомендація -> оцінка
#2 університет -> турист
#3 чиновник -> новини
#4 спортсмен -> метро

input = ["рекомендація", "університет", "чиновник", "спортсмен"]

# hint -> get indexes
for word in input: 
    for index, letter in enumerate(word): 
        print(f"{letter} -> {index}")
    print("\n")
        

r1 = input[0][3]+input[0][9:11]+input[0][6]+input[0][2]+input[0][8]
r2 = input[1][8]+input[1][0]+input[1][5]+input[1][7]+input[1][6]+input[1][8]
r3 = input[2][2:5]+input[2][1]+input[2][5:7]
r4 = input[3][6:8]+input[3][-5:-8:-1]

output = [r1, r2, r3, r4]



for word in range(0, len(input)): 
    print(f"{input[word]} -> {output[word]}")
