# Dustin Simpkins
# Shape matrix shenanigans
import matrix as m
import vector
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
