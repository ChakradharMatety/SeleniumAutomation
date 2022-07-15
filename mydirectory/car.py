class car:
    color="white"

    def make_noise(self):
        print("Dacia Car Noise is brrr")


class DaciaCar(car):
    def make_noise(self):
        print("Dacia Car Noise is vrrrr")


c= car()
print(c.color)
c.color="Blue"
print(c.color)
c.make_noise()

daciacars=DaciaCar()
daciacars.make_noise()

