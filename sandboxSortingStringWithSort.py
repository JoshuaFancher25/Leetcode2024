# learning how to sort a string
word = "world"

# sorted wont change the underlying structure of the word but returns a sorted array
# the word itself remains unchanged
# the sorted() function breaks apart the iterable word and returns an array of letters
# that are sorted in lexicographical order
print(sorted(word))
print(word)