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
4. Havendo números, informe o maior, o menor e a média de todos os números com duas casas decimais apenas como resultado. - ok

"""
##Requisição de input do usuário
numero = input("Digite um número para iniciar ou tecle enter para terminar")

## Ponto de checagem caso nenhum número seja informado. 
## Se um número for informado, eu o transformo em int
## e depois atribuo esse valor às outras variáveis.
## Isso me permite inicializá-las para poder trabalhar com elas
## nas operações de comparação e soma dentro do while mais abaixo.

if numero == "":
    print("Nenhum número foi lido – A primeira linha lida foi vazia!!!")
else:
    numero = int(numero)
    soma = numero
    numeroMaior = numero
    soma = numero
    numeroMenor = numero

## Variável para ser usada no cálculo da média. 
## Ela precisa ser zero mesmo com um input já feito, pois
## se o valor informado for "" ele pulará o while e irá para o if
## mais abaixo. Eu poderia configurar de outras formas, mas essa 
## foi a que encontrei para fazer o programa funcionar mais adequadamente
## sem ter que alterar muito o código já feito.
i=0

## Comparo a variável para que o while não seja iniciado erroneamente.
while numero != "":
    
    numero = input("Digite um número para iniciar ou tecle enter para terminar")
    
    ## Como eu preciso usar a função int() para transformar a variável "numero",
    ## eu preciso fazer a verificação ou será gerado um erro de 
    ## "invalid literal for int() with base 10: '' "
    if numero != "":
        numero = int(numero)
   
        ## somo numero à soma que foi inicalizada com o primeiro número informado
        soma = numero + soma

        ## Comparo o novo número infomado com o inicial
        if numero > numeroMaior:
            numeroMaior = numero
        elif numero < numeroMenor:
            numeroMenor = numero
    ## Esse +1 é adicionado mesmo que o valor seja "" para sair do código para compensar
    ## pelo +1 que não foi adicionado no input fora do laço while.
    i+=1


## Utilizo um if pois se não digitar nada na entrada gerará
## erro. Se o 'i' for maior que '1' significa que o programa rodou ao menos uma vez
if i != 0:
    print("A soma é: ", soma)
    print("O número menor é: ", numeroMenor)
    print("O número maior é: ", numeroMaior)
    print("A média dos números é: ", "%.2f" % (soma/(i)))