"""
Faça um programa que receba uma frase e retorne:

(a) (1,0 ponto) Quantidade de vogais que há na entrada. Exemplo: Se a entrada é ‘Olá, eu sou
estudante de Fundamentos de Programação’ então a saída será: No total há 21 vogais na
entrada Olá, eu sou estudante de Fundamentos de Programação. Se a entrada é
‘lkjhgfdmnbv’ então a saída será: ‘Não há vogais na entrada lkjhgfdmnbv’.

(b) (1,0 ponto) Quantidade de cada vogal. Exemplo: Se a entrada é ‘Olá, eu sou estudante de
Fundamentos de Programação’ então a saída será: ‘Há 6 A's, 6 E's, 0 I's, 5 O's e 4 U's.’


1. Receber uma frase;
2. Contar quantas vogais há;
3. Contar quanto de cada vogal há.

"""

frase = input("Digite uma frase: ")
quantVogais = 0


vogais = ["a", "á", "ã", "â",
"e", "é", "ê",
"i", "í",
"o", "ó", "ô", "õ",
"u", "ú", "ü",
"A", "Á", "Â", "Ã",
"E", "É", "E",
"I", "Í",
"O", "Ó", "Ô", "Õ",
"U", "Ú", "Ü"]

i = 0

tamanhoVogais = len(vogais)
print("tamanhoVogais", tamanhoVogais)
auxiliar = [0]*tamanhoVogais
print("auxiliar", auxiliar)

letras= []
for c in frase:
    letras.append(c)
print(letras)


for letra in letras:
    j = 0
    for vogal in vogais:
        print("letra", letra, "vogal", vogal)
        if letra == vogal:
            quantVogais = quantVogais + 1
            auxiliar[j] = auxiliar[j] + 1
        print(j)
        j+=1


print(quantVogais)
for passo in range(len(auxiliar)):

    print("Quantidade de vezes que a letra", vogais[i] , "aparece é ", auxiliar[i])
    i+=1