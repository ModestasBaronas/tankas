
def pasirinkimas():
    print("MENIU \n 1. Pradėti žaidima \n 2. Valdymas \n 3. Top rezultatai \n 4. Išeiti")


def valdymas():
    print("Tikslas nušauti prieša, pries pasibaigiant ejimu skaičiui. Kekvienas priešo nušovimas prideda 2 ejimus")
    print("Judejimas: w(viršun), a(kairėn),d(dešinėn),s(apačion)")
    print("Šauti: f\nInformacija: x (žiurima kryptis; dabartinės kordinatės;"
          " priešo kordinatės; tašku suma; atlikti šuviai)")
    print("Išeiti: q")


def toprezultatai():
    print("Top rezultatai:")
    with open("rezultatai.txt", 'r') as topas:
        eilutes = topas.readlines()

    top = []
    for eilute in eilutes:
        if ':' in eilute:
            vardas, taskai = eilute.split(':')
            top.append((vardas, int(taskai)))

    isrusiuota = sorted(top, key=lambda x: -x[1])

    for i in range(min(10, len(isrusiuota))):
        vardas, taskai = isrusiuota[i]
        print(f"{i + 1}. {vardas}: {taskai}")
