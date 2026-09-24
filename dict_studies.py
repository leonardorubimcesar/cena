#!/usr/bin/env python3

#Exercício 1 - criar um dicionário de coisas favoritas
# fav = {
#     'livro' : "Ensaio sobre a cegueira",
#     'música' : 'Homemade Dynamite',
#     'árvore' : 'Ipê'}

#Exercício 2 - imprimir livro 
# print(fav['livro'])

#Exercício 3 - imprimir livro com variável na chave
# fav_livro = 'livro' 
# print(fav[fav_livro]) 

# Exercício 4 - imprimir árvore favorita
# print(fav['árvore'])

# Exercício 5 - adicionar organismo favorito e imprimi-lo
# fav['organismo'] = 'felinos'
# fav_organismo = 'organismo'
# print(fav[fav_organismo])

# Exercício 6 - imprimir valor do dicionário a partir do valor na linha de comando
# print(list(fav.keys()))
# fav_coisa = input('Enter your input: ')
# print("Received input is: ", fav[fav_coisa])

# Exercício 7 - alterar valor de 'organismo'
# fav['organismo'] = 'felinos'
# fav_organismo = 'organismo'
# fav['organismo'] = 'bactérias'
# print(fav)

# Exercício 8 - substituir valor de chave por input do usuário
# fav['livro']= input('Insira seu valor:')
# print("Received input is: ", fav['livro'])

# Exercício 9 - usar loop for para imprimir cada chave e valor
# for favorito in fav:
#     item = fav[favorito]
#     print(favorito, item)

# Exercício 10 - criar conjunto com duas sintaxes diferentes
# mySet = set('ATGTGGG') #set() separa a string em elementos
# mySet2 = {'ATGCCT'} #{} não separa a string se os elementos não forem strings próprias
# mySet3 = 'ATGCCT'
# unique = set(mySet3) #daí agora também separa os elementos 
# mySet2 = {'A','T','G','C','C','T'}
# conjunto = mySet | mySet2
# print(conjunto)
# print(mySet)
# print(mySet2)
# print(unique)

# Exercício 11 - comparação dois conjuntos
# set_a = {'3', '14', '15', '9', '26', '5', '35', '9'}
# set_b = {'60', '22', '14', '0', '9'}
# Intersecção
# print('intersecção:', set_a&set_b)
# Diferença
# print('diferença de a-b: ',set_a-set_b)
# print('diferença de b-a: ',set_b-set_a)
# União
# print('união: ',set_a|set_b)
# Diferença simétrica
# print('diferença simétrica: ',set_a^set_b)

# Exercício 12 - criar conjunto a partir de sequência de DNA
seq =  set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC')
print(seq)