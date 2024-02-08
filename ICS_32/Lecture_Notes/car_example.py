class Bike:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def ride(self):
        print('Riding my Bike!')
    
class Electric_Bike (Bike):
    def __init__(self, make, model, power) -> None:
        super().__init__(make, model) #calling constructor of the parent class
        self.power = power

if __name__ == "__main__":
    print("practice w classes and objects")

    b = Bike("Honda", 2020)
    b.ride()

    eb = Electric_Bike("Tesla", 2022, 100)
    eb.ride()