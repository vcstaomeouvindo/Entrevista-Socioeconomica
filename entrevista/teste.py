#import library
import gspread

#connect to the service account
gc = gspread.service_account(filename="chave.json")

#connect to your sheet (between "" = the name of your G Sheet, keep it short)
sh = gc.open("Teste").sheet1

#get the values from cells a2 and b2
r1 = sh.acell("b2").value
r2 = sh.acell("b3").value

print(r1)
print(r2)

row = 2
renda = []
limit = 7

while row <= limit:

 renda.append(int(sh.acell(f"b{row}").value))
 for i in renda:
     if int(i) <= 30:
         prenda = 4
        
 row += 1
 
row = 2
gastos = []
limit = 7

while row <= limit:

 gastos.append(int(sh.acell(f"c{row}").value))
 for i in gastos:
     if int(i) <= 30:
         p = 4
         
 row += 1
 
 total = []

for r in range(len(renda)):
    total.append(renda[r] - gastos[r])
    

print(renda)
print(gastos)
print(total)

print('Pontuação final: ')
for i in total:
    if int(i) <= 30:
        pf = 6
        print(pf)
    else:
        pf = 2
        print(pf)

