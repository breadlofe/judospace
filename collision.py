# Dustin Simpkins
import math

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
