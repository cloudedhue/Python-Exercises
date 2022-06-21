
def idkMan(spam):
    spamString = ', '.join(map(str, spam[:len(spam)-1]))
    spamString = spamString + ' and ' + str(spam[len(spam)-1])
    return spamString

spam = ['apples', 'bananas', 'tofu', 'cats']

spamString = idkMan(spam)
print(spamString)
