#Importing numpy
import numpy as np

#Main Parent class to declare variables and numpy array
class ConfusionMatrix:
    def __init__(self):
        self.data = np.array([[34, 13, 5], [0, 52, 0], [13, 0, 33]])
        
        self.TP0 = self.data[0][0]
        self.TP1 = self.data[1][1]
        self.TP2 = self.data[2][2]
        
        self.TN0 = self.data[1][1] + self.data[1][2] + self.data[2][1] + self.data[2][2]
        self.TN1 = self.data[0][0] + self.data[0][2] + self.data[2][0] + self.data[2][2]
        self.TN2 = self.data[0][0] + self.data[0][1] + self.data[1][0] + self.data[1][1]
        
        self.FP0 = self.data[0][1] + self.data[0][2]
        self.FP1 = self.data[1][0] + self.data[1][2]
        self.FP2 = self.data[2][0] + self.data[2][1]
        
        self.FN0 = self.data[1][0] + self.data[2][0]
        self.FN1 = self.data[0][1] + self.data[2][1]
        self.FN2 = self.data[0][2] + self.data[1][2]

#Calculation for class 0
class class0(ConfusionMatrix):
    def __init__(self):
        super().__init__()

    def show(self, calc):
        self.accuracy = calc.accuracy(self.TP0, self.TN0, self.FP0, self.FN0)
        self.error = calc.error(self.TP0, self.TN0, self.FP0, self.FN0)
        self.recall = calc.recall(self.TP0, self.FN0)
        self.precision = calc.precision(self.TP0, self.FP0)
        self.f1score = calc.f1_score(self.precision, self.recall)
        self.f05score = calc.f05_score(self.precision, self.recall)
        self.f2score = calc.f2_score(self.precision, self.recall)
        self.support = calc.support(self.TP0, self.FN0)
        
        print(f'TP for class 0 is {self.TP0}')
        print(f'FP for class 0 is {self.FP0}')
        print(f'TN for class 0 is {self.TN0}')
        print(f'FN for class 0 is {self.FN0}')
        
        print("\n Datas for class 0:")
        print("Accuracy:", self.accuracy)
        print("Error:", self.error)
        print("Recall:", self.recall)
        print("Precision:", self.precision)
        print("F1 Score:", self.f1score)
        print(f"The f0.5 score is {self.f05score}")
        print(f"The f2 score is {self.f2score}")
        print(f"The support is {self.support}\n")
        

#Calculation for class 1
class class1(ConfusionMatrix):
    def __init__(self):
        super().__init__()

    def show(self, calc):
        self.accuracy1 = calc.accuracy(self.TP1, self.TN1, self.FP1, self.FN1)
        self.error1 = calc.error(self.TP1, self.TN1, self.FP1, self.FN1)
        self.recall1 = calc.recall(self.TP1, self.FN1)
        self.precision1 = calc.precision(self.TP1, self.FP1)
        self.f1score1 = calc.f1_score(self.precision1, self.recall1)
        self.f05score1 = calc.f05_score(self.precision1, self.recall1)
        self.f2score1= calc.f2_score(self.precision1, self.recall1)
        self.support = calc.support(self.TP1, self.FN1)
        
        print(f'TP for class 1 is {self.TP1}')
        print(f'FP for class 1 is {self.FP1}')
        print(f'TN for class 1 is {self.TN1}')
        print(f'FN for class 1 is {self.FN1}')
        
        print("\n Datas for class 1:")
        print("Accuracy:", self.accuracy1)
        print("Error:", self.error1)
        print("Recall:", self.recall1)
        print("Precision:", self.precision1)
        print("F1 Score:", self.f1score1)
        print(f"The f0.5 score is {self.f05score1}")
        print(f"The f2 score is {self.f2score1}")
        print(f"The support is {self.support}\n")

#Calculation for class 2
class class2(ConfusionMatrix):
    def __init__(self):
        super().__init__()

    def show(self, calc):
        self.accuracy2 = calc.accuracy(self.TP2, self.TN2, self.FP2, self.FN2)
        self.error2 = calc.error(self.TP2, self.TN2, self.FP2, self.FN2)
        self.recall2 = calc.recall(self.TP2, self.FN2)
        self.precision2 = calc.precision(self.TP2, self.FP2)
        self.f1score2 = calc.f2_score(self.precision2, self.recall2)
        self.f05score2 = calc.f05_score(self.precision2, self.recall2)
        self.f2score2 = calc.f2_score(self.precision2, self.recall2)
        self.support = calc.support(self.TP2, self.FN2)
        
        print(f'TP for class 2 is {self.TP2}')
        print(f'FP for class 2 is {self.FP2}')
        print(f'TN for class 2 is {self.TN2}')
        print(f'FN for class 2 is {self.FN2}')
        
        print("\nDatas for class 2:")
        print("Accuracy:", self.accuracy2)
        print("Error:", self.error2)
        print("Recall:", self.recall2)
        print("Precision:", self.precision2)
        print("F1 Score:", self.f1score2)
        print(f"The f0.5 score is {self.f05score2}")
        print(f"The f2 score is {self.f2score2}")
        print(f"The support is {self.support}\n")

#Class to create all Calculations
class Calculation(ConfusionMatrix):
    def __init__(self):
        super().__init__()

    def accuracy(self, TP, TN, FP, FN):
        return (TP + TN) / (TP + TN + FP + FN)

    def error(self, TP, TN, FP, FN):
        return (FP + FN) / (TP + TN + FP + FN)

    def recall(self, TP, FN):
        return TP / (TP + FN)

    def precision(self, TP, FP):
        return TP / (TP + FP)

    def f1_score(self, precision, recall):
        return 2 * (precision * recall) / (precision + recall)
    
    def f05_score(self, precision, recall):
        return 1.25 * (precision * recall) / 0.25*(precision + recall)
    
    def f2_score(self, precision, recall):
        return 5 * (precision * recall) / 4*(precision + recall)
        
    def support(self, TP, FN):
        return TP + FN
    
if __name__ == "__main__":
    
    confusion = ConfusionMatrix()
    calc = Calculation()
    class_0 = class0()
    class_1 = class1()
    class_2 = class2() 
    
    class_0.show(calc)
    class_1.show(calc)
    class_2.show(calc)

