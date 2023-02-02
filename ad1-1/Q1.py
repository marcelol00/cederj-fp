### Marcelo da Silva de Almeida
### Matrícula = 20213050157

"""
1a Questão (2,0 pontos)
Faça um programa na Linguagem Python 3 que leia da entrada padrão linhas de texto até
que uma linha vazia seja digitada. Com exceção da linha vazia, todas as demais possuem
números inteiros. Seu programa deve escrever na saída padrão a mensagem “Nenhum
número foi lido – A primeira linha lida foi vazia!!!”, caso a primeira linha lida não contenha
nenhum número. Caso contrário, escreva o menor número lido, o maior número lido e a
média dos números lidos, com precisão de duas casas decimais, conforme teste a seguir

1. Ler entradas de texto até que uma linha vazia seja digitada - ok
2. As entradas precisam ser convertidas em números inteiros após serem lidas - ok
3. Informar "Nenhum número foi lido – A primeira linha lida foi vazia!!!" caso nada seja informado na primeira linha. - ok
4. Havendo números, informe o maior, o menor e a média de todos os números com duas casas decimais apenas como resultado.

"""
## Inicialização de variáveis
numero = 0
i=0
numeros=[]
soma = 0

## Início do loop while que compara a variável numero com com "" para então começar.
while numero != "":

    numero = input("Digite um número para iniciar ou tecle enter para terminar")

    ## Ponto de checagem caso nenhum número seja informado. Como essa checagem deve ser feita apenas na primeira vez,
    ## eu utilizo a variável "i" para fazer o controle da entrada do programa no "if". Eu logo adiciono +1 à "i" para que 
    ## possa-se sair do programa sem aparecer a imagem abaixo.
    if numero == "" and i == 0:
        print("Nenhum número foi lido – A primeira linha lida foi vazia!!!")
        break
    ## Como eu preciso usar a função int() para transformar a variável "numero",
    ## eu preciso fazer aplicar essa saída "prévia" do laço quando o usuário clicar informar ""
    ## ou será gerado um erro de "invalid literal for int() with base 10: '' "
    if numero == "":
        break


    ## Converto e adiciono o valor da variável numero na lista numeros
    numero = int(numero)
    numeros.append(numero)
    print(i)


    ## somo numero à soma que foi inicalizada com 0 e 
    soma = numero + soma


    i+=1

i = 0

for num1 in numeros:
    for num2 in numeros:
        if num1 >= num2:
            numeroMaior = num1
        else:
            numeroMaior = num2

    for num2 in numeros:
        if num1 < num2:
            numeroMenor = num1
        else:
            numeroMenor = num2


    i+=1

if i != 0:
    print(soma)
    print(numeroMaior)
    print(numeroMenor)
    print("%.2f" % (soma/len(numeros)))


