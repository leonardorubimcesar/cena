#!/usr/bin/env python3

codons = {
    'GCU' : 'Alanina',
    'UGU' : 'Cisteína',
    'AUG' : 'Metionina',
    'UGA' : 'Stop',
    'UAA' : 'Stop'
}

print(codons.items())
print(list(codons.keys()))
codon = input('Coloque sua sequência de códons: ' )
codon2 = input('Coloque sua sequência de códons: ' )
print("Sua sequência de aminoácidos é: ", codons[codon], codons[codon2])
