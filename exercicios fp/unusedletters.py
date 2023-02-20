inputStr = input("Enter a text string: ")
text = inputStr.upper()

# TODO: define a set named notUsed that contains the letters of
# the alphabet that are not contained in the user entered string.
notUsed = set()
lst =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for letter1 in text:
   if letter1 in lst:
      lst.remove(letter1)
   else:
      continue
for letter in lst:
   notUsed.add(letter)
for element in sorted(notUsed) :
   print(element, end="")
print()