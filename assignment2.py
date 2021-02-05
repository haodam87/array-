# palindrome=input(("Enter a word:"))
# if(palindrome==palindrome [::-1]):
#       print("Yes")
# else:
#       print("No")
def palindrome():

    word= input("Enter a word:")
    originalword = []
    palindromecheck = []

    for index in range(0, len(word)):
        originalword.append(word[index])
        print(originalword)

    for index in range(len(word) -1, -1, -1):
        palindromecheck.append(word[index])
        print(palindromecheck)
    
    for index in range(0, len(word)):
        if originalword[index] != palindromecheck[index]:
            return input('This is not a Palindrome')
        return input("This is a Palindrome")

print(palindrome())