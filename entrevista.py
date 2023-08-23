##Iniciando entrevista

nome = input("Nome do candidato: ")

cpf = input("CPF do candidato: ")

inscr = input("Número de inscrição: ")

fam = int(input("Número de pessoas na família: "))

confiabilidade = {
        "A" : 2,
        "B" : 2,
        "C" : 2,
        "D" : 2,
        "E" : 2,
        "F" : 2,
        "G" : 0,
        "H" : 0,
        "I" : 0
        }

print(''' Tipo de comprovação (coloque A, B, C, etc.):
          A. Não declarou renda
          B. Apresenta um holerite (desde que o documento não tenha mais do que 6 meses)
          C. Declaração de próprio punho explicando alguma fonte sem formalização jurídica ou que não é possível apresentar comprovante (ex: uma pensão alimentícia, trabalhador autônomo)
          D. Documento de aposentadoria
          E. Carteira de trabalho: página com o emprego e salário mais recente, incluindo também a página de identificação (formato digital ou físico)
          F. Documentos do governo comprovando o valor de algum auxílio
          G. Não apresentou um documento comprobatório
          H. Extratos ou prints da conta do banco (ex: um print alegando que entraram R$1500 na conta)
          I. Apresentou um holerite com mais de 6 meses.''')
          
rendac = int(input('Insira a renda do candidato: '))   
 
conf1 = input("Selecione uma alternativa: ")

rendaccon = rendac * confiabilidade[conf1]
    
rendap = int(input("Insira a renda do pai: "))
    
conf2 = input("Selecione uma alternativa: ")
    
rendapcon = rendap * confiabilidade[conf2]

rendam = int(input("Insira a renda da mãe: "))

conf3 = input("Selecione uma alternativa: ")

rendamcon = rendam * confiabilidade[conf3]

rendaif = int(input("Insira da renda dos irmão/filhos: "))



rendacon = int(input("Insira a renda do cônjuge: "))

rendaout = int(input("Insira a renda de outras fontes: "))

rendaext = int(input("Insira a renda de fontes externas: "))

renda = rendaccon + rendapcon + rendam + rendaif + rendacon + rendaout + rendaext

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
print("Pontuação de renda total: ",prenda)

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
print("Pontuação de renda per capita: ",prendapc)

aluguel = int(input('Insira o valor do aluguel (se não tiver, coloque 0): '))

iptu = int(input('Insira o valor do IPTU: '))

agua = int(input('Insira o valor da conta de água: '))

luz = int(input('Insira o valor da conta de luz: '))

tel = int(input('Insira o valor da conta de telefone: '))

net = int(input('Insira o valor da conta de internet e TV: '))

transp = int(input('Insira gasto com transporte mensal: '))

edu = int(input('Insira gasto com educação: '))

saude = int(input('Insira gasto com plano de saúde: '))

outg = int(input('Insira outros gastos: '))

ipva = int(input('Insira o valor do IPVA: '))

irp = int(input('Insira o valor do IR a pagar: '))

irr = int(input('Insira o valor do IR a restituir: '))
