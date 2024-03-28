import numpy as np
import matplotlib.pyplot as plt


class Day_4:
    def __init__(self):
        self.result = []
        # Generating random Numbers
        self.num = np.random.randint(99, size=(100))

    # Calculation for first equation(y=2x+3)
    def first(self):
        for i in self.num:
            a = (2 * i) + 3
            self.result.append(a)
        return self.result

    # Calculation for second equation (y=2x^2+3x+4)
    def second(self):
        for i in self.num:
            a = (2 * i**2) + (3 * i) + 4
            self.result.append(a)
        return self.result

    # Calculation for third equation (y=2x^3+3x^3+4x+5)
    def third(self):
        for i in self.num:
            a = (2 * i*3) + (3 * i*2) + (4 * i) + 5
            self.result.append(a)
        return self.result

    # Calculation for fourth equation(y=3x+2x+4x+5)
    def four(self):
        for i in self.num:
            a = (3*i) + (2*i)+(4*i)+5
            self.result.append(a)
        return self.result

    # Drawing Plots
    def draw(self):
        fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(8, 10))

        ax[0, 0].plot(Day_4.first(self), marker="o", markersize=3, c="red")
        ax[0, 1].plot(Day_4.second(self), marker="o", markersize=3, c="blue")
        ax[1, 0].plot(Day_4.third(self), marker="o", markersize=3, c="green")
        ax[1, 1].plot(Day_4.four(self), marker="o", markersize=3, c="black")

        ax[0, 0].set_title("Linear regression using (y = 2x+3)")
        ax[0, 1].set_title("Linear regression using (y = 2x^2 + 3x + 4)")
        ax[1, 0].set_title(
            "Linear regression using (y = 2x^3 + 3x^2 + 4x + 5)")
        ax[1, 1].set_title(
            "Linear regression using (y= 3x_1 + 2x_2 + 4x_3 + 5)")

        fig.suptitle("Linear Regression Calculation using numpy random.")
        plt.subplots_adjust(
            left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.2, hspace=0.3
        )
        plt.show()


if __name__ == "__main__":
    calc = Day_4()
    calc.draw()
