
initial_words = ["школа", "книга", "голуб", "зошит", "аркуш"]
expected_results = ["шшккооллаа", "нкгиа", "гбоблбуббб", "10791086109610801090", "бслфщ"]
words = ["школа", "книга", "голуб", "зошит", "аркуш"]
#words = ["Тимофій", "Василь", "Ангеліна", "Костянтин", "Квазимодо"]
word_1 = words[0] # кожна буква подвоєна
word_2 = words[1] # слово разбите на пари букв, кожна пара букв у зворонбому порядку
word_3 = words[2] # після кожною букви відображати останню букву в слові
word_4 = words[3] # вивести замість букв значення їх символьних кодів
word_5 = words[4] # взяти за основу символьний код кожної букви, додати 1 до нього, відобразити відповідні букви



r1 = ""
r2 = ""
r3 = ""
r4 = ""
r5 = ""

#1 
for letter in word_1:
    r1 += letter*2
#print("1 : ", r1)

#2 
w2_pairs = []
for i in range(0, len(word_2), 2):
    pair = word_2[i:i+2]
    w2_pairs.append(pair[::-1])
r2 = "".join(w2_pairs)  
#print("2 : ", r2)


#3
last_letter_index = len(word_3)-1
for letter in word_3:
    r3 += letter+word_3[last_letter_index]
#print("3 : ", r3)

#4 
for letter in word_4:
    r4 += str(ord(letter))
#print("4 : ", r4)

#5 
w5_letter_codes = []
for letter in word_5:
    w5_letter_codes.append(ord(letter)+1)

w5_new_letters = []
for letter_code in w5_letter_codes: 
    w5_new_letters.append(chr(letter_code))
r5 = "".join(w5_new_letters)

#print("5 : ", r5)
    
results = [r1, r2, r3, r4, r5]

def check_initial_results(initial_words, current_words, expected_results, current_result, index): 
    if initial_words != current_words: 
        #print("You used other set of words")
        return ""
    else: 
        if current_result == expected_results[index]: 
            return ", status: OK"
        else: 
            return ", status: FAIL"

result = []
i = 0
for word in words: 
    result.append( [words[i], results[i]] )
    
    print(f"{words[i]} -> {results[i]}{check_initial_results(initial_words, words, expected_results, results[i], i)}")
    i += 1