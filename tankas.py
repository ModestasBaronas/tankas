import random
# !!!!!!!!!!!!!!!!!!!!
vardas = ""
rezultatas = 100
# !!!!!!!!!!!!!!!!!!!!
lauko_plotis = 10
lauko_ilgis = 10
laukas = []
for y1 in range(lauko_ilgis):
    laukas.append([])
    for x1 in range(lauko_plotis):
        laukas[y1].append("-")


# ========================================================================
# class Taskai:
#     def __init__(self, vardas, rezultatas):
#         self.vardas = vardas
#         self.rezultatas = rezultatas
#
#     def saugoti(self):
#         with open("rezultatai.txt", "a") as f:
#             f.write(f"{self.vardas},{self.rezultatas}\n")
#
#
# zaidejo_taskai = Taskai()
# ================================================================================

class Tankas:
    def __init__(self, kryptis, x_axis, y_axis):
        self.kryptis = kryptis
        self.x_axis = int(x_axis)
        self.y_axis = int(y_axis)

    def siaure(self):
        laukas[self.y_axis][self.x_axis] = "-"
        self.y_axis -= 1
        self.kryptis = "Šiaure"
        laukas[self.y_axis][self.x_axis] = "X"

    def pietus(self):
        laukas[self.y_axis][self.x_axis] = "-"
        self.y_axis += 1
        self.kryptis = "Pietus"
        laukas[self.y_axis][self.x_axis] = "X"

    def vakarai(self):
        laukas[self.y_axis][self.x_axis] = "-"
        self.x_axis -= 1
        self.kryptis = "Vakarai"
        laukas[self.y_axis][self.x_axis] = "X"

    def rytai(self):
        laukas[self.y_axis][self.x_axis] = "-"
        self.x_axis += 1
        self.kryptis = "Rytai"
        laukas[self.y_axis][self.x_axis] = "X"

    def info(self):
        print(f'Kryptis - {self.kryptis}')
        print(f'kordinates: x = {self.x_axis}, y = {self.y_axis}')
        print(f'Taškai: {rezultatas}')
        print(f'atlikti šuviai{suviai}')

    def fire(self):
        x = self.x_axis
        y = self.y_axis

        pataikyta = "Nepataikyta"

        suvio_distancija = 10

        for distancija in range(suvio_distancija):
            if x == priesas.x_axis and y == priesas.y_axis:
                pataikyta = "Pataikyta"
                break

            if self.kryptis == "Šiaure":
                y -= 1
            elif self.kryptis == "Pietus":
                y += 1
            elif self.kryptis == "Vakarai":
                x -= 1
            elif self.kryptis == "Rytai":
                x += 1

        suviai.append((x, y, self.kryptis, pataikyta))

        if pataikyta:
            print("Pataikyta!")
            priesas.kitur()
            global rezultatas
            rezultatas += 10

        else:
            print("Nepataikyta")


suviai = []
tankete = Tankas("šiaure", 5, 5)


class PriesoTankas:
    def __init__(self):
        self.x_axis = random.randint(0, lauko_plotis - 1)
        self.y_axis = random.randint(0, lauko_ilgis - 1)

    def info(self):
        print(f'Enemy tank at x = {self.x_axis}, y = {self.y_axis}')

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
    print(f'Tanko kordinates: x = {tankete.x_axis}, y = {tankete.y_axis}   Kryptis:{tankete.kryptis}')
    print(f'Priešo kordinates: x = {priesas.x_axis}, y = {priesas.y_axis}')


# ============================================================================
while True:
    rodyti_lauka()
    veiksmas = input("komanda(w,a,s,d,f,x,q): ")
    if veiksmas == "a":
        tankete.vakarai()
    elif veiksmas == "w":
        tankete.siaure()
    elif veiksmas == "s":
        tankete.pietus()
    elif veiksmas == "d":
        tankete.rytai()
    elif veiksmas == "f":
        tankete.fire()
    elif veiksmas == "x":
        tankete.info()
    elif veiksmas == "q":
        break
