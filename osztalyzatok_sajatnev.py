import random

jegyek = []

tantargyak_szama = int(input("Hány tantárgy volt a félév során?(5-15) "))
while  tantargyak_szama<5  or tantargyak_szama>15:
    print("Helytelen érték! 5 és 15 közötti számot adjon meg!: ")
    tantargyak_szama = int(input("Hány tantárgy volt a félév során?(5-15) "))
print(f"Rendben! A tantárgyak száma: {tantargyak_szama}")


for _ in range(tantargyak_szama):
    jegyek.append(random.randint(1,5))


print(jegyek)
print(f"Legjobb osztályzat: {max(jegyek)}")
print(f"Legrosszabb osztályzat: {min(jegyek)}")
print(f"Jegyek Átlaga: {sum(jegyek)/tantargyak_szama}")

