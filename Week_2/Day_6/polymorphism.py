# def add(a, b, c=0):
#     return a+b+c


# print(add(3, 5))
# print(add(2, 3, 4))

class Truck():
    def toyota(self):
        print("Truck is Toyota")


class Pickup(Truck):
    def toyota(self):
        print("Pickup")


class Lorry(Truck):
    def toyota(self):
        print("Lorry")


if __name__ == "__main__":
    truck = Truck()
    truck.toyota()

    pickup = Pickup()
    pickup.toyota()

    lorry = Lorry()
    lorry.toyota()
