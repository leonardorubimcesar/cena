#!/usr/bin/env python3
import sys
numero = int(sys.argv[1])
if numero < 0:
    message = 'é negativo'
    print(numero, message)
elif numero > 0 and numero < 50 and numero % 2 == 0:
    message = 'é um número par positivo e menor que 50'
    print(numero, message)
elif numero > 0 and numero < 50 and numero % 2 != 0:
    message = 'é um número ímpar positivo menor que 50'
    print(numero, message)
elif numero > 50 and numero % 3 == 0:
    message = 'é um número maior que 50 e divisível por 3'
    print(numero, message)
elif numero > 50 and numero % 3 != 0:
    message = 'é um número maior que 50 e não divisível por 3'
    print(numero, message)
else:
    message = "deve ser 0 ou 50"
    print(numero, message)

