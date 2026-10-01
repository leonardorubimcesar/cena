#!/usr/bin/env python3

# Exercício 2
taxa = 'sapiens, erectus, neanderthalensis' #instrução 1 - Criar string
print(taxa) #instrução 2 - imprimir a string
print(taxa[1]) #instrução 3- imprimir taxa[1]
print(type(taxa)) #instrução 4 - imprimir o tipo da variável taxa
split_taxa = taxa.split(', ') #instrução 5 - dividir a string em uma lista de strings
print(split_taxa)
species = split_taxa #instrução 6 - criar uma lista de strings a partir da variável split_taxa
print(species) #instrução 7 - imprimir a lista de strings species
print(species[1]) #instrução 8 - imprimir species[1]
print(type(species)) #instrução 9 - imprimir o tipo da variável species
species_sorted = sorted(species) #instrução 10 - ordenar a lista species em ordem alfabética
species_tamanho = sorted(species, key = len) #instrução 11 - ordenar a lista species pelo tamanho da string
print(species_tamanho) 