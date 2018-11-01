p1= input('Telefonou para a vítima?')
p2=input("Esteve no local do crime?")
p3= input("Mora perto da vítima?")
p4= input("Devia para a vítima?")
p5= input("Já trabalhou com a vítima?")
cont=0
if p1=='sim':
  cont+=1
if p2=="sim":
  cont+=1
if p3=="sim":
  cont+=1
if p4=="sim":
  cont+=1
if p5=="sim":
  cont+=1

if cont==2:
  print("Suspeito")

elif cont==3 or cont==4:
  print("Cúmplice")
elif cont==5:
  print("Assassino")
else:
  print("Inocente")


