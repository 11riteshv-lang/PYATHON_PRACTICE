# reverce given number and given word 



n = int(input('Enter a number: '))

for i in range(n, 0, -1):
    print(i, end=' ')

print()
    
word = input('Enter a word: ')

for i in range(len(word) - 1, -1, -1):
    print(word[i], end=' ')