#ANTES DE RODAR: conferir se os nomes das colunas condizem com as colunas da planilha, conferir a viabilidade dos dados, conferir autodeclaração e outras observações

#importando o pandas e o datetime
import pandas as pd
pd.options.mode.chained_assignment = None
import datetime as dt

#é importante já termos definidos os intervalos e a pontuação correspondente a cada faixa, SEMPRE REVISAR
#lembrar que os índices devem ser os mesmos
intervalos_renda_total = [(0, 1099), (1100, 1463), (1464, 1799), (1800, 2180), (2181, 2598), (2599, 3099), (3100, 3795), (3796, 4983), (4984, 10000000000000)]
pontos_renda_total = [20, 18, 15, 12, 9, 6, 3, 1, 0]
intervalos_renda_pc = [(0, 359), (360, 499), (500, 637), (638, 757), (758, 916), (917, 1111), (1112, 1401), (1402, 1952), (1953, 10000000000000)]
pontos_renda_pc = [30, 26, 22, 18, 14, 10, 6, 2, 0]

#importando a planilha (ela deve estar na mesma pasta que o arquivo do código)
#x = input('Nome do arquivo da planilha, com extensão: ')
x = 'Entrevista Socioeconômica - TSI 2023 (respostas).xlsx'
df = pd.read_excel(x)

#removendo as colunas inúteis e renomeando
#é possível mudar o nome das colunas conforme for o arquivo, mas ter cuidado para mudar em todas as instâncias em que o nome é mencionado
#se atentar a ordem, mas ela pode ser alterada, já que o programa identifica a coluna com base no nome
data_cols = ['Número de Identificação', 'Número do Pedido', 'Nome COMPLETO', 'Como o candidato se autodeclara?', 'Quantas pessoas moram com o candidato? (INCLUINDO O CANDIDATO)', 'Quantas pessoas tiveram a identidade com documentos completos comprovados  (INCLUINDO O CANDIDATO)', 'Caso seja necessário, informar número de pessoas com comprovação incompleta (apresentação de documento sem foto, como CPF, declaração de perda sem BO, etc) ',  'Renda do candidato', 'Tipo de comprovação de renda do candidato apresentada:', 'Renda do pai (se ele morar com você)', 'Tipo de comprovação de renda do pai apresentada:', 'Renda da mãe (se ela morar com você)', 'Tipo de comprovação de renda da mãe apresentada:', 'Renda dos irmãos/filhos (se eles morarem com você)', 'Tipo de comprovação de renda dos irmãos/filhos apresentada:', 'Renda do cônjuge', 'Tipo de comprovação de renda do cônjuge apresentada:', 'Renda vinda de outras fontes', 'Tipo de comprovação de renda vinda de outras fontes apresentada:', 'Renda vinda de fontes externas', 'Tipo de comprovação de renda vinda de fontes externas:', 'Quantos imóveis a família possui? (SEM CONTAR A SUA PRÓPRIA CASA, EM QUE RESIDE)', 'A casa em que o candidato mora é?', 'Valor do aluguel: residencial, comercial e valor do condomínio (se possuir)', 'Tipo de comprovação do aluguel apresentada:', 'IPTU (valor total) – correspondente à imóveis e terrenos', 'Tipo de comprovação de IPTU', 'Conta de água', 'Tipo de comprovação de conta de água apresentada:', 'Conta de luz', 'Tipo de comprovação de conta de luz apresentada:', 'Conta de Telefone (fixo + celulares pré e pós pagos)', 'Tipo de comprovação de conta de telefone apresentada', 'Internet e TV a Cabo', 'Tipo de comprovação de conta de Internet e TV a cabo apresentada', 'Transporte (particular e público + vale transporte)', 'Educação (em andamento)', 'Tipo de comprovação de educação', 'Assistência Médica e/ou Odontológica', 'Tipo de comprovação de médica ou odontológica', 'Outros gastos (Valor)', 'Tipo de comprovação de outros gastos', 'Quantos carros sua família possui?', 'Quantas motos sua família possui?', 'IPVA (valor total) + DPVAT – correspondente à veículos', 'Tipo de comprovação de IPVA', 'Imposto de Renda a Pagar', 'Tipo de comprovação de IR', 'Imposto de Renda a Restituir ', 'Tipo de comprovação de IR.1', 'Dívidas (valor total de ser pago) – empréstimos, consórcios, carnês, financiamentos, agiota, membro da família, etc.', 'Tipo de comprovação de Dívidas', 'Onde você estudou no Ensino Médio?', 'Se você está no Ensino Médio, que ano está cursando?', 'Caso tenha estudado em escola particular no ensino médio, possuía bolsa?', 'Tipo de comprovação de Escolaridade', 'Nível de Escolaridade do Pai', 'Nível de Escolaridade da Mãe']

df_aj = df[data_cols]

new_cols = ['Número de Identificação', 'Número do Pedido', 'Nome', 'decl_racial', 'fam', 'fam_comp', 'fam_inc',  'renda_c', 'renda_c_conf', 'renda_p', 'renda_p_conf', 'renda_m', 'renda_m_conf', 'renda_if', 'renda_if_conf', 'renda_conj', 'renda_conj_conf', 'renda_out', 'renda_out_conf', 'renda_ext', 'renda_ext_conf', 'imoveis', 'tipo_casa', 'aluguel', 'aluguel_conf', 'iptu', 'iptu_conf', 'agua', 'agua_conf', 'luz', 'luz_conf', 'telefone', 'telefone_conf',  'internet', 'internet_conf', 'transp', 'edu', 'edu_conf', 'saude', 'saude_conf', 'outros_gastos', 'outros_gastos_conf', 'carros', 'motos', 'ipva', 'ipva_conf', 'ir_pagar', 'ir_pagar_conf', 'ir_rest', 'ir_rest_conf', 'dividas', 'dividas_conf', 'tipo_EM', 'ano_EM', 'bolsa_EM', 'EM_conf', 'escolaridade_p', 'escolaridade_m']

cols = {data_cols[i]: new_cols[i] for i in range(len(data_cols))}
#esse dicionário iguala o nome das colunas do forms com os novos nomes, portanto o index da coluna na lista data_cols deve ser o mesmo na lista new_cols

df_aj.rename(columns = cols, inplace = True)

#agora, com a tabela arrumada, podemos começar os cálculos (é possível conferir os critérios no drive)
#cálculo das confiabilidades da parte - a -
#membros da família
df_aj['fam_inc'] = df_aj['fam_inc'].fillna(0)

df_aj['fam_conf'] = df_aj['fam_comp'] * 2 + df_aj['fam_inc']

df_aj['fam'] = df_aj['fam_conf'] / 2

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

def conf(col1, col2):
    df_aj[col1] = df_aj[col1].astype(float)
    df_aj[col2] = df_aj[col2].astype(float)
    cont = df_aj[col1] * (df_aj[col2]/2)
    return cont

df_aj['rd1_t'] = conf('renda_c', 'renda_c_conf')
df_aj['rd2_t'] = conf('renda_p', 'renda_p_conf')
df_aj['rd3_t'] = conf('renda_m', 'renda_m_conf')
df_aj['rd4_t'] = conf('renda_if', 'renda_if_conf')
df_aj['rd5_t'] = conf('renda_conj', 'renda_conj_conf')
df_aj['rd6_t'] = conf('renda_out', 'renda_out_conf')
df_aj['rd7_t'] = conf('renda_ext', 'renda_ext_conf')

#renda total
df_aj['renda_total'] = df_aj[['rd1_t', 'rd2_t','rd3_t','rd4_t','rd5_t','rd6_t','rd7_t']].sum(axis = 1)

#pontuação renda total

#vamos definir a função de pontuação
def pontuacao(df, coluna, intervalos, pontos):
    #validar se as listas tem o mesmo tamanho (para cada intervalo, uma pontuação)
    if len(intervalos) != len(pontos):
        raise ValueError("Número de intervalos não é o mesmo do número de possíveis pontos!")

    #lista vazia para conter os pontos (depois transformaremos em coluna na df)
    pontos_atribuidos = []

    #passa por cada linha
    for value in df[coluna]:
        #confere em qual intervalo cada célula se encaixa e atribui uma pontuação
        score = None
        for i, interval in enumerate(intervalos):
            if interval[0] <= value <= interval[1]:
                score = pontos[i]
                break

        #adiciona o score na lista
        pontos_atribuidos.append(score)

    #lista vira coluna
    df[f'''pont_{coluna}'''] = pontos_atribuidos

    return df

#aplicar a função na df
df_aj = pontuacao(df_aj, 'renda_total', intervalos_renda_total, pontos_renda_total)

#pontuação renda per capita
df_aj['renda_pc'] = df_aj['renda_total'] / df_aj['fam']

df_aj['renda_pc'] = df_aj['renda_pc'].fillna(0)

df_aj = pontuacao(df_aj, 'renda_pc', intervalos_renda_pc, pontos_renda_pc)

#confiabilidade gastos
#aluguel
def aluguel_conf(tipo):
    df_aj.loc[df_aj[tipo]=="Casa própria", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Casa própria e comprovou pagar condomínio", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Apresenta um contrato de aluguel (desde que o documento esteja no prazo de vigor)", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Declaração de próprio punho, desde que alegue o valor e o motivo de não ter recibo", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Se a pessoa declara que vive em situação irregular ou em casa emprestada", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Carteira de trabalho não encerrada", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Recibo de aluguel sem data nem nome (somente com o valor)", tipo] = 1
    df_aj.loc[df_aj[tipo]=="Casa alugada mas não apresentou documento comprobatório", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Print ou nota fiscal de transferência de banco", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Paga condomínio em casa própria mas não apresentou documento comprobatório", tipo] = 0

aluguel_conf('aluguel_conf')

df_aj['res_aluguel'] = df_aj['aluguel'] * df_aj['aluguel_conf']

#iptu
data = dt.date.today()

atual_iptu = "Comprovante de IPTU de " + str(data.year - 2) + ',  ' + str(data.year - 1) + ' ou ' + str(data.year)

antigo_iptu = "Documentos de " + str(data.year - 3) + " ou mais antigos"

def iptu_conf(tipo):
    df_aj.loc[df_aj[tipo]=="Declaração de isenção à próprio punho ou um documento que mostre que ela é isenta", tipo] = 2
    df_aj.loc[df_aj[tipo]==atual_iptu, tipo] = 2
    df_aj.loc[df_aj[tipo]=="Casa em situação irregular ou emprestada e disse que não paga IPTU", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Declaração de próprio punho, desde que alegue o valor e o motivo de não ter recibo", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Quando a pessoa mora em casa própria, coloca que não paga IPTU, mas não declara isenção", tipo] = 1
    df_aj.loc[df_aj[tipo]=="Declarou valor mas não comprovou", tipo] = 0
    df_aj.loc[df_aj[tipo]==antigo_iptu, tipo] = 0
    df_aj.loc[df_aj[tipo]=="Valor declarado 0", tipo] = 0

iptu_conf('iptu_conf')

#água
def agua_conf(tipo):
    df_aj.loc[df_aj[tipo]=="Declarou valor 0 e a casa está em situação irregular ou se o indivíduo morar de favor.", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Existe alguma explicação ou declaração do porquê não paga água tais como ( tirar água do poço, etc)", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Declarou um valor e ele é comprovado através de um documento recente", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Documento incompleto, pouco visível, onde não há como ver o valor final ou o nome de quem vem na conta.(Leve no bom senso)", tipo] = 1
    df_aj.loc[df_aj[tipo]=="Valor declarado 0 e não comprovou o porquê de não pagar.", tipo] = 1
    df_aj.loc[df_aj[tipo]=="Declarou um valor mas não comprovou", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Não é um documento recente (mais de 6 meses)", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Documento ilegível", tipo] = 0

agua_conf('agua_conf')

#Educação
def edu_conf(tipo):
    df_aj.loc[df_aj[tipo]=='Valor declarado 0', tipo] = 2
    df_aj.loc[df_aj[tipo]=='Um boleto ou comprovante de pagamento qualquer instituição de educação', tipo] = 2
    df_aj.loc[df_aj[tipo]=='Um print ou recibo de pagamento, mas que não diz quem estava recebendo.', tipo] = 1
    df_aj.loc[df_aj[tipo]=='Declarou valor mas não apresentou comprovante.', tipo] = 0

edu_conf('edu_conf')    

df_aj['res_edu'] = df_aj['edu'] * df_aj['edu_conf'] / 2

#Saúde
def saude_conf(tipo):
    df_aj.loc[df_aj[tipo]=="Valor declarado 0", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Documento, boleto, transferência bancária que indique que quem recebe o valor é um plano de saúde", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Valor comprovado no holerite", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Declarou valor mas não apresentou um documento comprobatório", tipo] = 0
    df_aj.loc[df_aj[tipo]=="Consultas avulsas (não é algo recorrente)", tipo] = 0

saude_conf('saude_conf')

df_aj['res_saude'] = df_aj['saude'] * df_aj['saude_conf'] / 2

#Outros
def outros_gastos_conf(tipo):
    df_aj.loc[df_aj[tipo]=="Valor declarado 0", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Valor comprovado", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Valor inferior a 300", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Valor superior a 300 e comprovado", tipo] = 2
    df_aj.loc[df_aj[tipo]=="Gasto não recorrente", tipo] = 0

outros_gastos_conf('outros_gastos_conf')

df_aj['res_outros_gastos'] = df_aj['outros_gastos'] * df_aj['outros_gastos_conf'] / 2