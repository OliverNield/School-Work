word = input('Input your word to be translated')
length = len(word)
i = 0
counter = 0
output = ['a','b']
for i in range(length):
    temp = word[i]
    print(temp)
    if temp in ['a','e','i','o','u','A','E','I','O','U']:
        print('vowel')
        output[counter] = temp
        counter = counter + 1
        print(counter,output)
    else:
        print('not vowel')
print(output)