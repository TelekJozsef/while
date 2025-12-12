szam = int(input("Adj meg egy páros számot: "))

while szam % 2 != 0:
    print("Ez nem páros, kérek egy páros számot.")
    szam = int(input("Adj meg egy páros számot: "))

print("A ",szam, "páros.")
