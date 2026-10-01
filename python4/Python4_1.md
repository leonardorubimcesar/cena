#Exercício 1
>>> fav = ['gatos', 'brownie', 'roxo', 'queijo', 'poesia'] #comando 1 - criar uma lista de 5 coisas que eu gosto
>>> print(fav) #comando 2 - imprimir lista
['gatos', 'brownie', 'roxo', 'queijo', 'poesia']
>>> print(fav[2]) #comando 3 - imprimir elemento do meio
roxo
>>> fav[2] = 'canario' #comando 4 - substituir item do meio
>>> print(fav) #comando 5 - imprimir nova lista
['gatos', 'brownie', 'canario', 'queijo', 'poesia']
>>> fav.append('roxo') #comando 6 - adicionar novo elemento no fim
>>> print(fav)
['gatos', 'brownie', 'canario', 'queijo', 'poesia', 'roxo']
>>> fav.insert(0, "papel") #comando 7 - adicionar novo elemento no início
>>> print(fav)
['papel', 'gatos', 'brownie', 'canario', 'queijo', 'poesia', 'roxo']
>>> fav.insert(3, "cacau") #comando 8 - adicionar novo elemento no meio
>>> print(fav)
['papel', 'gatos', 'brownie', 'cacau', 'canario', 'queijo', 'poesia', 'roxo']
>>> fav.pop(7) #comando 9 - remover elemento no fim
'roxo' #diferente de .insert(), o método .pop() imprime o elemento que será eliminado da lista
>>> print(fav)
['papel', 'gatos', 'brownie', 'cacau', 'canario', 'queijo', 'poesia']
>>> fav.pop(0) #comando 10 - remover elemento no início
'papel' 
>>> print(fav)
['gatos', 'brownie', 'cacau', 'canario', 'queijo', 'poesia']
>>> fav.pop(3) #comando 11 - remover elemento no meio
'canario'
>>> print(fav)
['gatos', 'brownie', 'cacau', 'queijo', 'poesia']
>>> string_fav = ','.join(fav) #comando 12 - criar string com elementos restantes
>>> print(string_fav)
gatos,brownie,cacau,queijo,poesia