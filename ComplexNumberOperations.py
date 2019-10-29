import math


class Complex(object):

    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        # print(self.real, self.imag)

    # adding two complex numbers
    def __add__(self, other):
        addcomplex = Complex(self.real + other.real, self.imag + other.imag)
        return addcomplex.__str__()

    # subtracting two complex numbers
    def __sub__(self, other):
        subcomplex = Complex(self.real - other.real, self.imag - other.imag)
        return subcomplex.__str__()

    # multiplication of two complex numbers
    def __mul__(self, other):
        multiplycomplex = Complex(self.real*other.real - self.imag*other.imag,
                            self.imag*other.real + self.real*other.imag)
        return multiplycomplex.__str__()

    # Division of two numbers
    def __truediv__(self, other):
        r = float(other.real**2 + other.imag**2)
        divcomplex = Complex((self.real*other.real + self.imag*other.imag)/r,
                             (self.imag*other.real - self.real*other.imag)/r)
        return divcomplex.__str__()

    # Modulus of a complex number
    def modulus(self):
        return math.sqrt(self.real**2 + self.imag**2)

    # Creating complex number string from the real and imaginary numbers
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % self.imag
            else:
                result = "0.00-%.2fi" % abs(self.imag)
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result


if __name__ == "__main__":

    C = Complex(1, 2)
    D = Complex(4, 5)

    addResult = C + D
    print("Addition of C and D: ", addResult)

    subResult = C - D
    print("Subtraction of C and D: ", subResult)

    multiplyResult = C * D
    print("Multiplication of C and D: ", multiplyResult)

    divResult = C / D
    print("division of C and D: ", divResult)

    modC = C.modulus()
    print("Mod of C: ", modC)

    modD = D.modulus()
    print("Mod of D: ", modD)

