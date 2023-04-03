import string
text = input('Input a phrase or word: ').lower()
i = 0 
heterogram = True
while i < len(text) and heterogram:
    if text[i].isalpha() and text.count(text[i]) > 1:
        print("It isn't a heterogram")
        heterogram = False
    i+=1
if (heterogram):
    print("It's a heterogram")
