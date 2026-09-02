#!/usr/bin/env python3

#Exercício 1
fav = ['gatos', 'brownie', 'roxo', 'queijo', 'poesia'] #comando 1
#print(fav) #instrução 2 - imprimir a lista
#print(fav[2]) #instrução 3 - imprimir elemento do meio

fav[2] = 'canario' #instrução 4 - alterar elemento do meio
#print(fav) #instrução 5 - imprimir a lista alterada

fav.append('roxo')  #instrução 6 - adicionar elemento no final da lista
fav.insert(0, "papel") #instrução 7 - adicionar elemento no início da lista
fav.insert(3, "cacau") #instrução 8 - adicionar elemento no meio da lista
fav.pop(6) #instrução 9 - remover elemento do final da lista
fav.pop(0) #instrução 10 - remover elemento do início da lista
fav.pop(3) #instrução 11 - remover elemento do meio da lista
string_fav = ','.join(fav) #instrução 12 - transformar a lista em string

#print(fav) 
print(string_fav)