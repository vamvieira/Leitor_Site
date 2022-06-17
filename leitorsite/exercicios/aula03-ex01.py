

alunos ={}
for i in range(5):
    ra=int(input('Informe o RA: '))
    nota1 = float(input('Informe a 1a nota: '))
    nota2 = float(input('Informe a 2a nota: '))
    nota3 = float(input('Informe a 3a nota: '))
    lista = [nota1, nota2, nota3]
    alunos[ra] = lista

print(alunos)

for chave in alunos:
    media = sum(alunos[chave] / len(alunos[chave]))
    print(media)


