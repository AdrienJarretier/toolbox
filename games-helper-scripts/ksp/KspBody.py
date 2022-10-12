import math
from scipy.constants import G


class KspBody:

    bodies = {}

    # return bodies names as a list
    @classmethod
    def bodiesList(cls):
        return list(cls.bodies.keys())

    # mass in kg
    # radius in meters
    # rotationPeriod (sidereal rotation) in seconds
    def __init__(self, name, mass, radius, rotationPeriod, soi):

        self.name = name
        self.mass = mass
        self.radius = radius
        self.rotationPeriod = rotationPeriod
        self.soi = soi

        self.standardGravitationalParameter = G * self.mass

        self.bodies[name] = self

    def surfaceLinearSpeed(self) -> float:
        """
        Compute surface linear speed from radius and rotation Period

        Returns :
            float: the surface linear speed in meters/sec
        """
        circumference = 2*math.pi*self.radius
        return circumference/self.rotationPeriod


KspBody("kerbin", 5.2915158e22, 600e3, 21549.425, None)
KspBody("mun", 9.76e20, 200e3, 138984.38, 2429559.1)
KspBody("minmus", 2.646e19, 60e3, 1*6*3600+5*3600+13*60, None)
KspBody("sun", 1.7565459e28, 261600000, 432000, None)
