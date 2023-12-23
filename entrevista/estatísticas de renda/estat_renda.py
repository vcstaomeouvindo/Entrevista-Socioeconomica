import pandas as pd
pd.options.mode.chained_assignment = None

#importando a planilha (ela deve estar na mesma pasta que o arquivo do código)
x = input('Nome do arquivo da planilha, com extensão: ')
df = pd.read_excel(x)

#removendo as colunas inúteis e renomeando
#é possível mudar o nome das colunas conforme for o arquivo, mas ter cuidado para mudar em todas as instâncias em que o nome é mencionado
#se atentar a ordem, mas ela pode ser alterada, já que o programa identifica a coluna com base no nome
data_cols = ['Número do Pedido','Quantas pessoas moram com o candidato? (INCLUINDO O CANDIDATO)', 'Quantos documentos o candidato apresentou de pessoas que moram com ele (INCLUINDO O CANDIDATO)', 'Caso seja necessário, informar número de pessoas com comprovação incompleta (apresentação de documento sem foto, como CPF, declaração de perda sem BO, etc) ',  'Renda do candidato', 'Tipo de comprovação de renda do candidato apresentada:', 'Renda do pai (se ele morar com você)', 'Tipo de comprovação de renda do pai apresentada:', 'Renda da mãe (se ela morar com você)', 'Tipo de comprovação de renda da mãe apresentada:', 'Renda dos irmãos/filhos (se eles morarem com você)', 'Tipo de comprovação de renda dos irmãos/filhos apresentada:', 'Renda do cônjuge', 'Tipo de comprovação de renda do cônjuge apresentada:', 'Renda vinda de outras fontes', 'Tipo de comprovação de renda vinda de outras fontes apresentada:', 'Renda vinda de fontes externas', 'Tipo de comprovação de renda vinda de fontes externas:']

df_aj = df[data_cols]

new_cols = ['Número do Pedido', 'fam', 'fam_comp', 'fam_inc',  'renda_c', 'renda_c_conf', 'renda_p', 'renda_p_conf', 'renda_m', 'renda_m_conf', 'renda_if', 'renda_if_conf', 'renda_conj', 'renda_conj_conf', 'renda_out', 'renda_out_conf', 'renda_ext', 'renda_ext_conf']

cols = {data_cols[i]: new_cols[i] for i in range(len(data_cols))}
#esse dicionário iguala o nome das colunas do forms com os novos nomes, portanto o index da coluna na lista data_cols deve ser o mesmo na lista new_cols

df_aj.rename(columns = cols, inplace = True)

#agora, com a tabela arrumada, podemos começar os cálculos (é possível conferir os critérios no drive)
#cálculo das confiabilidades da parte - a -
#membros da família
df_aj['fam_inc'] = df_aj['fam_inc'].fillna(0)

df_aj['fam_conf'] = df_aj['fam_comp'] * 2 + df_aj['fam_inc']

df_aj['fam_conf'] = df_aj['fam_conf'] / 2

#rendas
def renda_conf(tipo, tipo2):
    df_aj.loc[df_aj[tipo]=="Não apresentou um documento comprobatório", tipo2] = 0
    df_aj.loc[df_aj[tipo]=="Extratos ou prints da conta do banco (ex: um print alegando que entraram R$1500 na conta)", tipo2] = 0
    df_aj.loc[df_aj[tipo]=="Apresentou um holerite com mais de 6 meses.", tipo2] = 0

renda_conf('renda_c_conf', 'renda_c')
renda_conf('renda_p_conf', 'renda_p')
renda_conf('renda_m_conf', 'renda_m')
renda_conf('renda_if_conf', 'renda_if')
renda_conf('renda_conj_conf', 'renda_conj')
renda_conf('renda_out_conf', 'renda_out')
renda_conf('renda_ext_conf', 'renda_ext')

#renda total
df_aj['rendat'] = df_aj[['renda_c', 'renda_p','renda_m','renda_if','renda_conj','renda_out','renda_ext']].sum(axis = 1)

#renda per capita
df_aj['rendapc'] = df_aj['rendat'] / df_aj['fam_conf']

df_aj['rendapc'] = df_aj['rendapc'].fillna(0)

#exportando pra excel
arq_exp = input('Nome da planilha para exportar, com extensão (a planilha será criada na mesma pasta onde se encontra o arquivo do programa e a planilha inicial com os dados): ')

df_aj.to_excel(arq_exp)