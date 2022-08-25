def Python_Math_Quiz(prompt):
    return prompt [::-1] == prompt

word = input ("Input a wor: ")
if Python_Math_Quiz(word):
    print("{} is a palindrome".format(word))
else:
    print("Not a palindrome")
