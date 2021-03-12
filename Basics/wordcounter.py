txtfile = open("D:\english-words\words_alpha.txt", "r")
wordtofind = input("Enter a string to find the occurences?")
user_list = []
for words in txtfile:
    if wordtofind == words:
        print('matched')
        #print(wordtofind)
        user_list.append(words)

print(user_list)
print(f'The searched word appeared {len(user_list)} times in the text file')
