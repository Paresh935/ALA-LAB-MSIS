# This file includes steps 1,2 and 3 (Steps.txt)

import math
import random
from typing import Self


class Vec:
    #A simple class for representing mathematical vectors.

    def __init__(self, elements):
        #Create a vector from a list of numbers.
        self.elements = list(elements)
        # Check that every element is a number
        for x in self.elements:
            if not isinstance(x, (int, float)):
                raise TypeError("Vector elements must be numbers.")



    def __add__(self, other):
        #Add two vectors element by element.
        if not isinstance(other, Vec):
            raise TypeError("Can only add another Vec.")
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions.")
     
        result = []
        #created empty list to store the result of the addition
        for x, y in zip(self.elements, other.elements):
            result.append(x + y)
        return Vec(result)


    def __sub__(self, other):
        # """Subtract two vectors element by element."""

        if not isinstance(other, Vec):
            raise TypeError("Can only subtract another Vec.")

        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimensions.")

        result = []
        #created empty list to store the result of the subtraction
        for x, y in zip(self.elements, other.elements):
            result.append(x - y)
        return Vec(result)



    def __rmul__(self, scalar):
        # Multiply every element of the vector by a scalar.

        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")

        result = []
        for x in self.elements:
            result.append(x * scalar)
        return Vec(result)



    def __imul__(self, scalar):
        # Multiply the vector by a scalar in place.
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")

        for i in range(len(self.elements)):
            self.elements[i] *= scalar
        return self



    def __neg__(self):
        # Return the negative of the vector.
        return Vec([-x for x in self.elements])



    def __radd__(self, other):
        # Allow vectors to work with Python's sum() function.
        if other == 0:
            return self
        return self + other



    def __iadd__(self, other):
        # Add another vector to this vector in place.
        result = self + other
        self.elements = result.elements
        return self



    def __len__(self):
        # Return the number of elements in the vector.
        return len(self.elements)



    def __repr__(self):
        # Return a readable representation of the vector.
        return repr(self.elements)



    @staticmethod
    def zeros(n):
        #Create a vector containing n zeros.
        return Vec([0.0] * n)



    @staticmethod
    def ones(n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Dimension must be a positive integer.")
        return Vec([1.0] * n)


    @staticmethod
    def uniform(n):
        #Creates a vector containing n random numbers between 0 and 1.
        return Vec([random.random() for _ in range(n)])



    def norm(self):
    #Find the length (L2 norm) of the vector.
    #The norm is calculated by taking the square root of the sum of squares of all vector elements.
    #formula:sqrt(e[0]^2 + e[1]^2 + e[2]^2 + ... + e[n-1]^2)

        sum_square = sum(x ** 2 for x in self.elements)
        return round(math.sqrt(sum_square), 5)


    def mean (self: Self) -> float:
        
    # Calculate the average value of the vector.
    # The mean is found by adding all elements and dividing by the total number of elements.
    # Formula: (x[0] + x[1] + ... + x[n-1]) / n
        if len(self.elements) == 0:
            raise ValueError("Cannot compute mean of an empty vector.")
        return sum(self.elements) / len(self.elements)  


    def demean(self: Self)-> Self:
    # Subtract the mean value from every element of the vector.
    # self.mean() calculates the mean of the vector.
    # self.ones(len(self.elements)) creates a vector of 1s with the same size.
    # Multiplying the mean by the ones vector gives a vector containing
    # the mean value at every position.
    # Finally, subtract this mean vector from the original vector.
    #Formula: Demean(x) = x - mean(x)
    
        return self - self.mean() * self.ones(len(self.elements))



    def std(self: Self) -> float:
    # Calculate the standard deviation of the vector elements.
    # First find the de-meaned vector and calculate its norm.
    # Then divide the norm by the square root of the number of elements.
    # Formula: std(x) = norm(demean(x)) / sqrt(n)
        if len(self.elements) == 0:
            raise ValueError("Cannot compute standard deviation of an empty vector.")
        
        return self.demean().norm() / math.sqrt(len(self.elements))

    