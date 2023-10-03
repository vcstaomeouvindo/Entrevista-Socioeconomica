import pandas as pd

df = pd.read_excel('Entrevista Socioeconômica - TSI 2023 (respostas).xlsx')

fam = pd.Series(df['Quantas pessoas moram com o candidato? (INCLUINDO O CANDIDATO)'])

print(fam)

tiporenda = pd.Series(df["Tipo de comprovação de renda do candidato apresentada:"])

print(tiporenda)

listtiporenda = tiporenda.tolist()

confrenda = []

print(listtiporenda)

i = 0

while i < len(listtiporenda):
    
    for i in range(len(listtiporenda)):
        if i == 'Não declarou renda' :
            confrenda = 2
        elif i == 'Apresenta um holerite (desde que o documento não tenha mais do que 6 meses)': 
            confrenda = 2
        elif i == 'Declaração de próprio punho explicando alguma fonte sem formalização jurídica ou que não é possível apresentar comprovante (ex: uma pensão alimentícia, trabalhador autônomo)': 
            confrenda = 2
        elif i == 'Documento de aposentadoria': 
            confrenda = 2
        elif i == 'Carteira de trabalho: página com o emprego e salário mais recente, incluindo também a página de identificação (formato digital ou físico)': 
            confrenda = 2
        elif i == 'Documentos do governo comprovando o valor de algum auxílio': 
            confrenda = 2
        elif i == 'Não apresentou um documento comprobatório': 
            confrenda = 0
        elif i == 'Extratos ou prints da conta do banco (ex: um print alegando que entraram R$1500 na conta)': 
            confrenda = 0
        elif i == 'Apresentou um holerite com mais de 6 meses.': 
            confrenda = 0
    
        
        
print(confrenda)