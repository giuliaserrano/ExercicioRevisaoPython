lista1= []
lista2=[]
for i in range(10):
  a = int(input("Digite os elementos da primeira lista: "))
  lista1.append(a)

print("Acabou a primeira lista \n")
for j in range(10):
  b = int(input("Digite os elementos da segunda lista: "))
  lista2.append(b)

vetor = []
for n in range(10):
  s = lista1[n]
  s2 = lista2[n]
  vetor.append(s)
  vetor.append(s2)
print("Acabou a segunda lista \n")
print("Elementos intercalados: ",vetor)
