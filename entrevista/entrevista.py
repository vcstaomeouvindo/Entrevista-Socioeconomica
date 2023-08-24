import gspread

#connect to the service account
gc = gspread.service_account(filename="chave.json")

#connect to your sheet (between "" = the name of your G Sheet, keep it short)
sh = gc.open("Entrevista Socioeconômica - TSI 2023 (respostas)").sheet1

row = 2
renda = []
fam = []
limit = 100

while row <= limit:

 renda.append(int(sh.acell(f"aj{row}").value))
 for i in renda:
    if int(i >= 0) and int(i < 882):
        prenda = 20
    elif (i >= 882) and (i < 1242):
        prenda = 18
    elif (i >= 1242) and (i < 1350):
        prenda = 15
    elif (i >= 1350) and (i < 1600):
        prenda = 12
    elif (i >= 1600) and (i < 2520):
        prenda = 9
    elif (i >= 2520) and (i < 4800):
        prenda = 6
    elif (i >= 4800) and (i < 5500):
        prenda = 3
    elif (i >= 5500):
        prenda = 0
        print(prenda)
        
 fam.append(int(sh.acell(f"ae{row}").value))

rendapc = []

for r in range(len(renda)):
    rendapc.append(renda[r] / fam[r])
    
    print(rendapc)
