info = ("""Acre    AC
Alagoas    AL
Amapá    AP
Amazonas    AM
Bahia    BA
Ceará    CE
Distrito Federal    DF
Espírito Santo    ES
Goiás    GO
Maranhão    MA
Mato Grosso    MT
Mato Grosso do Sul    MS
Minas Gerais    MG
Pará    PA
Paraíba     PB
Paraná    PR
Pernambuco    PE
Piauí    PI
Rio de Janeiro    RJ
Rio Grande do Norte    RN
Rio Grande do Sul     RS
Rondônia    RO
Roraima    RR
Santa Catarina     SC
São Paulo     SP
Sergipe    SE
Tocantins    TO""")

# Separando os elementos por espaços ou quebras de linha
info = info.split('     ')
print (info)

# Ajustando o nome da variável de comprimento
length = len(info)

# Inicializando a lista info2
info2 = []

# Iterando sobre os estados (pulando os códigos)
for i in range(0, length, 2):
    info2.append(info[i])

print(info2)
