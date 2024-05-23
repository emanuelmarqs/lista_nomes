#lista
nomes = ['Alex', 'Simone', 'Natalia', 'Emanuel', 'Alexandra','Alice','Bedian','Caique','Dylan','Yago','Zurich']

# ordenando a lista em ordem alfabética
nomes.sort()

#nomes.sort(reverse = True) #ordena em ordem alfabetica inversamente

# for nome in nomes:  for simples
#     print(nome)

for i in range(len(nomes)):    #range é o tamanho da lista, saber quantas posições ela tem.
                           #len é uma função que tenta medir o tamanho da lista, enumera.
    print(f' {i + 1}° nome da lista: {nomes[i]}.')