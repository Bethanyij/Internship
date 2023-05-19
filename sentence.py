def ispalindrome(sentence):
  sentence= sentence.replace(" ","")

  if len(sentence) <=1:
    return True
  elif sentence [0] != sentence[-1]:
    return False
  else:
    return ispalindrome(sentence[1:-1])  
  
 

inputsentence= input("Enter a Sentence :")
if ispalindrome(inputsentence):
 print (inputsentence,"is a Palindrome.")
else:
  print (inputsentence,"is not a Palindrome.")


# mr owl ate my metal worm
# Do geese see God
# was it a car or a cat i saw