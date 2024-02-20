
words = ["школа", "книга", "голуб", "зошит", "аркуш"]
word_1 = words[0]
word_2 = words[1]
word_3 = words[2]
word_4 = words[3]
word_5 = words[4]

for i in range(0, len(words)):
    word_[i+10] = words[i]

print(word_12)

r1 = ""
r2 = ""
r3 = ""
r4 = ""
r5 = ""

#1 
c = 0
for letter in word_1:
    r1 += word_1[c]*2
    c += 1
#print("1 : ", r1)

#2 
w2_pairs = []
for i in range(0, len(word_2), 2):
    pair = word_2[i:i+2]
    w2_pairs.append(pair[::-1])
r2 = "".join(w2_pairs)  
#print("2 : ", r2)


#3
c=0
last_letter = len(word_3)-1
#print(last_letter)
#print(word_3[last_letter])
for letter in word_3:
    r3 += word_3[c]+word_3[last_letter]
    c += 1
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

result = []
i = 0
for word in words: 
    result.append( [words[i], results[i]] )
    print(f"{words[i]} -> {results[i]}")
    i += 1