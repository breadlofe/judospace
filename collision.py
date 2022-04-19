# Dustin Simpkins
import math
import shape_matrix as sm
import matrix
import vector

class Distance:
    """
    Takes the position of two entities and finds the distance between both center points.
    """
    def __init__(self, point1, point2):
        """
        Takes two points given and creates local variables.
        :param point1: Tuple (x,y)
        :param point2: Tuple (x,y)
        """
        if type(point1) == tuple and type(point2) == tuple and len(point1) == 2 and len(point2) == 2:
            self.obj1 = point1
            self.obj2 = point2
        else:
            raise TypeError("Points given must be tuples (x,y).")
        self.points = [self.obj1, self.obj2]

    def distance(self):
        """
        Takes two points, checks to see if values within are float/int, then completes distance formula.
        :return: float of distance between two points.
        """
        for point in self.points:
            for i in range(2):
                if type(point[i]) == int or type(point[i]) == float:
                    distance = math.sqrt((self.obj2[0] - self.obj1[0])**2 + (self.obj2[1] - self.obj1[1])**2)
                    return distance
                else:
                    raise TypeError("Points checked must be int or float.")

class Collision:
    """
    Checks to see if distance matches radius of both objects to see if colliding.
    """
    def __init__(self, point1, point2, point1_radius, point2_radius):
        self.obj1 = point1
        self.obj2 = point2
        d = Distance(self.obj1, self.obj2)
        self.distance = Distance.distance(d)
        if isinstance(point1_radius, (int, float)) and isinstance(point2_radius, (int, float)):
            self.obj1_r = point1_radius
            self.obj2_r = point2_radius
        else:
            raise TypeError("Radius must be int or float.")

    def collide(self):
        """
        Checks to see if two points (including radius) are colliding.
        :return: Boolean representing if colliding or not
        """
        if self.distance <= self.obj1_r + self.obj2_r:
            return True
        else:
            return False

class AlphaCollision:
    """
    Checks to see if center vector of projectile circle is in the area of triangle bounds.
    """
    def __init__(self, triangle, proj_x, proj_y):
        """
        Most importantly creates vector for projectile, since there was not one before.
        :param triangle: Shape matrix for triangle.
        :param proj_x: x-value of projectile.
        :param proj_y: y-value of projectile.
        """
        self.tri = triangle  # Remember to use the bounding triangle to account for radius.
        self.proj = vector.Vector(proj_x, proj_y)
        self.proj_3D = vector.Vector(proj_x, proj_y, 0)
        self.radius = 5
        self.tri_3D = sm.make_3D(self.tri)
        self.tri_area = sm.area_of_triangle((self.tri_3D._data[0] - self.tri_3D._data[1]),
                                            (self.tri_3D._data[1] - self.tri_3D._data[2]))

    def collide(self):
        """
        Checks to see if vector is inside of of triangle.
        :return: Boolean.
        """
        circ_to_1 = self.proj_3D - self.tri_3D._data[0]
        circ_to_2 = self.proj_3D - self.tri_3D._data[1]
        circ_to_3 = self.proj_3D - self.tri_3D._data[2]
        a_o_ct1 = sm.area_of_triangle(circ_to_1, circ_to_2)
        a_o_ct2 = sm.area_of_triangle(circ_to_2, circ_to_3)
        a_o_ct3 = sm.area_of_triangle(circ_to_3, circ_to_1)
        if round(a_o_ct1 + a_o_ct2 + a_o_ct3, 5) == round(self.tri_area, 5):
            return True
        else:
            return False
