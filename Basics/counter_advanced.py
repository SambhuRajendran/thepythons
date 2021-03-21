txtfile = open("D:\english-words\words_alpha.txt", "r")
wordtofind = input("Enter a string to find the occurences?")
user_list = []
for words in txtfile:
    result = words.find(wordtofind)
    user_list.append(result)

print(user_list)
print(f'The searched word appeared {len(user_list)} times in the text file')