class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"Dom o powierzchni {self.area} m2, "
                f"{self.rooms} pokoi, cena {self.price} zł, "
                f"adres: {self.address}, działka {self.plot} m2.")


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f"Mieszkanie o powierzchni {self.area} m2, "
                f"{self.rooms} pokoi, cena {self.price} zł, "
                f"adres: {self.address}, piętro {self.floor}.")


house = House(area=120, rooms=5, price=750000, address="ul. Leśna 12, Katowice", plot=500)
flat = Flat(area=60, rooms=3, price=350000, address="ul. Mickiewicza 5/12, Katowice", floor=3)
print(house)
print(flat)
