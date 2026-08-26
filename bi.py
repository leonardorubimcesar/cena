#!/usr/bin/env python3
import sys
numero = int(sys.argv[1])
if numero % 400 == 0:
    message = 'é um ano bissexto'
    print(numero, message)
elif numero % 4 == 0 and numero % 100 != 0:
    message = 'é um ano bissexto'
    print(numero, message)
else:
    message = 'não é um ano bissexto'
    print(numero, message)

