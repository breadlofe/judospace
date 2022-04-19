# Dustin Simpkins
# ETGG 1803 Lab 06
# April 4, 2022
# Hayden Ridgeway
import vector
import math

class Matrix(object):
    """
    Creates a Matrix M from Vectors within the Vector class.
    """
    def __init__(self, *vectors):
        """
        Constructor for the Matrix class.
        :param *vectors: A variable argument list of Vectors
        :return: N/A for contructors
        """
        if isinstance(vectors[0], vector.Vector):
            self.num_cols = vectors[0].dim
        else:
            raise TypeError("All inputs must be Vectors of same dimension.")
        # _data sends message that this variable is a private part of class.
        temp = vectors[0].copy()
        self._data = [temp]
        self.num_rows = 1
        for i in range(1, len(vectors)):
            if isinstance(vectors[i], vector.Vector) and vectors[i].dim == self.num_cols:
                self._data.append(vectors[i].copy())
                self.num_rows += 1
            else:
                raise TypeError("All inputs must be Vectors of same dimension.")

    def __str__(self):
        """
        Creates str for Matrix
        :return: str of Matrix row by column
        """
        data_string = f"/{self._data[0][0]}"
        for i in range(1, len(self._data[0])):
            if i < len(self._data[0]) - 1:
                data_string += f", {self._data[0][i]}"
            elif i == len(self._data[0]) - 1:
                data_string += f", {self._data[0][-1]}\\\n"
        if len(self._data[0]) == 1:
            data_string += f"\\\n"
                
        for i in range(1, len(self._data)):
            if i < len(self._data) - 1: # In the middle of the Matrix.
                data_string += f"|{self._data[i][0]}"
                for j in range(1, len(self._data[i])):
                    if j < len(self._data[i]) - 1:
                        data_string += f", {self._data[i][j]}"
                    elif j == len(self._data[i]) - 1:
                        data_string += f", {self._data[i][-1]}|\n"
                if len(self._data[i]) == 1:
                    data_string += f"|\n"
                        
            elif i == len(self._data) - 1: # At the end of the Matrix.
                data_string += f"\\{self._data[-1][0]}"
                for j in range(1, len(self._data[-1])):
                    if j < len(self._data[-1]) - 1:
                        data_string += f", {self._data[-1][j]}"
                    elif j == len(self._data[-1]) - 1:
                        data_string += f", {self._data[-1][-1]}/"
                if len(self._data[i]) == 1:
                    data_string += f"/"
                    
        return data_string

    def copy(self):
        """
        Creates deep copy of Matrix so it is not referenced.
        :return: deep copy of Matrix
        """
        temp = []
        for value in self._data:
            temp.append(value.copy())
        return Matrix(*temp)

    def __getitem__(self, index):
        """
        Takes index (row x column) and gives value.
        :param index: tuple of two int (row, column).
        :return: float at position index.
        """
        if isinstance(index, tuple) and len(index) == 2:
            for i in range(len(index)):
                if isinstance(index[i], int):
                    if 0 <= index[0] <= self.num_rows - 1:
                        number = self._data[index[0]]
                        if 0 <= index[1] <= self.num_cols - 1:
                            number = number[index[1]]
                        else:
                            raise IndexError("Number of columns given exceeded index range.")
                    else:
                        raise IndexError("Number of rows given exceeded index range.")
                else:
                    raise TypeError("Values inside tuple must be int.")
        else:
            raise TypeError("Index must be in form of tuple with two values.")
        return number

    def __setitem__(self, index, value):
        """
        Takes value given and replaces value at index given.
        :param index: tuple of two int (row, column).
        :param value: int or float
        :return: None
        """
        if isinstance(value, (float,int)):
            if isinstance(index, tuple) and len(index) == 2:
                for i in range(len(index)):
                    if isinstance(index[i], int):
                        if 0 <= index[0] <= self.num_rows - 1:
                            if 0 <= index[1] <= self.num_cols - 1:
                                self._data[index[0]][index[1]] = float(value)
                            else:
                                raise IndexError("Number of columns given exceeded index range.")
                        else:
                            raise IndexError("Number of rows given exceeded index range.")
                    else:
                        raise TypeError("Values inside tuple must be int.")
            else:
                raise TypeError("Index must be tuple with two values (row, column).")
        else:
            raise TypeError("Value given must be float or int.")

    def get_row(self, row):
        """
        Returns given row in Matrix as Vector.
        :param row: int.
        :return: Vector.
        """
        if isinstance(row, int):
            if 0 <= row <= self.num_rows - 1:
                return self._data[row]
            else:
                raise IndexError("Number of rows given exceeded index range.")
        else:
            raise TypeError("Row must be int.")

    def get_column(self, column):
        """
        Returns given column in Matrix as Vector.
        :param column: int.
        :return: Vector.
        """
        temp_list = []
        if isinstance(column, int):
            for i in range(self.num_rows):
                temp_list.append(self._data[i][column])
        else:
            raise TypeError("Column must be int.")
        return vector.Vector(*temp_list)

    def set_row(self, index, n_vector): # If argument named 'vector', program breaks.
        """
        Replaces existing row with given row.
        :param index: int
        :param n_vector: new Vector object.
        :return: None
        """
        if isinstance(index, int):
            if isinstance(n_vector, vector.Vector):
                if len(self._data[index]) == len(n_vector):
                    self._data[index] = n_vector.copy() # Super important to copy here.
                else:
                    raise ValueError("Vector given does not have same dim as before.")
            else:
                raise TypeError("Vector given must be a Vector.")
        else:
            raise TypeError("Index given must be int.")

    def set_column(self, index, n_vector):
        """
        Replaces existing column with given column.
        :param index: int.
        :param n_vector: new Vector object.
        :return: None
        """
        if isinstance(index, int):
            if isinstance(n_vector, vector.Vector):
                if self.num_rows == len(n_vector):
                    for i in range(self.num_rows):
                        self._data[i][index] = n_vector[i]
                else:
                    raise ValueError("Vector given does not have same dim as previous column.")
            else:
                raise TypeError("Vector given must be a Vector.")
        else:
            raise TypeError("Index given must be int.")
                        

    def __add__(self, other):
        """
        Adds Matrix to other Matrix.
        :param other: Matrix of same dimensions as self.
        :return: Matrix.
        """
        temp_list = []
        if isinstance(other, Matrix):
            if self.num_rows == other.num_rows and self.num_cols == other.num_cols:
                for i in range(self.num_rows):
                    number = self._data[i] + other._data[i]
                    temp_list.append(number)
            else:
                raise IndexError("Matrix dimensions do not match.")
        else:
            raise TypeError("other must be Matrix.")
        return Matrix(*temp_list)

    def __sub__(self, other):
        """
        Subtracts Matrix by other Matrix.
        :param other: Matrix of same dimensions as self.
        :return: Matrix.
        """
        temp_list = []
        if isinstance(other, Matrix):
            if self.num_rows == other.num_rows and self.num_cols == other.num_cols:
                for i in range(self.num_rows):
                    number = self._data[i] - other._data[i]
                    temp_list.append(number)
            else:
                raise IndexError("Matrix dimensions do not match.")
        else:
            raise TypeError("other must be Matrix.")
        return Matrix(*temp_list)

    def __mul__(self, other):
        """
        Multiplies Matrix by other Matrix, scalar, or vector.
        :param other: scalar, Vector, or Matrix.
        :return: Matrix.
        """
        temp_list = []
        if isinstance(other, (int, float)): # Is scalar.
            for i in range(self.num_rows):
                number = self._data[i] * other
                temp_list.append(number)
                
        elif isinstance(other, vector.Vector): # Is vertical Vector.
            num_list = []
            for i in range(self.num_rows):
                num_list.append(vector.dot(self._data[i], other))
                temp_list.append(vector.Vector(num_list[i]))
                                  
        elif isinstance(other, Matrix): # Is Matrix.
            if self.num_cols == other.num_rows:
                num_list = []
                vect_list = []
                for i in range(self.num_rows):
                    for j in range(other.num_cols):
                        column = other.get_column(j)
                        num_list.append(vector.dot(self._data[i], column))
                    vect_list.append(num_list[:]) # Allows transport of ints outside loop.
                    num_list.clear() # Stops multiple ints being readded to list.
                for i in range(len(vect_list)):
                    temp_list.append(vector.Vector(*vect_list[i])) # Unpacks ints within vect_list and converts to Vector.
            else:
                raise IndexError("Number of Columns of first Matrix must equal number of Rows of other Matrix.")
        else:
            raise TypeError("other must be int, float, Matrix, or Vector.")
        
        return Matrix(*temp_list)

    def __rmul__(self, other):
        """
        Allows multiplication on the right of Matrix.
        :param other: scalar or Vector. Matrix not needed because it is covered by __mul__.
        :return: Matrix.
        """
        temp_list = []
        if isinstance(other, (int, float)): # Is scalar.
            return self * other

        elif isinstance(other, vector.Vector): # Is horizontal Vector.
            num_list = []
            vect_list = []
            # No need to go through vector rows, since there is only 1
            for j in range(self.num_cols):
                column = self.get_column(j)
                num_list.append(vector.dot(other, column))
            vect_list.append(num_list[:])
            num_list.clear()
            for i in range(len(vect_list)):
                temp_list.append(vector.Vector(*vect_list[i])) # Unpacks ints within vect_list and converts to Vector.
            return Matrix(*temp_list)

    def __neg__(self):
        """
        Gives negative of Matrix given
        :param self: Matrix
        :return: Matrix (but negative)
        """
        return self * -1

    def __eq__(self, other):
        """
        Checks if two Matrices are equal
        :param other: Matrix
        :return: boolean
        """
        if isinstance(other, Matrix) and other.num_rows == self.num_rows and other.num_cols == self.num_cols:
            eq_rows = 0 # Needed so program checks each row instead of returning true or false only after checking one.
            for i in range(self.num_rows):
                if self._data[i] == other._data[i]:
                    eq_rows += 1
                else:
                    return False
            if eq_rows == self.num_rows:
                return True
        else:
            return False

    def det(self):
        """
        Returns determinate of square Matrix.
        :param self: Matrix.
        :return: determinant as float.
        """
        if self.num_rows == self.num_cols: # Can be done without hard coding.
            if self.num_rows == 2:
                a = self._data[0][0]
                b = self._data[0][1]
                c = self._data[1][0]
                d = self._data[1][1]
                det = (a*d) - (b*c)
            elif self.num_rows == 3:
                a = self._data[0][0]
                b = self._data[0][1]
                c = self._data[0][2]
                d = self._data[1][0]
                e = self._data[1][1]
                f = self._data[1][2]
                g = self._data[2][0]
                h = self._data[2][1]
                i = self._data[2][2]
                det = a*(e*i - f*h) + b*(f*g - d*i) + c*(d*h - e*g)
            elif self.num_rows == 4:
                det = (1/24)*((trace(self)**4) - 6*(trace(self)**2) * trace(self*self) + 3*(trace(self*self)**2) + 8*(trace(self)*trace(self*self*self)) - 6*(trace(self*self*self*self)))
            else:
                return NotImplemented
        else:
            raise TypeError("Must input sqaure Matrix.")
        return det

    def transpose(self):
        """
        Returns transpose of given Matrix.
        :param self: Matrix.
        :return: Transpose
        """
        temp_list = []
        for i in range(self.num_cols):
            temp_list.append(self.get_column(i))
        return Matrix(*temp_list) 
        
def identity(rows):
    """
    Gives identity for given number of rows.
    :param rows: int.
    :return: Matrix.
    """
    if isinstance(rows, int):
        M = zero(rows, rows)
        for i in range(rows):
            M._data[i][i] = 1
    else:
        raise TypeError("rows must be int.")
    return M        

def zero(rows, columns):
    """
    Gives matrix of all zeros based on given rows and columns.
    :param rows: int.
    :param columns: int.
    :return: Matrix.
    """
    temp_list = []
    row_list = []
    vector_list = []
    if isinstance(rows, int) and isinstance(columns, int):
        for i in range(columns):
            temp_list.append(0)
        for j in range(rows):
            row_list.append(temp_list[:])
        for i in range(len(row_list)):
            vector_list.append(vector.Vector(*row_list[i]))
    else:
        raise TypeError("Rows and Columns must be given as int.")
    return Matrix(*vector_list)

def ones(rows, columns):
    """
    Gives matrix of all zeros based on given rows and columns.
    :param rows: int.
    :param columns: int.
    :return: Matrix.
    """
    temp_list = []
    row_list = []
    vector_list = []
    if isinstance(rows, int) and isinstance(columns, int):
        for i in range(columns):
            temp_list.append(1)
        for j in range(rows):
            row_list.append(temp_list[:])
        for i in range(len(row_list)):
            vector_list.append(vector.Vector(*row_list[i]))
    else:
        raise TypeError("Rows and Columns must be given as int.")
    return Matrix(*vector_list)

def trace(matrix):
    """
    Returns trace of given Matrix.
    :param matrix: Square Matrix
    :return: Trace of square Matrix
    """
    if isinstance(matrix, Matrix):
        if matrix.num_rows == matrix.num_cols:
            trace = 0
            rows = 0
            for i in range(matrix.num_cols):
                trace += matrix._data[rows][i]
                rows += 1
        else:
            raise TypeError("Must input square Matrix.")
    else:
        raise TypeError("matrix must be Matrix.")
    return trace
        
def inverse(matrix):
    """
    Returns inverse of given Matrix if possible.
    :param matrix: Sqaure Matrix (either 2x2, 3x3, or 4x4).
    :return: Matrix.
    """
    if isinstance(matrix, Matrix):
        if matrix.num_rows == matrix.num_cols:
            det = matrix.det()
            if det != 0:
                multiplier = (1/det)
                m_copy = matrix.copy()
                if matrix.num_rows == 2:
                    a = m_copy._data[0][0]
                    b = m_copy._data[0][1]
                    c = m_copy._data[1][0]
                    d = m_copy._data[1][1]
                    m_copy[0,0] = d
                    m_copy[1,1] = a
                    m_copy[0,1] = -b
                    m_copy[1,0] = -c
                    inverse = (multiplier)*(m_copy)
                elif matrix.num_rows == 3:
                    inside = (1/2) * ((trace(m_copy)**2) - trace(m_copy * m_copy)) * identity(3) - m_copy * trace(m_copy) + (m_copy * m_copy)
                    inverse = multiplier * inside
                elif matrix.num_rows == 4:
                    inside = (1/6) * ((trace(m_copy)**3) - 3 * trace(m_copy) * trace(m_copy * m_copy)
                                    + 2 * trace(m_copy * m_copy * m_copy)) * identity(4) - (1/2) * m_copy * ((trace(m_copy)**2)
                                                                                                        - trace(m_copy * m_copy)) + (m_copy * m_copy) * trace(m_copy) - (m_copy * m_copy * m_copy)
                    inverse = multiplier * inside
                else:
                    return NotImplemented
            else:
                raise ValueError("Matrix is not invertible by IMT because determinant is equal to zero.")
        else:
            raise ValueError("Matrix must be square in order to be invertible.")
    else:
        raise TypeError("Matrix must be a matrix to be invertible.")
    return inverse
    
def rotate(angle):
    """
    Creates 2D rotation matrix given angle
    :param angle: angle in radians, int or float
    :return: Matrix
    """
    if isinstance(angle, (float,int)):
        row1 = vector.Vector(math.cos(angle), math.sin(angle))
        row2 = vector.Vector(-math.sin(angle), math.cos(angle))
        R_M = Matrix(row1, row2)
    else:
        raise TypeError("angle must be int or float.")
    return R_M

def hg(value):
    """
    Converts vector or matrix to homogeneous coordinates.
    :param value: Matrix or Vector
    :return: Matrix or Vector.
    """
    temp_list = []
    if isinstance(value, vector.Vector):
        temp = value.copy()
        temp.data.append(float(1))
        temp = vector.Vector(*temp.data)
        return temp
    elif isinstance(value, Matrix):
        for i in range(value.num_rows):
            temp = value._data[i].copy()
            temp.data.append(float(1))
            temp = vector.Vector(*temp.data)
            temp_list.append(temp)
        return Matrix(*temp_list)
    else:
        raise TypeError("value must be Vector or Matrix.")

def translate(dim, dx, dy, dz=1):
    """
    Creates a translation matrix in given dimension with given dx, dy, and dz if given.
    :param dim: int representing dim of Matrix. Max 3, min 2.
    :param dx: Change in x-value for translation. Int or float.
    :param dy: Change in y-value for translation. Int or float.
    :param dz: Change in z-value for translation. Int or float. Optional.
    :return: Matrix.
    """
    if isinstance(dim, int):
        if isinstance(dx, (float, int)) and isinstance(dy, (float, int)) and isinstance(dz, (float, int)):
            if dim == 2:
                T = identity(dim + 1)
                T[dim, 0] = dx
                T[dim, 1] = dy
            elif dim == 3:
                T = identity(dim + 1)
                T[dim, 0] = dx
                T[dim, 1] = dy
                T[dim, 2] = dz
            else:
                return NotImplemented
        else:
            return TypeError("dx, dy, and dz must all be ints or floats.")
    else:
        return TypeError("dim must be int.")
    return Matrix(*T._data) # Resets number of rows and columns

def project(dim_desired):
    """
    Creates projection from either 3D to 2D or 4D to 3D.
    :param dim_desired: Dimension of matrix user would like to project to.
    :return: Matrix.
    """
    if isinstance(dim_desired, int):
        P = identity(dim_desired)
        if dim_desired == 2:
            P._data.append(vector.Vector(0, 0))
        elif dim_desired == 3:
            P._data.append(vector.Vector(0, 0, 0))
        else:
            return NotImplemented
    else:
        return TypeError("dim_desired must be int.")
    return Matrix(*P._data) # Resets number of rows and columns
