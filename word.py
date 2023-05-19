def wordpalindrome (word):
    return word == word[ : : -1]

def ispalindrome(sentence):
    sen= sentence.split()
    for word in sen :
        if not wordpalindrome(word):
            return False
    return True

inputsentence = input("Enter a sentence: ")
if ispalindrome(inputsentence):
    print ("Every word in this sentence is a palindrome.")
else:
   print ("Not every word in this sentence is a palindrome.")

