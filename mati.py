#!/usr/bin/env python3
numero = 51
if numero < 0:
    message = 'negativo'
    print(message)
elif numero > 0 and numero < 50 and numero % 2 == 0:
    message = 'é um número par menor que 50'
    print(número, message)
elif numero > 0 and numero < 50 and numero % 2 != 0:
    message = 'é um número ímpar menor que 50'
    print(numero, message)
elif numero > 0 and numero > 50 and numero % 3 == 0:
    message = 'é maior que 50 e divisível por 3'
    print(numero, message)
elif numero > 50 and numero % 3 != 0:
    message = 'é maior que 50 e não divisível por 3'
    print(numero, message)
else:
    message = 'deve ser 0 ou 50'
    print(numero, message)


