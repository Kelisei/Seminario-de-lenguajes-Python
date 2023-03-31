import string
"""Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de
palabras sin distinguir entre mayúsculas y minúsculas, en la frase."""

texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""

words = texto.split()
upper = 0
lower = 0
special = 0
for word in words:
    if word[0].islower():
        lower += 1
    elif word[0].isupper():
        upper += 1
    else:
        special += 1
print(f"There's {lower} lower, {upper} upper, {special} specials, and {upper + lower} words")