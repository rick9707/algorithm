kg = int(input())

restKg = kg % 5
restThree = kg % 318
fiveKg = 0
threeKg = 0
a = 1
b = 1
c = kg
d = kg
e = kg
f = kg


if restKg % 3 == 0:
   fiveKg = kg // 5
   threeKg = restKg // 3
   e = fiveKg + threeKg

if kg % 3 == 0:

    d = kg // 3



while(5*a < kg):
    if (kg - 5 * a) % 3 == 0:
        if c > a + ((kg - 5 * a) // 3):
            c = a + ((kg - 5 * a) // 3)
    a = a + 1
f = min(e,d,c)

if f == kg: print(-1)
else: print(f)

