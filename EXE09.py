# Escreva um programa que peça ao usuário para inserir três números inteiros, some os DOIS primeiros e multiplique esse total pelo terceiro. exiba o resultado da operação com a seguinte mensagem : "O total é: [?]"

num1 = int (input ("Insira o primeiro número: "))
num2 = int (input ("Insira o segundo número: "))
num3 = int (input ("Insira o terceiro número: "))

resultado = (num1 + num2) * num3
print ("O total é:", resultado)