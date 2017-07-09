import time

pyg = "ay"

print("Welcome to the Pig Latin Translator!")
time.sleep(1)
original = input("Enter a word: ") 
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_ori = word+first+pyg
    new_ori = new_ori[1:len(new_ori)]
    time.sleep(.5)
    print("In Pig Latin: %s is %s" %(original, new_ori))
else:
    print('sorry, this word won\'t do')

