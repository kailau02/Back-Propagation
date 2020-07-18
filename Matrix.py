import random


class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for col in range(cols)] for row in range(rows)]

    # Print a table of data to represent a matrix
    def printTable(self):
        colCount = "___________0" + "".join(
            ["___________|_" + "".join(["_" for y in range(11 - len(str(x + 1)))]) + str(x + 1) for x in
             range(self.cols - 1)]) + "___________|"
        table = "R/C" + str(colCount) + "\n"
        for row in range(self.rows):
            table += str(row) + "_|_"
            for col in range(self.cols):
                addedSpace = "".join(["_" for x in range(21 - len(str(self.data[row][col])))])
                table += "".join(addedSpace[:len(addedSpace) // 2]) + str(self.data[row][col]) + "".join(
                    addedSpace[len(addedSpace) // 2:]) + "_|_"
            table = table[:-1]
            table += "\n"
        print(table)

    # Randomize all values in matrix
    def randomize(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.data[row][col] = (random.random() * 2.0) - 1.0

    # Return a matrix from an array
    @staticmethod
    def fromArray(arr):
        m = Matrix(len(arr), 1)
        for element in range(len(arr)):
            m.data[element][0] = arr[element]
        return m

    # Return a matrix from an array
    @staticmethod
    def fromCondensedArray(arr, rows, cols):
        m = Matrix(rows, cols)
        for row in range(rows):
            for col in range(cols):
                m.data[row][col] = arr[0]
                arr.pop(0)
        return m

    # Return an array from a matrix
    @staticmethod
    def toArray(m):
        arr = []
        for row in range(m.rows):
            for col in range(m.cols):
                arr.append(m.data[row][col])
        return arr

    # Multiply two matrices
    @staticmethod
    def multiplyMatrices(m1, m2):
        if m1.cols != m2.rows:
            print("A's Cols must match B's rows.")
        else:
            result = Matrix(m1.rows, m2.cols)

            for row in range(result.rows):
                for col in range(result.cols):
                    sum = 0
                    for i in range(m1.cols):
                        sum += m1.data[row][i] * m2.data[i][col]
                    result.data[row][col] = sum
            return result

    # Multiply all values in a matrix by n
    def multiply(self, n):
        if type(n) is Matrix:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.data[row][col] *= n.data[row][col]
        else:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.data[row][col] *= n
    # Subtract two matrices
    @staticmethod
    def subtract(a, b):
        result = Matrix(a.rows, a.cols)
        for row in range(result.rows):
            for col in range(result.cols):
                result.data[row][col] = a.data[row][col] - b.data[row][col]
        return result

    # Add all values in matrix by n
    def add(self, n):
        if type(n) is Matrix:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.data[row][col] += n.data[row][col]
        else:
            for row in range(self.rows):
                for col in range(self.cols):
                    self.data[row][col] += n

    # Return a matrix that switches rows and cols
    @staticmethod
    def transpose(m):
        result = Matrix(m.cols, m.rows)
        for row in range(m.rows):
            for col in range(m.cols):
                result.data[col][row] = m.data[row][col]
        return result

    # Map all values in a matrix by n
    def map(self, func):
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.data[row][col]
                self.data[row][col] = func(val)

    # Return a matrix with all values mapped by n
    @staticmethod
    def mapMatrix(m, func):
        result = Matrix(m.rows, m.cols)
        for row in range(m.rows):
            for col in range(m.cols):
                val = m.data[row][col]
                result.data[row][col] = func(val)
        return result
