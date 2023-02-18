"""
Faça um programa que receba uma frase e retorne:

(a) (1,0 ponto) Quantidade de vogais que há na entrada. Exemplo: Se a entrada é ‘Olá, eu sou
estudante de Fundamentos de Programação’ então a saída será: No total há 21 vogais na
entrada Olá, eu sou estudante de Fundamentos de Programação. Se a entrada é
‘lkjhgfdmnbv’ então a saída será: ‘Não há vogais na entrada lkjhgfdmnbv’.

(b) (1,0 ponto) Quantidade de cada vogal. Exemplo: Se a entrada é ‘Olá, eu sou estudante de
Fundamentos de Programação’ então a saída será: ‘Há 6 A's, 6 E's, 0 I's, 5 O's e 4 U's.’


1. Receber uma frase; ok
2. Contar quantas vogais há; ok
3. Contar quanto de cada vogal há. ok

"""

frase = input("Digite uma frase: ")
quantVogais = 0

## Lista de vogais que no final será usada como referência

vogais = ["a", "e", "i", "o", "u"]

## Eu precisei criar duas listas de vogais pois python é case sensitive

vogaisMinusculas = ["a", "á", "ã", "â", "à",
"e", "é", "ê",
"i", "í",
"o", "ó", "ô", "õ",
"u", "ú", "ü"]

vogaisMaiusculas = ["A", "Á", "Ã", "Â", "À",
"E", "É", "Ê",
"I", "Í",
"O", "Ó", "Ô", "Õ",
"U", "Ú", "Ü"]

## Recebendo o valor das vogais e criando uma lista auxiliar que armazenará
## a quantidade de cada uma delas de acordo com a posição de cada uma

vogaisAuxiliar = [0]*17

vogalAuxiliar = [0]*5

## Como não podemos usar métodos mais sofisticados, fiz uma iteração usando
## o 'for' para criar uma lista com cada letra na frase escrita.

letras= []
for c in frase:
    letras.append(c)


## Começo iterando pela frase e depois itero pelas duas listas de vogais.
## Já que todas as vogais encontram-se na mesma posição nas duas listas
## eu só preciso continuar incrementando mais à lista "auxiliar" que não
## terá erro. Eu uso "j=0" antes das iterações nas listas de vogais para 
## inicializar a variável e para não ocorrer estouro de lista quando
## for iterar a segunda lista de vogais.

for letra in letras:

    j = 0
    for vogal in vogaisMinusculas:
        if letra == vogal:
            quantVogais = quantVogais + 1
            vogaisAuxiliar[j] = vogaisAuxiliar[j] + 1
        j+=1

    j = 0
    for vogal in vogaisMaiusculas:
        if letra == vogal:
            quantVogais = quantVogais + 1
            vogaisAuxiliar[j] = vogaisAuxiliar[j] + 1
        j+=1


## Agora eu concateno todas as variações de acentos das vogais 
## na vogal minúscula, tornando, assim, menos extensa a lista
## a ser impressa.


j = 0
for total in vogaisAuxiliar:
    if j < 5:
        vogalAuxiliar[0] = vogalAuxiliar[0] + total
    elif j >= 5 and j < 8:
        vogalAuxiliar[1] = vogalAuxiliar[1] + total
    elif j >= 8 and j < 10:
        vogalAuxiliar[2] = vogalAuxiliar[2] + total
    elif j >= 10 and j < 14:
        vogalAuxiliar[3] = vogalAuxiliar[3] + total
    elif j >= 14 and j < 17:
        vogalAuxiliar[4] = vogalAuxiliar[4] + total

    j+=1




############
############

## Verifico se existem vogais, imprimo a quantidade de vogais
## e depois imprimo quantas vezes cada vogal é repetida.

############
############

tamanhoVogais = len(vogais)


if quantVogais != 0:
    print("No total há %i de vogais em '%s'" % (quantVogais, frase))
    print("Há %i A's, %i E's, %i I's, %i O's, %i U's " % (vogalAuxiliar[0], vogalAuxiliar[1], vogalAuxiliar[2], vogalAuxiliar[3], vogalAuxiliar[4],))
else:
    print("Não há vogais na entrada '%s'" % (frase))