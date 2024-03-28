import csv
import numpy as np
import matplotlib.pyplot as plt


class DataSet:
    def __init__(self):
        self.name, self.year, self.selling_price, self.km_driven, self.fuel, self.seller_type, self.transmission, self.owner = ([
        ] for _ in range(8))
        with open("car_details.csv", mode="r") as file:
            csvFile = csv.DictReader(file)
            dataset.conversion(self, csvFile)

    def conversion(self, csvFile):

        self.name, self.year, self.selling_price, self.km_driven, self.fuel, self.seller_type, self.transmission, self.owner = ([
        ] for _ in range(8))
        with open("car_details.csv", mode="r") as file:
            csvFile = csv.DictReader(file)
            for line in csvFile:
                for attr, lst in zip(line.keys(), [self.name, self.year, self.selling_price, self.km_driven, self.fuel, self.seller_type, self.transmission, self.owner]):
                    try:
                        value = int(line[attr])
                        lst.append(value)
                    except ValueError:
                        pass
        self.name = np.array(self.name)
        self.year = np.array(self.year)
        self.selling_price = np.array(self.selling_price)
        self.km_driven = np.array(self.km_driven)
        self.fuel = np.array(self.fuel)
        self.seller_type = np.array(self.seller_type)
        self.transmission = np.array(self.transmission)
        self.owner = np.array(self.owner)

        analysis.calculate_mean(self)
        analysis.calculate_median(self)
        analysis.calculate_std(self)
        analysis.calculate_min(self)
        analysis.calculate_variance(self)
        analysis.draw(self)


class Analysis(DataSet):
    def __call__(self):
        return super().__call__()

    def calculate_mean(self):
        print(f"Mean of Selling Price is {np.mean(self.selling_price)}")
        print(f"Mean of KM Driven is {np.mean(self.km_driven)}")
        print(f"Mean of year is {np.mean(self.year)}\n")

    def calculate_median(self):
        print(f"median of Selling Price is {np.median(self.selling_price)}")
        print(f"median of KM Driven is {np.median(self.km_driven)}")
        print(f"median of year is {np.median(self.year)}\n")

    def calculate_std(self):
        print(
            f"Standard Deviation of Selling Price is {np.std(self.selling_price)}")
        print(f"Standard Deviation of KM Driven is {np.std(self.km_driven)}")
        print(f"Standard Deviation of year is {np.std(self.year)}\n")

    def calculate_variance(self):
        print(f"Varaince of Selling Price is {np.var(self.selling_price)}")
        print(f"Variance of KM Driven is {np.var(self.km_driven)}")
        print(f"Variance of year is {np.var(self.year)}\n")

    def calculate_min(self):
        print(f"Minimun of Selling Price is {np.min(self.selling_price)}")
        print(f"Minimun of KM Driven is {np.min(self.km_driven)}")
        print(f"Minimum of year is {np.min(self.year)}\n")

    def draw(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.selling_price, label='Selling Price')
        plt.title('Selling Price and Kilometers Driven Over Years')
        plt.xlabel(self.year)
        plt.ylabel(self.km_driven)
        plt.grid(linestyle=':')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    dataset = DataSet
    analysis = Analysis
    dataset()
