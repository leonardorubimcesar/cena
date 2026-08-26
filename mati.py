#!/usr/bin/env python3
numero = 49
if numero < 0:
    message = 'negativo'
    print(message)
elif numero > 0 and numero < 50:
    message = 'positivo e menor que 50'
    print(message)
elif numero > 0 and numero > 50:
    message = 'positivo e maior que 50'
    print(message)
else:
    message = 'deve ser 0 ou 50'
    print(numero, message)


