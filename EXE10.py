# Escreva um programa que pergunte quantos pedaço o bolo tem, em seguida pergunte ao usuário quantos pedaço ele comeu, calcule quantos pedaços ainda tem e exiba o resultado como uma mensagem de livre escolha

quantped = int (input ("Quantos pedaços o bolo tem? "))
quantcom = int (input ("Quantos pedaços você comeu? "))

resultado = quantped - quantcom

print ("O bolo no total tinha", quantped, "pedaços e você comeu", quantcom, "pedaços, sobrou no total:", resultado ,"pedaços")