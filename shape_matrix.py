# Dustin Simpkins
# Shape matrix shenanigans
import matrix as m
import vector
import math
# CONVERSION METHOD

def convert(matrix):
    """
    Takes Matrix and converts it to list so it can be used by pygame.
    :param matrix: Matrix.
    :return: list.
    """
    if isinstance(matrix, m.Matrix):  # Checks if matrix is Matrix.
        temp_list = []  # Creates temp_list to store values of rows.
        for i in range(matrix.num_rows):  # Goes through each row.
            temp_list.append(matrix._data[i].data)  # Appends .data (list of values) of each vector in i.
        return temp_list

# Defining function to find area of triangle using Linear Algebra.
def area_of_triangle(vect1, vect2):
    """
    Takes two vectors, or sides of traingles, and gives back area of triangle.
    :param vect1: vector3
    :param vect2: vector3
    :return: float
    """
    if isinstance(vect1, vector.Vector) and isinstance(vect2, vector.Vector):
        # Error handling to see if they are vectors.
        return (vector.cross(vect1, vect2)).mag / 2
        # Vector3 error not necessary since it is covered by cross product error handling.
    else:
        raise TypeError("Needs vectors")

# Defining function that converts 2D Matrix to 3D for triangles
def make_3D(matrix):
    """
    Takes 2D Matrix and adds third dimension by adding column of zeros.
    :param matrix: Matrix
    :return: Matrix
    """
    if isinstance(matrix, m.Matrix) and matrix.num_cols == 2:
        matrix = m.hg(matrix)  # Converting triangle point vectors to vector3 for future cross product.
        matrix.set_column(2, vector.Vector(0, 0, 0))
        # Getting rid of 1's from homogeneous conversion to not alter cross product solution.
    else:
        raise TypeError("Matrix must be 2D Shape Matrix.")
    return matrix

def rotate_3D(theta):
    """
    Creates a 3D rotation matrix.
    :param theta: Angle in radians.
    :return: 3D rotation matrix.
    """
    if isinstance(theta, (int, float)):
        r_m = m.Matrix(vector.Vector(math.cos(theta), math.sin(theta), 0),
                       vector.Vector(-math.sin(theta), math.cos(theta), 0),
                       vector.Vector(0, 0, 1))
    else:
        raise TypeError("Theta must be int or float.")
    return r_m

def full_rotation(matrix, theta, dx, dy):
    """
    Converts to 3D, translates, rotates, invert translate.
    :param matrix: matrix.Matrix
    :param theta: int or float in radians.
    :param dx: int or float to be translated by.
    :param dy: int or float to be translated by.
    :return: Matrix.
    """
    if isinstance(matrix, m.Matrix) and matrix.num_cols == 2:
        if isinstance(theta, (int, float)):
            if isinstance(dx, (int, float)):
                if isinstance(dy, (int, float)):
                    matrix = make_3D(matrix)
                    # matrix = matrix * m.translate(2, dx, dy) * rotate_3D(theta) * m.inverse(m.translate(2, dx, dy))
                    matrix = matrix * m.inverse(m.translate(2, dx, dy)) * rotate_3D(theta) * m.translate(2, dx, dy) # Still problematic.
                    matrix = matrix * m.project(2)
                else:
                    raise TypeError("dy must be int or float.")
            else:
                raise TypeError("dx must be int or float.")
        else:
            raise TypeError("Theta must be int or float.")
    else:
        raise TypeError("Matrix must be a matrix.")
    return matrix

