import numpy as np

class ConicSection:
    def __init__(self, a, b, c, d, e, f):
        self.conicMatrix = np.array([[a, b, c], [b, c, e], [d, e, f]])

    def Determinant(self):
        return self.b**2 - 4 * self.a * self.c

    def isDegenerate(self):
        

    def SectionType(self):
        if self.Determinant() < 0:
            if self.a == self.c and self.b == 0:
                return "Circle"
            else:
                return "Ellipse"
        elif self.Determinant() == 0:
            return "Parabola"
        elif self.Determinant() > 0:
            return "Hyperbola"

conicA = 2
conicB = 2
conicC = 2
conicD = 2
conicE = 2
conicF = 2


conictest = ConicSection(conicA, conicB, conicC, conicD, conicE, conicF)
print(f"Determinant: {conictest.Determinant()}")
print(f"Type: {conictest.SectionType()}")




