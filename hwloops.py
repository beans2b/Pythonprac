"""HW1"""

result=0 
count=0
while result < 50:
    i = int(input("Enter a number: "))
    if i < 0:
        print("Negative numbers are ignored")
    else:
        result = result + i
        print(result)
        count += 1
   
print("Result Reached: ")
print("Valid numbers: ", count)

    
"""HW2
isValid = False
while isValid == False:
    word = input("Enter a word: ")
    allowed = ['a','b','c','d','e','A','B','C','D','E','1','2','3','4','5']
    index = 0
    uppercount=0
    lowercount=0
    digitcount=0
    invalid = 0
    
    while index < len(word):
        wordindex= word[index]
        if wordindex.islower():
            lowercount += 1
        if wordindex.isupper():
            uppercount += 1
        if wordindex.isdigit():
            digitcount += 1
        if wordindex not in allowed:
            invalid +=1

        index+= 1 

    if uppercount == 0:
        print("missing uppercase")
    if digitcount == 0:
        print("missing digit")
    if lowercount == 0:
        print("missing lowercase")
    if invalid > 0:
        print("invalid input")

    if uppercount > 0 and lowercount > 0 and digitcount > 0 and invalid ==0 :
        print("Valid word accepted!")
        isValid = True
    
    """

    
