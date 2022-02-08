from scipy.constants import G

class KspBody:

    bodies = {}

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

KspBody("kerbin", 5.2915158e22, 600e3, 21549.425, None)
KspBody("mun", 9.76e20, 200e3, 138984.38, 2429559.1)
KspBody("minmus", 2.646e19, 60e3, 1*6*3600+5*3600+13*60, None)
KspBody("sun", 1.7565459e28, 261600000, 432000, None)