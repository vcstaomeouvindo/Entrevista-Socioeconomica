##Iniciando entrevista

nome = input("Nome do candidato: ")

cpf = input("CPF do candidato: ")

inscr = input("Numero de inscricao: ")

fam = int(input("Numero de pessoas na familia: "))

renda = int(input('Insira a renda: '))

if (renda >= 0) and (renda < 882):
    prenda = 20
elif (renda >= 882) and (renda < 1242):
    prenda = 18
elif (renda >= 1242) and (renda < 1350):
    prenda = 15
elif (renda >= 1350) and (renda < 1600):
    prenda = 12
elif (renda >= 1600) and (renda < 2520):
    prenda = 9
elif (renda >= 2520) and (renda < 4800):
    prenda = 6
elif (renda >= 4800) and (renda < 5500):
    prenda = 3
elif (renda >= 5500):
    prenda = 0
print(prenda)

rendapc = renda / fam

if (rendapc >= 0) and (rendapc < 245):
    prendapc = 30
elif (rendapc >= 245) and (rendapc < 345):
    prendapc = 26
elif (rendapc >= 345) and (rendapc < 450):
    prendapc = 22
elif (rendapc >= 450) and (rendapc < 580):
    prendapc = 18
elif (rendapc >= 580) and (rendapc < 700):
    prendapc = 14
elif (rendapc >= 700) and (rendapc < 900):
    prendapc = 10
elif (rendapc >= 900) and (rendapc < 1345):
    prendapc = 6
elif (rendapc >= 1345):
    prendapc = 2
print(prendapc)
