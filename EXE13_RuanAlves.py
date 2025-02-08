# Escreva um programa que solicite um determinado número de dias, em seguida exiba o quanto esses dias equivalem em horas, minutos e segundos

dias = int (input("Quantos dias serão determinados? "))

horas = dias * 24
minutos = dias * 1440
segundos = dias * 86400

print ("Pela quantidade de dias escolhendo sendo",dias,"dias foram no total:\n",horas,"horas\n",minutos,"minutos \n",segundos,"segundos")