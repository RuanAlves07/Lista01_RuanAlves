#Escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem, divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida da mensagem "cada cliente deve pagar: [x valor]"

valtotal = int (input ("Qual foi o valor total da conta? "))
qntclientes = int (input ("Qual a quantidade de clientes existentes? "))

resultado = valtotal / qntclientes

print ("Cada cliente deve pagar: R$",resultado)