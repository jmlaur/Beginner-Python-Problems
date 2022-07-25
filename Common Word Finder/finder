file = open('text.txt')
test = dict()
for line in file:
    x = line.split()
    for word in x: 
        test[word] = test.get(word, 0) + 1
maxWord = max(test, key=test.get)
print("Most common word:", maxWord + ":", test[maxWord])
