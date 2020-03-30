#Identificadores

#- Não começam com números
#- Não pode ter caractere especial
#- Não pode ter espaço entre as letras


palavrasReservadas = ['int','float','char','if','else']
operadoresRelacionais = ['>','<','>=','<=','!=','==']
simbolosTerminais = ['=',',',';','(',')','{','}']
numeros = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
arquivo = open('prof.txt', 'r')
lista = arquivo.readlines() # readlinesssssss
arquivo.close()

print(lista)
for index, val in enumerate(lista):
    lista[index] = val.replace('\n','')

print(lista)

for terminal in simbolosTerminais:
    for index, val in enumerate(lista):
        lista[index] = val.replace(terminal,' ' + terminal + ' ')

print(lista)
for operador in operadoresRelacionais:
    for index, val in enumerate(lista):
        lista[index] = val.replace(operador,' ' + operador + ' ')

print(lista)

for index, val in enumerate(lista):
    lista[index] = val.replace('  ',' ')

print(lista)
for index, val in enumerate(lista):
    lista[index] = val.strip()

print(lista)
for index, val in enumerate(lista):
    lista[index] = val.split(' ')

print(lista)


listaFinal = []
for i in lista:
    listaFinal.extend(i)


print(listaFinal)

for token in listaFinal:
    if token in palavrasReservadas:
        print(token + ' - Palavra Reservada')
    elif token in operadoresRelacionais:
        print(token + ' - Operador Relacional')
    elif token in simbolosTerminais:
        print(token + ' - Simbolo Terminal')
    elif token in numeros:
        print(token + ' - Numero')
    else:
        print(token + ' - Identificador')
    
    