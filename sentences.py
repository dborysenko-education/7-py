text = input("Enter free text: ")
# count_fs = text.count(".")
# count_em = text.count("!")
# count_qm = text.count("?")

# print(f"Nmber of sentences in this text is {count_fs + count_em + count_qm}")

deliminers = [".", "!", "?"]
sentences = 0
for delim in deliminers: 
    sentences += text.count(delim)

print(f"Nmber of sentences in this text is {sentences}")