import random
from meniu import pasirinkimas, valdymas, toprezultatai


rezultatas = 0

lauko_plotis = 10
lauko_ilgis = 10
laukas = []

for y1 in range(lauko_ilgis):
    laukas.append([])
    for x1 in range(lauko_plotis):
        laukas[y1].append("-")


class Tankas:
    def __init__(self, kryptis, x_axis, y_axis):
        self.kryptis = kryptis
        self.x_axis = int(x_axis)
        self.y_axis = int(y_axis)

    def siaure(self):
        if self.y_axis == 0:
            print("Pasiektos šiaures ribos")
            return
        laukas[self.y_axis][self.x_axis] = "-"
        self.y_axis -= 1
        self.kryptis = "Šiaure"
        laukas[self.y_axis][self.x_axis] = "X"

    def pietus(self):
        if self.y_axis == lauko_ilgis - 1:
            print("Pasiektos pietu ribos")
        laukas[self.y_axis][self.x_axis] = "-"
        self.y_axis += 1
        self.kryptis = "Pietus"
        laukas[self.y_axis][self.x_axis] = "X"

    def vakarai(self):
        if self.x_axis == 0:
            print("Pasiektos vakaru ribos")
        laukas[self.y_axis][self.x_axis] = "-"
        self.x_axis -= 1
        self.kryptis = "Vakarai"
        laukas[self.y_axis][self.x_axis] = "X"

    def rytai(self):
        if self.x_axis == lauko_plotis - 1:
            print("Pasietos rytu ribos")
        laukas[self.y_axis][self.x_axis] = "-"
        self.x_axis += 1
        self.kryptis = "Rytai"
        laukas[self.y_axis][self.x_axis] = "X"

    def info(self):
        print(f'Kryptis - {self.kryptis}')
        print(f'Tanko kordinates: x = {tankete.x_axis}, y = {tankete.y_axis}')
        print(f'Priešo kordinates: x = {priesas.x_axis}, y = {priesas.y_axis}')
        print(f'Taškai: {rezultatas}')
        print(f'Atlikti šuviai: {visisuviai}\n{suviai}')
        input("Noredami testi iveskite betka")

    def reset(self):
        laukas[self.y_axis][self.x_axis] = "-"
        self.x_axis = 5
        self.y_axis = 5
        laukas[self.y_axis][self.x_axis] = "X"

    def fire(self):
        x = self.x_axis
        y = self.y_axis

        global ejimai
        suvis = False
        suvio_distancija = 10

        for distancija in range(suvio_distancija):
            if x == priesas.x_axis and y == priesas.y_axis:
                suvis = True
                break

            if self.kryptis == "Šiaure":
                y -= 1
            elif self.kryptis == "Pietus":
                y += 1
            elif self.kryptis == "Vakarai":
                x -= 1
            elif self.kryptis == "Rytai":
                x += 1

        if suvis:
            print("Pataikyta!")
            priesas.kitur()
            global rezultatas
            rezultatas += 10
            ejimai += 2
            tekstas = "Pataikyta"

        else:
            print("Nepataikyta")
            ejimai -= 1
            tekstas = "Nepataikyta"

        suviai.append((tankete.x_axis, tankete.y_axis, self.kryptis, tekstas))
        global visisuviai
        visisuviai += 1


tankete = Tankas("šiaure", 5, 5)


class PriesoTankas:
    def __init__(self):
        self.x_axis = random.randint(0, lauko_plotis - 1)
        self.y_axis = random.randint(0, lauko_ilgis - 1)

    def info(self):
        print(f'Prieso tankas x = {self.x_axis}, y = {self.y_axis}')

    def kitur(self):
        laukas[self.y_axis][self.x_axis] = "-"
        self.x_axis = random.randint(0, lauko_plotis - 1)
        self.y_axis = random.randint(0, lauko_ilgis - 1)
        laukas[self.y_axis][self.x_axis] = "x"


priesas = PriesoTankas()
# =====================================================================


def rodyti_lauka():
    laukas[tankete.y_axis][tankete.x_axis] = "X"
    laukas[priesas.y_axis][priesas.x_axis] = "E"
    for row in laukas:
        for cell in row:
            print(cell, end="  ")
        print()


# ============================================================================
veiksmas = ""
while True:
    tankete.reset()
    pasirinkimas()
    pasirinko = input("Pasirinkite:")
    if pasirinko not in ["1", "2", "3", "4"]:
        print("Neteisingai pasirinkote")
    else:

        if pasirinko == "1":
            ejimai = 10
            suviai = []
            visisuviai = 0
            while ejimai > -1:
                rodyti_lauka()
                veiksmas = input("komanda(w,a,s,d,f,x,q): ")
                print(f'Liko ėjimu: {ejimai}')
                if veiksmas == "a":
                    tankete.vakarai()
                    ejimai -= 1
                elif veiksmas == "w":
                    tankete.siaure()
                    ejimai -= 1
                elif veiksmas == "s":
                    tankete.pietus()
                    ejimai -= 1
                elif veiksmas == "d":
                    tankete.rytai()
                    ejimai -= 1
                elif veiksmas == "f":
                    tankete.fire()
                elif veiksmas == "x":
                    tankete.info()
                elif veiksmas == 'q':
                    break
            print(f"Rezultatas: {rezultatas}")
            vardas = input("Iveskite savo varda: ")
            with open('rezultatai.txt', 'a') as f:
                f.write(f'{vardas}: {rezultatas}\n')

        elif pasirinko == "2":
            valdymas()
            pass
        elif pasirinko == "3":
            toprezultatai()
            pass
        elif pasirinko == "4":
            break
