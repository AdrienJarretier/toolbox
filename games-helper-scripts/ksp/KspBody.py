import math
from scipy.constants import G, g


def semiMajorAxis(centralBodyRadius, apoapsisAltitude, periapsisAltitude):

    return ((apoapsisAltitude+periapsisAltitude)/2) + centralBodyRadius


def orbitalSpeed(centralBodyRadius, centralBodyGravitationalParameter, apoapsisAltitude: float, periapsisAltitude: float, currentAltitude: float = None) -> float:
    """
    Compute orbital speed at a given altitude on the given orbit around the given body

    Args:
        centralBodyRadius: the radius of the orbited body.
        centralBodyGravitationalParameter: the standard Gravitational Parameter of the orbited body.
        apoapsisAltitude, periapsisAltitude : altitudes in meters
        currentAltitude: OPTIONAL, in meters from surface, if ommited, compute speed from an assumed circular orbit at an average altitude

    Returns:
        float: orbital speed in m/s at the current altitude
    """

    a = semiMajorAxis(centralBodyRadius, apoapsisAltitude, periapsisAltitude)

    currentAltitude = currentAltitude or a-centralBodyRadius

    # distance from central body center
    r = currentAltitude+centralBodyRadius

    mu = centralBodyGravitationalParameter

    return (mu*(2/r-1/a))**(0.5)


class KspBody:

    bodies = {}

    # return bodies names as a list
    @classmethod
    def bodiesList(cls):
        return list(cls.bodies.keys())

    # mass in kg
    # radius in meters
    # rotationPeriod (sidereal rotation) in seconds
    def __init__(self, name: str, mass: float, radius: float, rotationPeriod: float, soi: float, atmoHeight: float):
        """
        Instantiate new Body such as Kerbin

        Args:
            name:
            mass: in kg
            radius: in meters
            rotationPeriod: sidereal rotation in seconds
            soi: Sphere of Influence in meters
            atmoHeight: upper limit of the atmosphere in meters
        """

        self.name = name
        self.mass = mass
        self.radius = radius
        self.rotationPeriod = rotationPeriod
        self.soi = soi
        self.atmoHeight = atmoHeight

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

    def reachingSpaceCompute(self) -> dict:
        timeToReach = math.sqrt(2*self.atmoHeight/g)
        deltaVToReach = g*timeToReach
        speedUponReachingSpace = deltaVToReach+self.surfaceLinearSpeed()
        wasteddeltaV = g*timeToReach

        missingSpeed = orbitalSpeed(self.radius, self.standardGravitationalParameter,
                                    self.atmoHeight, self.atmoHeight) - speedUponReachingSpace

        deltaV_from_ground_to_lowestOrbit = missingSpeed + wasteddeltaV + deltaVToReach
        return {
            'timeToReach': timeToReach,
            'deltaVToReach': deltaVToReach,
            'speedUponReachingSpace': speedUponReachingSpace,
            'wasteddeltaV': wasteddeltaV,
            'deltaV_from_ground_to_lowestOrbit': deltaV_from_ground_to_lowestOrbit
        }


KspBody("kerbin", 5.2915158e22, 600e3, 21549.425, None, 70000)
KspBody("mun", 9.76e20, 200e3, 138984.38, 2429559.1, 0)
KspBody("minmus", 2.646e19, 60e3, 1*6*3600+5*3600+13*60, None, 0)
KspBody("sun", 1.7565459e28, 261600000, 432000, None, None)
