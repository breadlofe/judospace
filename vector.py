# Dustin Simpkins
# ETGG 1803 Lab 05
# March 9, 2022
# <RESOURCES>

"""
This module contains a Vector class with some general vector operations as well as a Vector2 class and a Vector3 class
with specific methods and properties. It also contains functions for dot product, cross product, and conversion
from polar coordinates to a two-dimensional Vector2.
"""

# This Vector class is mostly correct. Part of it was used to show various things that could go wrong. I think I
# fixed all the errors but DO NOT trust it completely until you have checked it.

# DO NOT share this file with anyone else.

import math


class Vector(object):
    def __init__(self, *args):
        """
        The constructor for the Vector class.
        :param *args: A variable length argument list of ints or floats
        :return: N/A for constructors
        """
        self.data = []
        for value in args:
            if isinstance(value, (float, int)):
                self.data.append(float(value))
            else:
                raise TypeError('Only integer or float values can be accepted.')

        self.dim = len(self.data)

        if self.dim == 2:
            self.__class__ = Vector2
        elif self.dim == 3:
            self.__class__ = Vector3

    def __getitem__(self, index):
        """
        Return the value at the given index.
        :param index: An integer index
        :return: The float value at position index
        """
        if isinstance(index, int):
            if -self.dim <= index <= self.dim - 1:
                return self.data[index]
            return IndexError('Index out of range.')
        return TypeError('The position must be an integer index.')

    def __setitem__(self, index, value):
        """
        Update the value at the given index with the specified value.
        :param index: integer index to be updated
        :param value: new float value value
        :return: Returns None. Changes the list index with the value.
        """
        if isinstance(value, (float, int)):
            self.data[index] = float(value)
        else:
            raise TypeError('Only integer or float values can be accepted.')

    def __str__(self):
        """
        Return a formatted string of the form <Vector{dim}: {data}> for use with print().
        Do not call this method directly.
        :return: a formatted string for use with print
        """
        data_string = f'<Vector{self.dim}:'
        for i in range(self.dim):
            if i < self.dim - 1:
                data_string += ' ' + str(self[i]) + ','
            elif i == self.dim - 1:
                data_string += ' ' + str(self[i]) + '>'
        return data_string

    def __len__(self):
        """
        Return the number of elements in an instance of the Vector class.
        :param: N/A
        :return: Returns length of self.data
        """
        return len(self.data)

    def __eq__(self, other):
        """
        Overload == operator.
        Return boolean indicating whether other is a Vector equal to self.
        :param other: A Vector
        :return: If all the the vector parameters are equal, returns True. Otherwise, False
        """
        if isinstance(other, Vector) and self.dim == other.dim:
            for i in range(self.dim):
                if self[i] != other[i]:
                    return False
            return True
        return False

    def copy(self):
        """
        Return a deep copy of an instance of the Vector class.
        :param: N/A
        :return: A deep copy of the Vector
        """
        # Note: This could be completed with the single line return Vector(*self.data)
        # but the approach used here carries over to other deep copy scenarios like a Matrix class.
        temp = []
        for value in self.data:
            temp.append(value)
        return Vector(*temp)

    def __mul__(self, other):
        """
        Overload the * operator.
        Return the product of a Vector and a scalar, or NotImplemented for other data types.
        :param other: int or float. Other data types NotImplemented
        :return: The vector multiplied on the right by a scalar
        """
        if isinstance(other, (float, int)):
            v = self.copy()
            for i in range(self.dim):
                v[i] *= other
            return v
        else:
            # raise TypeError("Can only multiply a vector by a float or integer scalar.")
            return NotImplemented

    def __rmul__(self, other):
        """
        Overload the * operator when the Vector is on the right.
        :param other: int or float
        :return: The vector multiplied on the left by a scalar
        """
        return self * other

    def __add__(self, other):
        """
        Overload the + operator.
        Return the sum of self and a Vector other if the dimensions match.
        :param other: A Vector of the same dimension as self
        :return: The Vector sum of self and other
        """
        if isinstance(other, Vector) and self.dim == other.dim:
            v = self.copy()
            for i in range(self.dim):
                v[i] += other[i]
            return v
        else:
            raise TypeError('You can only add another Vector' + str(self.dim) + ' to this Vector' + str(
                self.dim) + ' (You passed "' + str(other) + '".)')

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        """
        Overload the - operator.
        :param other: A Vector
        :return: The Vector self - other
        """
        return self + -other

    def __neg__(self):
        """
        Negate a Vector.
        :param: A Vector instance
        :return: The negative of the Vector
        """
        return self * -1

    def __truediv__(self, other):
        """
        Overload the / operator.
        :param other: A float or an int
        :return: A Vector divided by the scalar other
        """
        if isinstance(other, (float, int)) and other != 0:
            v = self.copy()
            for i in range(self.dim):
                v[i] /= float(other)
            return v
        elif other == 0:
            raise ZeroDivisionError('Cannot divide a Vector by 0.')
        else:
            raise TypeError('Can only divide a Vector by a non-zero float or integer scalar.')

    # NEW (Lab 5) v

    def norm(self, p):
        """
        Finds p-norm of a Vector.
        :param p: pos int or str 'infinity'
        :return: p-norm value
        """
        if isinstance(p, int) and p > 0:
            values = 0
            for i in range(self.dim):
                values += abs(self[i] ** p)
            norm = (values) ** (1 / p)
        elif isinstance(p, str) and p == "infinity":
            value_list = []
            for i in range(self.dim):
                value_list.append(abs(self[i]))
            norm = max(value_list)
        else:
            raise TypeError("p must be positive int or str 'infinity'.")
        return norm

    @property
    def mag(self):
        """
        Finds 2-norm of Vector by using square roots.
        :param: Vector
        :return: 2-norm of Vector
        """
        values = 0
        for i in range(self.dim):
            values += abs(self[i] ** 2)
        norm = (values) ** (1 / 2)
        return norm

    @property
    def mag_squared(self):
        """
        Finds 2-norm of Vector without square root.
        :param: Vector
        :return: 2-norm of Vector
        """
        values = 0
        for i in range(self.dim):
            values += abs(self[i] ** 2)
        return values

    @property
    def normalize(self):
        """
        Normalizes Vector.
        :param: Vector
        :return: Unit form of Vector
        """
        return self / self.mag

    @property
    def is_zero(self):
        """
        Checks to see if Vector is Zero Vector.
        :param: Vector
        :return: Bool
        """
        temp_list = []
        for i in range(self.dim):
            temp_list.append(self[i])
        for j in range(len(temp_list)):
            if temp_list[j] > 0:
                return False
        return True

    @property
    def i(self):
        """
        Converts Vector into tuple of coordinates.
        :param: Vector
        :return: Tuple
        """
        temp_list = []
        for i in range(self.dim):
            temp_list.append(int(self[i]))
        return tuple(temp_list)


# NEW (Lab 5) ^

class Vector2(Vector):
    def __init__(self, x, y):
        """
        The constructor for the Vector2 class.
        :parameters: Floats or ints x and y
        :return: Creates a vector instance that is in Vector and Vector2 class
        """
        super().__init__(x, y)

    @property
    def x(self):
        """
        Return the x value of a Vector2.
        :param: N/A
        :return: The x component
        """
        return self[0]

    @x.setter
    def x(self, newvalue):
        """
        Change the x value of a Vector2.
        :param: The integer or float value to which x should be changed
        :return: Returns None. Changes x value to new value.
        """
        if isinstance(newvalue, (int, float)):
            self[0] = float(newvalue)
        else:
            raise TypeError('Only integer or float values can be accepted.')

    @property
    def y(self):
        """
        Return the y value of a Vector2.
        :param: N/A
        :return: The y component
        """
        return self[1]

    @y.setter
    def y(self, newvalue):
        """
        Change the y value of a Vector2.
        :param: The integer or float value to which y should be changed
        :return: Returns None. Changes y value to new value.
        """
        if isinstance(newvalue, (int, float)):
            self[1] = float(newvalue)
        else:
            raise TypeError('Only integer or float values can be accepted.')

    # NEW (Lab 5) V

    @property
    def degrees(self):
        """
        Finds the degree of a Vector2 in polar space.
        :param: Vector2
        :return: Returns degree value.
        """
        radians = math.asin(self.y / self.mag)
        degrees = radians * (180 / math.pi)
        return degrees

    @property
    def degrees_inv(self):
        """
        Finds the degree of a Vector2 in polar space (negates y for pygame).
        :param: Vector2
        :return: Returns degree value.
        """
        radians = math.asin(-self.y / self.mag)
        degrees = radians * (180 / math.pi)
        return degrees

    @property
    def radians(self):
        """
        Finds the radians of a Vector2 in polar space.
        :param: Vector2
        :return: Returns radian value.
        """
        radians = math.asin(self.y / self.mag)
        return radians

    @property
    def radians_inv(self):
        """
        Finds the radians of a Vector2 in polar space (negates y for pygame).
        :param: Vector2
        :return: Returns radian value.
        """
        radians = math.asin(-self.y / self.mag)
        return radians

    @property
    def perpendicular(self):
        """
        Creates a Vector2 perpendicular to inputed Vector2
        :param: Vector2
        :return: Returns perpednicular Vector2
        """
        p_selfx = -self.y
        p_selfy = self.x
        perpendicular = Vector2(p_selfx, p_selfy)
        return perpendicular

    # NEW (Lab 5) ^


class Vector3(Vector):
    def __init__(self, x, y, z):
        """
        The constructor for the Vector3 class.
        :parameters: Floats or ints x, y, and z
        :return: Creates a vector instance that is in Vector and Vector3 class
        """
        super().__init__(x, y, z)

    @property
    def x(self):
        """
        Return the x value of a Vector3.
        :param: N/A
        :return: The x component
        """
        return self[0]

    @x.setter
    def x(self, new_value):
        """
        Change the x value of a Vector3.
        :param: The integer or float value to which x should be changed
        :return: Returns None. Changes x value to new value.
        """
        if isinstance(new_value, (int, float)):
            self[0] = float(new_value)
        else:
            raise TypeError('Only integer or float values can be accepted.')

    @property
    def y(self):
        """
        Return the y value of a Vector3.
        :param: N/A
        :return: The y component
        """
        return self[1]

    @y.setter
    def y(self, new_value):
        """
         Change the y value of a Vector3.
        :param: The integer or float value to which y should be changed
        :return: Returns None. Changes y value to new value.
        """
        if isinstance(new_value, (int, float)):
            self[1] = float(new_value)
        else:
            raise TypeError('Only integer or float values can be accepted.')

    @property
    def z(self):
        """
        Return the z value of a Vector3.
        :param: N/A
        :return: The z component
        """
        return self[2]

    @z.setter
    def z(self, new_value):
        """
        Change the z value of a Vector3.
        :param: The integer or float value to which z should be changed
        :return: Returns None. Changes z value to new value.
        """
        if isinstance(new_value, (int, float)):
            self[2] = float(new_value)
        else:
            raise TypeError('Only integer or float values can be accepted.')


# NEW (Lab 5) V

def dot(v, w):
    """
    Takes dot product of two vectors and returns number.
    :param v, w: Vectors of same dimension
    :return: Dot product
    """
    if isinstance(v, Vector) and isinstance(w, Vector):
        if v.dim == w.dim:
            dot_product = 0
            for i in range(v.dim):
                mul = v[i] * w[i]
                dot_product += mul
            return dot_product
        else:
            raise TypeError("Vectors must be in same dimension.")
    else:
        raise TypeError("Only Vector types can be accepted.")


def cross(v, w):
    """
    Takes the cross product of two Vector3's and returns a Vector3.
    :param v, w: Vector3
    :return: Cross product
    """
    if isinstance(v, Vector3) and isinstance(w, Vector3):
        x = (v.y * w.z) - (w.y * v.z)
        # -0 checks append issue where zeros have negative signs.
        if x == -0:
            x = 0
        y = -((v.x * w.z) - (w.x * v.z))
        if y == -0:
            y = 0
        z = (v.x * w.y) - (w.x * v.y)
        if z == -0:
            z = 0
        cross_product = Vector(x, y, z)
        return cross_product
    else:
        raise TypeError("Cross product can only be obtained with Vector3.")


def polar_to_Vector2(r, theta, pygame="no"):
    """
    Takes polar coordinates, radius and angle in radians, and converts to Vector2.
    :param: radius and theta as int or float, argument for yes or no str
    :return: Vector2
    """
    if isinstance(r, (float, int)) and isinstance(theta, (float, int)):
        x_val = (math.cos(theta) * r)
        # If statements of values get rid of extremely small floats.
        if x_val < 0.000000000001 and x_val > -0.00000000001:
            x_val = 0
        if pygame == "no":
            y_val = (math.sin(theta) * r)
            if y_val < 0.000000000001 and y_val > -0.00000000001:
                y_val = 0
        elif pygame == "yes":
            y_val = -(math.sin(theta) * r)
            if y_val < 0.000000000001 and y_val > -0.00000000001:
                y_val = 0
        else:
            raise ValueError("Typed str can only be 'yes' or 'no'.")
        new_vect = Vector2(x_val, y_val)
        return new_vect
    else:
        raise TypeError("r and theta must be int or float.")

# NEW (Lab 5) ^

