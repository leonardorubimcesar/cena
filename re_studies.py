#!/usr/bin/env python3

# importar biblioteca re
import re 

# importar biblioteca urlopen para captar arquivo do repositório
from urllib.request import urlopen

# link do arquivo do repositório
# url = "https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07_nobody.txt"

# permite que arquivo txt seja usado como string
# with urlopen(url) as resposta:
#     texto = resposta.read().decode("utf-8")

# Exercício 1 - encontrar posição da palavra Nobody
# for found in re.finditer(r'(Nobody)', texto):
#     whole = found.group(0)
#     up       = found.group(1)
#     up_start = found.start(1) + 1   # é necessário converter da notação 0 para 1 
#     up_end   = found.end(1) 
    # print("posição:",up_start, up_end , sep="\t" )

# Exercício 2 - substituir e criar arquivo
# new_str = re.sub(r'Nobody', 'Daniel', texto)
# print(new_str)
# with open('Daniel.txt', 'w', encoding='utf-8') as arquivo:
#     arquivo.write(new_str)

# Exercício 3 - encontrar cabeçalho em arquivo .fasta
# fasta = "https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07.fasta"

# with urlopen(fasta) as repost:
#     text = repost.read().decode("utf-8")

# for found in re.finditer(r'(>.+ .+)', text):
#     whole = found.group(0)
#     print(whole)

# Exercício 4 
# if re.finditer(r'(>.+ .+)', text):
# codigo = re.search(r"(>(\S+)\s+(.*))",text)
# codigo = re.search(r"(>(\S+))",text)
# codigo = re.search(r"((>\S+)(\s+.*))",text)
# print("id:", codigo.group(3))

# for found in re.finditer(r"((>\S+)(\s+.*))",text):
#     print("id:", found.group(2), "descrição:", found.group(3))

# Exercício 6
#R - A ou G
#Y - C ou T

# dna = "https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07_ApoI.fasta"
# with urlopen(dna) as rta:
#     seq = rta.read().decode("utf-8")

# found = re.findall(r'[AG]AATT[CT]',seq)
# print(found)

# Exercício 7

# found = re.search(r'([AG])(AATT[CT])', seq)
# new_str = re.sub(r'[AG]AATT[CT]', found.group(1) + '^' + found.group(2), seq)
# print(new_str)

# Exercício 8
# new_str = new_str.replace('\n', '')
# sep = new_str.split('^')
# print(sorted(sep, key = len))

# species_tamanho = sorted(species, key = len)

# Exercício 9 
# with open("bionet.txt", "r", encoding="utf-8") as arquivo:
#     texto = arquivo.read()
# linhas = texto.splitlines()
# dados = linhas[10:]
# print(dados[:5])

# enzimas = {}

# with open("bionet.txt", "r", encoding="utf-8") as arquivo:
#     linhas = arquivo.readlines()

# for linha in linhas[10:]:
#     colunas = linha.split()

#     if len(colunas) >= 2:
#         nome = colunas[0]
#         padrao = colunas[1]
#         enzimas[nome] = padrao

# print(enzimas)

# Exercício 11

# identificadores = [
#     "EXP2026_B03_P12", "EXP2026_B3_P12", "EXP2026_B03_P2", "exp2026_B03_P12", "EXP2026_B03_P12_extra"
# ]

# padrão = r'^EXP\d{4}_B\d{2}_P\d{2}$'

# for nome in identificadores:
#     if re.match(padrão, nome):
#         print(f'{nome:<25} -->, Válido') #isso faz com que formatação da resposta seja melhor do que sem f'{}...
#     else:
#         print(f'{nome:<25} -->, Inválido')

# Exercício 12

# lista = []

# url = "https://github.com/labbces/cen0336/blob/master/files/pH.txt"

# from urllib.request import urlopen

# p = r"(S[0-9]{2}): pH ?= ?(\d[;.]?\d?);$"

# with urlopen(url) as resposta:
#     texto = resposta.read().decode("utf-8")

# found = re.search(p, texto)

# for line in texto:
#     if line:
#         print(line.group(1), line.group(2))
#     else:
#         print('não')


#___resolução do professor___

# url = "https://github.com/labbces/cen0336/blob/master/files/pH.txt"

# from urllib.request import urlopen

# with urlopen(url) as resposta:
#     texto = resposta.read().decode("utf-8")

# lista = []
# p = r"(S[0-9]{2}): pH ?= ?(\d[;.]?\d?);$"
# with open (texto, 'r') as fh:
#     for line in fh:
#         line = line.rstrip()
#         res = re.search(p, line)
#         if res:
#             l = [res.group(1), res.group(2)]
#             lista.append(l)
# print(lista)


# Exercício 13

import re
import sys

if len(sys.argv) !=2:
    print("Provide input file")
    exit()

dicionario = {'soja': "soja",
            "soja comum":'soja',
            'Glycine max':'soja',
            'cana de açúcar':'cana',
            'cana':'cana',
            'cana-de-açúcar':'cana',
            'cana de acucar':'cana',
            'cana-de-acucar':'cana',
            'milho':'milho',
            'milho comum':'milho',
            'Zea mays':'milho'}

file = sys.argv[1]
with open(file, 'r') as data: 
    for line in data:
        newline = line.rstrip()
        new = newline.lower()
        new1 = new.split('\t')
        print(new1)


