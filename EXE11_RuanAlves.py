# escreva um programa que pergunte o nome do aniversariante, em seguida pergunte a sua idade, acrescente mais 1 e exiba:  nome do aniversariante seguida da mensagem "no proximo aniversario você terá " idade + "anos"

nome = input ("Qual o seu nome? ")
idade = int (input ("Qual a sua idade? "))
if idade < 0:
    print ("Idade inválida! Por gentileza, insira uma idade válida.")
else:
    print (nome,", no próximo aniversário você terá", idade + 1, "anos")

