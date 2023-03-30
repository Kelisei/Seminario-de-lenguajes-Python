import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""

words = jupyter_info.split()
letter = input('Input a letter ').lower()

if (len(letter) == 1) and (letter in string.ascii_lowercase):
    for word in words:
        if word.lower().startswith(letter):
            print(word)
else:
    print('Not a word bozo')