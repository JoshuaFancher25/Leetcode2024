# function to determine if a string is a plindrome
# civic level racecar tacocat
def isPalindrome(s):
    if s == s[::-1]:
        return True
    return False

word = "Aa"
word2 = "tacocat"
word3 = "racecar"
word4 = "asdfasaaa"
print(isPalindrome(word))
print(isPalindrome(word2))
print(isPalindrome(word3))
print(isPalindrome(word4))
print(1//2)