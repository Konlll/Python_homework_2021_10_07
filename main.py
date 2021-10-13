def main():
    matek = float(input("Add meg a matek átlagod! "))
    tori = float(input("Add meg a töri átlagod! "))
    angol = float(input("Add meg az angol átlagod! "))
    if matek > 5 or angol > 5 or tori > 5 or matek < 1 or angol < 1 or tori < 1:
        print("Hibás bemenet, ilyen átlag nem létezik.")
    else:
        atlag = (matek + tori + angol) / 3
        if atlag < 3.5:
            print("Az ösztöndíjad: 0 Ft")
        elif atlag >= 3.5 and atlag < 4.:
            print("Az ösztöndíjad: 10000 Ft")
        elif atlag >= 4 and atlag < 4.8:
            print("Az ösztöndíjad: 15000 Ft")
        elif atlag >= 4.8 and atlag <= 5:
            print("Az ösztöndíjad: 30000 Ft")

if __name__ == "__main__":
    main()