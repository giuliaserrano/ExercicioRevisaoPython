nome = []
kms = []
km = 0
for c in range(5):
    print(f"Veiculo {c + 1}")
    nome.append(input("Nome: "))
    km = float(input("KM por litro: "))
    kms.append(km)

print("Relatorio Final")
menor = 0
nme = ' '
for c,d in enumerate(nome):
    print(f"{c + 1}\t -\t{d}\t - \t{kms[c]} -\t{1000 / kms[c]:.2f}\t -\t{1000 / kms[c] * 2.25:.2f}")
    if km > menor:
        menor = km
        nme = nome[c]

print(f"O menor consumo e do {nme}")
