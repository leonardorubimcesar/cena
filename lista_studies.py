#!/usr/bin/env python3

#Exercício 1
#fav = ['gatos', 'brownie', 'roxo', 'queijo', 'poesia'] #comando 1
#print(fav) #instrução 2 - imprimir a lista
#print(fav[2]) #instrução 3 - imprimir elemento do meio

#fav[2] = 'canario' #instrução 4 - alterar elemento do meio
#print(fav) #instrução 5 - imprimir a lista alterada

#fav.append('roxo')  #instrução 6 - adicionar elemento no final da lista
# fav.insert(0, "papel") #instrução 7 - adicionar elemento no início da lista
# fav.insert(3, "cacau") #instrução 8 - adicionar elemento no meio da lista
# fav.pop(6) #instrução 9 - remover elemento do final da lista
# fav.pop(0) #instrução 10 - remover elemento do início da lista
# fav.pop(3) #instrução 11 - remover elemento do meio da lista
# string_fav = ','.join(fav) #instrução 12 - transformar a lista em string

#print(fav) 
# print(string_fav)

# Exercício 2
# taxa = 'sapiens, erectus, neanderthalensis' #instrução 1 - Criar string
# print(taxa) #instrução 2 - imprimir a string
# print(taxa[1]) #instrução 3- imprimir taxa[1]
# print(type(taxa)) #instrução 4 - imprimir o tipo da variável taxa
# split_taxa = taxa.split(', ') #instrução 5 - dividir a string em uma lista de strings
# print(split_taxa)
# species = split_taxa #instrução 6 - criar uma lista de strings a partir da variável split_taxa
# print(species) #instrução 7 - imprimir a lista de strings species
# print(species[1]) #instrução 8 - imprimir species[1]
# print(type(species)) #instrução 9 - imprimir o tipo da variável species
#species_sorted = sorted(species) #instrução 10 - ordenar a lista species em ordem alfabética
# species_tamanho = sorted(species, key = len) #instrução 11 - ordenar a lista species pelo tamanho da string
# print(species_tamanho) 

# Exercício 3
# my_list = ['a', 'bb', 'ccc']#instrução 1 - criar uma lista de strings
# list_copy = my_list #instrução 2 - criar uma cópia da lista my_list
# print(my_list) #instrução 3 - imprimir a lista my_list
# list_copy.append('dddd') #instrução 4 - adicionar um elemento à lista list_copy
# print(my_list) #instrução 5 - imprimir a lista my_list novamente para verificar se a lista foi alterada
# list_copy2 = my_list.copy() #instrução 6 - criar uma cópia da lista my_list usando o método copy()
# print(my_list) #instrução 7 - imprimir a lista my_list
# list_copy2.append('dddd') #instrução 8 - adicionar um elemento à lista list_copy2
# print(my_list) #instrução 9 - imprimir a lista my_list novamente para verificar se a lista foi alterada

# Exercício 4 - imprimir de 0 a 100
# contagem = 0
# while contagem < 101:
    # print('contagem: ', contagem)
    # contagem+=1

# Exercício 5 - calcular o fatorial de 1000
# contagem = 1000
# fatorial = 1
# while contagem > 1:
    # fatorial = fatorial * contagem
    # contagem = contagem - 1 #à medida que contagem diminui até 0, o fatorial vai aumentando até o valor final
# print(fatorial)

# Exercício 6
# p = [101,2,15,22,95,33,2,27,72,15,52]
#  for num in p:
#     if num % 2 == 0:
#         print(num)

# Exercício 7
# p_ordenada = sorted(p)
# print(p_ordenada)
# soma_pares = 0
# soma_impares = 0
# for num in p:
#     if num % 2 == 0:
#         soma_pares += num
#     else:
#         soma_impares += num
# print ('Soma dos números pares: ',soma_pares, '\nSoma dos números ímpares: ', soma_impares)

# Exercício 8
# for num in range(100):
    # print(num)

# Exercício 9
# for num in range(101):
    # if num > 0:
        # print(num)

# Exercício 10
# import sys
# count = int(sys.argv[1])
# while count < 100:
#     print(count)
#     count+=1 
#     if count > int(sys.argv[2]):
#         break
# while count < 100:
#     if count % 2 != 0: #para imprimir apenas número ímpares
#         print(count)
#     count+=1
#     if count > int(sys.argv[2]):
#         break

# Exercício 11
sequencias = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#   parte 1 - imprimir sequencias
#for sequencia in sequencias:
#   print(sequencia)
#   parte 2 - imprimir comprimento das sequencias + sequencias
# print(len(sequencia), sequencia)

# Exercício 12 - imprimir lista de tuplas 
# tuplas = [(len(seq), seq) for seq in sequencias]
# print(tuplas)

# Exercício 13
for sequencia in sequencias:
    print(sequencias.index(sequencia) + 1, len(sequencia), sequencia)