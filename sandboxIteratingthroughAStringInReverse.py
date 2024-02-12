# iterating through a string in reverse

word = "123456789"
print(len(word))

for i in range(len(word)-1, -1, -1):
    print(word[i])

print(word[::-1]) # to revers the string using list slicing

# using enumerate and a list to go over the string in reverse
word2 = "abcedfghijklmnopqrstuvwxyz"
for i, letter in reversed(list(enumerate(word2))):
    print(i, " : ", letter)


