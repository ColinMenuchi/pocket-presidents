def thing():
    global word
    word = 'cat'

def thingy():
    print(word)

    
thing()
word = word + 'c'
print(word)