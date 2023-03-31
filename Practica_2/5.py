"""5. Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras, y
sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir entre
mayúsculas y minúsctrulas."""
phrase = input('Introduce a phrase: ')
word = input('Introduce a word: ')
print(f'The word is in the phrase {phrase.lower().count(word.lower())} times')