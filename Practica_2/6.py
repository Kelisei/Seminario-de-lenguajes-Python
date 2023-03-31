word = input('Introduce a word: ')
match 'a' in word, 'n' in word: 
    case True, True: 
        print('a and n are in the word')
    case True, _:
        print('Only a is in the word')
    case _, True:
        print('Only n is in the word')
    case _,_:
        print('No letter a or n are in the word')