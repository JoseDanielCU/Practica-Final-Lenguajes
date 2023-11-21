import os
Diccionario = {}
letras = 'abcdefghijklmnopqrstuvwxyz'
for letra in letras:
    with open(f'dict_rae_txt/{letra}.txt', 'r', errors='ignore') as f:
        palabras = f.read().splitlines()
        Diccionario[letra] = palabras


