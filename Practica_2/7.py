import string
texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""
mayus = [letter for letter in texto if letter.isupper()]
minus = [letter for letter in texto if letter.islower()]
special = [letter for letter in texto.replace(" ", "").replace("\n", "") if not letter.isalpha()]
words = [word for word in texto.lower().split() if word[0].isalpha()]

print(f'Theres {len(mayus)} upper chars in the text, and {len(minus)} lowercase chars in the text, and {len(special)} special chars in the text')
print(f'Theres {len(words)} words in the text')