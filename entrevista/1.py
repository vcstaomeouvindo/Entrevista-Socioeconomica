#ANTES DE RODAR: conferir se os nomes das colunas condizem com as colunas da planilha, conferir a viabilidade dos dados, conferir autodeclaração e outras observações

#importando o pandas
import pandas as pd
pd.options.mode.chained_assignment = None

#importando a planilha (ela deve estar na mesma pasta que o arquivo do código)
#x = input('Nome do arquivo da planilha, com extensão: ')
x = 'Entrevista Socioeconômica - TSI 2023 (respostas).xlsx'
df = pd.read_excel(x)

#removendo as colunas inúteis e renomeando
#é possível mudar o nome das colunas conforme for o arquivo, mas ter cuidado para mudar em todas as instâncias em que o nome é mencionado
#se atentar a ordem, mas ela pode ser alterada, já que o programa identifica a coluna com base no nome
data_cols = ['Número de Identificação', 'Número do Pedido', 'Nome COMPLETO', 'Como o candidato se autodeclara?', 'Quantas pessoas moram com o candidato? (INCLUINDO O CANDIDATO)', 'Quantas pessoas tiveram a identidade com documentos completos comprovados  (INCLUINDO O CANDIDATO)', 'Caso seja necessário, informar número de pessoas com comprovação incompleta (apresentação de documento sem foto, como CPF, declaração de perda sem BO, etc) ',  'Renda do candidato', 'Tipo de comprovação de renda do candidato apresentada:', 'Renda do pai (se ele morar com você)', 'Tipo de comprovação de renda do pai apresentada:', 'Renda da mãe (se ela morar com você)', 'Tipo de comprovação de renda da mãe apresentada:', 'Renda dos irmãos/filhos (se eles morarem com você)', 'Tipo de comprovação de renda dos irmãos/filhos apresentada:', 'Renda do cônjuge', 'Tipo de comprovação de renda do cônjuge apresentada:', 'Renda vinda de outras fontes', 'Tipo de comprovação de renda vinda de outras fontes apresentada:', 'Renda vinda de fontes externas', 'Tipo de comprovação de renda vinda de fontes externas:', 'Quantos imóveis a família possui? (SEM CONTAR A SUA PRÓPRIA CASA, EM QUE RESIDE)', 'A casa em que o candidato mora é?', 'Valor do aluguel: residencial, comercial e valor do condomínio (se possuir)', 'Tipo de comprovação do aluguel apresentada:', 'IPTU (valor total) – correspondente à imóveis e terrenos', 'Tipo de comprovação de IPTU', 'Conta de água', 'Tipo de comprovação de conta de água apresentada:', 'Conta de luz', 'Tipo de comprovação de conta de luz apresentada:', 'Conta de Telefone (fixo + celulares pré e pós pagos)', 'Tipo de comprovação de conta de telefone apresentada', 'Internet e TV a Cabo', 'Tipo de comprovação de conta de Internet e TV a cabo apresentada', 'Transporte (particular e público + vale transporte)', 'Educação (em andamento)', 'Tipo de comprovação de educação', 'Assistência Médica e/ou Odontológica', 'Tipo de comprovação de médica ou odontológica', 'Outros gastos (Valor)', 'Tipo de comprovação de outros gastos', 'Quantos carros sua família possui?', 'Quantas motos sua família possui?', 'IPVA (valor total) + DPVAT – correspondente à veículos', 'Tipo de comprovação de IPVA', 'Imposto de Renda a Pagar', 'Tipo de comprovação de IR', 'Imposto de Renda a Restituir ', 'Tipo de comprovação de IR.1', 'Dívidas (valor total de ser pago) – empréstimos, consórcios, carnês, financiamentos, agiota, membro da família, etc.', 'Tipo de comprovação de Dívidas', 'Onde você estudou no Ensino Médio?', 'Se você está no Ensino Médio, que ano está cursando?', 'Caso tenha estudado em escola particular no ensino médio, possuía bolsa?', 'Tipo de comprovação de Escolaridade', 'Nível de Escolaridade do Pai', 'Nível de Escolaridade da Mãe']

df_aj = df[data_cols]

new_cols = ['Número de Identificação', 'Número do Pedido', 'Nome', 'decl_racial', 'fam', 'fam_comp', 'fam_inc',  'renda_c', 'renda_c_conf', 'renda_p', 'renda_p_conf', 'renda_m', 'renda_m_conf', 'renda_if', 'renda_if_conf', 'renda_conj', 'renda_conj_conf', 'renda_out', 'renda_out_conf', 'renda_ext', 'renda_ext_conf', 'imoveis', 'tipo_casa', 'aluguel', 'alugel_conf', 'iptu', 'iptu_conf', 'agua', 'agua_conf', 'luz', 'luz_conf', 'telefone', 'telefone_conf',  'internet', 'internet_conf', 'transp', 'edu', 'edu_conf', 'saude', 'saude_conf', 'outros_gastos', 'outros_gastos_conf', 'carros', 'motos', 'ipva', 'ipva_conf', 'ir_pagar', 'ir_pagar_conf', 'ir_rest', 'ir_rest_conf', 'dividas', 'dividas_conf', 'tipo_EM', 'ano_EM', 'bolsa_EM', 'EM_conf', 'escolaridade_p', 'escolaridade_m']

cols = {data_cols[i]: new_cols[i] for i in range(len(data_cols))}
#esse dicionário iguala o nome das colunas do forms com os novos nomes, portanto o index da coluna na lista data_cols deve ser o mesmo na lista new_cols

df_aj.rename(columns = cols, inplace = True)

#agora, com a tabela arrumada, podemos começar os cálculos (é possível conferir os critérios no drive)
#cálculo das confiabilidades da parte - a -
#membros da família
df_aj['fam_inc'] = df_aj['fam_inc'].fillna(0)

df_aj['fam_conf'] = df_aj['fam_comp'] * 2 + df_aj['fam_inc']

#rendas
def renda_conf(tipo):
    df_aj.loc[df_aj[tipo]=="Não declarou renda", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Apresenta um holerite (desde que o documento não tenha mais do que 6 meses)", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Declaração de próprio punho explicando alguma fonte sem formalização jurídica ou que não é possível apresentar comprovante (ex: uma pensão alimentícia, trabalhador autônomo)", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Documento de aposentadoria", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Carteira de trabalho: página com o emprego e salário mais recente, incluindo também a página de identificação (formato digital ou físico)", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Documentos do governo comprovando o valor de algum auxílio", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Não apresentou um documento comprobatório", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Extratos ou prints da conta do banco (ex: um print alegando que entraram R$1500 na conta)", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Apresentou um holerite com mais de 6 meses.", tipo] = 0

renda_conf('renda_c_conf')
renda_conf('renda_p_conf')
renda_conf('renda_m_conf')
renda_conf('renda_if_conf')
renda_conf('renda_conj_conf')
renda_conf('renda_out_conf')
renda_conf('renda_ext_conf')

def res_renda(tipo, tipo_conf, nomecol):
    df_aj[nomecol] = df_aj[tipo] * df_aj[tipo_conf]

res_renda('renda_c', 'renda_c_conf', 'res_renda_c')
res_renda('renda_p', 'renda_p_conf', 'res_renda_p')
res_renda('renda_m', 'renda_m_conf', 'res_renda_m')
res_renda('renda_if', 'renda_if_conf', 'res_renda_if')
res_renda('renda_conj', 'renda_conj_conf', 'res_renda_conj')
res_renda('renda_out', 'renda_out_conf', 'res_renda_out')
res_renda('renda_ext', 'renda_ext_conf', 'res_renda_ext')

#renda total
df_aj['rendat'] = df_aj[['res_renda_c', 'res_renda_p','res_renda_m','res_renda_if','res_renda_conj','res_renda_out','res_renda_ext']].sum(axis = 1)

#pontuação renda total
pont_rendat = []
for i in df_aj['rendat']:
    if (i >= 0) and (i < 882):
        pont_rendat.append(20)
    elif (i >= 882) and (i < 1242):
        pont_rendat.append(18)
    elif (i >= 1242) and (i < 1350):
        pont_rendat.append(15)
    elif (i >= 1350) and (i < 1600):
        pont_rendat.append(12)
    elif (i >= 1600) and (i < 2520):
        pont_rendat.append(9)
    elif (i >= 2520) and (i < 4800):
        pont_rendat.append(6)
    elif (i >= 4800) and (i < 5500):
        pont_rendat.append(3)
    elif (i >= 5500):
        pont_rendat.append(0)

df_aj['pont_rendat'] = pont_rendat

print([df_aj['pont_rendat']])

#pontuação renda per capita
df_aj['rendapc'] = df_aj['rendat'] / df_aj['fam_conf']

df_aj['rendapc'] = df_aj['rendapc'].fillna(0)

pont_rendapc = []
for i in df_aj['rendapc']:
    if (i >= 0) and (i < 245):
        pont_rendapc.append(30)
    elif (i >= 245) and (i < 345):
        pont_rendapc.append(26)
    elif (i >= 345) and (i < 450):
        pont_rendapc.append(22)
    elif (i >= 450) and (i < 580):
        pont_rendapc.append(18)
    elif (i >= 580) and (i < 700):
        pont_rendapc.append(14)
    elif (i >= 700) and (i < 900):
        pont_rendapc.append(10)
    elif (i >= 900) and (i < 1345):
        pont_rendapc.append(6)
    elif (i >= 1345):
        pont_rendapc.append(2)

df_aj['pont_rendapc'] = pont_rendapc

print([df_aj['pont_rendapc']])