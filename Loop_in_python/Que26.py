#  find the total number of vowels in a given string and print all the vowels present in the string.
    


text = input("Enter a sentance: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:                    
        count = count + 1

print("Total vowels:", count)




text = input("Enter a sentence: ")
vowels = "aeiouAEIOU"

for i in range(0, len(text), 1):
    if text[i] in vowels:
        print(text[i], end=' ')