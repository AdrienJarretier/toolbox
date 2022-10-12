from scipy.constants import pi
from KspBody import KspBody
from utils import *
import math

# apoapsisAltitude, periapsisAltitude  in meters from surface
# return semi major axis, the mean from max radius and min raidus from the center of the body
def semiMajorAxis(centralBody, apoapsisAltitude, periapsisAltitude):

    return ((apoapsisAltitude+periapsisAltitude)/2) + centralBody.radius

# apoapsisAltitude periapsisAltitude  in meters from surface
# optional : currentAltitude in meters from surface, if ommited, compute speed from an assumed circular orbit at an average altitude
# returns Speed in meters / second
def orbitalSpeed(centralBody, apoapsisAltitude, periapsisAltitude, currentAltitude=None):

    a = semiMajorAxis(centralBody, apoapsisAltitude, periapsisAltitude)

    currentAltitude = currentAltitude or a-centralBody.radius

    # distance from central body center
    r = currentAltitude+centralBody.radius

    mu = centralBody.standardGravitationalParameter

    return (mu*(2/r-1/a))**(0.5)

# Compute the time passed on the dark side of the body at lowest altitude, use for evaluating electricity storage capacity required
# return time in seconds
def timeInTheDark(centralBody):
    apoapsisAltitude = 0
    periapsisAltitude = 0
    a = semiMajorAxis(centralBody, apoapsisAltitude, periapsisAltitude)
    perimeter = 2*pi*a
    speed = orbitalSpeed(centralBody, apoapsisAltitude, periapsisAltitude)
    return math.ceil(perimeter/2/speed)


# altitudes in meters
# returns deltaV in meters / second
def transferDeltaV(centralBody, origApoapsis, origPeriapsis, targetApoapsis, targetPeriapsis):

    origSpeed = orbitalSpeed(centralBody, origApoapsis, origPeriapsis, origPeriapsis)
    halfTransferPeriapsisSpeed = orbitalSpeed(centralBody, targetApoapsis, origPeriapsis, origPeriapsis)

    halfTransferApoapsisSpeed = orbitalSpeed(centralBody, targetApoapsis, origPeriapsis, targetApoapsis)
    finalSpeed = orbitalSpeed(centralBody, targetApoapsis, targetPeriapsis, targetApoapsis)

    return (finalSpeed-halfTransferApoapsisSpeed)+(halfTransferPeriapsisSpeed - origSpeed)





# orbitalPeriod in seconds
# Returns semi major axis required to match given orbital period,
# that is average distance from center of orbiting body
def period2semiMajorAxis(centralBody, orbitalPeriod) -> float:

    mu = centralBody.standardGravitationalParameter

    T = orbitalPeriod

    semiMajorAxis = (((T/(2*pi))**2) * mu)**(1/3)

    return semiMajorAxis


# apoapsisAltitude and periapsisAltitude in meters from surface
# return period in seconds
def apsides2Period(centralBody, apoapsisAltitude, periapsisAltitude):

    mu = centralBody.standardGravitationalParameter

    # the orbit's semi-major axis
    a = ((apoapsisAltitude+periapsisAltitude)/2) + centralBody.radius
    return 2*pi*((a**3/mu)**(1/2))

# orbitAltitude in meters
# return period in seconds
def circularOrbitAltitude2Period(centralBody, orbitAltitude):

    return apsides2Period(centralBody, orbitAltitude, orbitAltitude)


def compute(centralBody):

    # apoapsis = float(input('apoapsis (m) : '))
    # periapsis = float(input('periapsis (m) : '))
    # M = float(input('attractor mass (kg) : '))

    apoapsisAlt = 80000
    periapsisAlt = 80000

    T = apsides2Period(
        centralBody, apoapsisAlt, periapsisAlt)
    a = round(period2semiMajorAxis(centralBody, T))
    periapsis = a + centralBody.radius
    apoapsis = a + centralBody.radius

    print()
    print(T/60, 'm')

    print('periapsis = apoapsis =', thousandSeparated(a))

    targetPeriods = [T]

    targetPeriods.append(T*5/4)
    targetPeriods.append(T*6/4)
    targetPeriods.append(T*3/4)
    targetPeriods.append(T*6/5)

    print()
    for i in range(1, len(targetPeriods)):
        target_a = period2semiMajorAxis(
            centralBody, targetPeriods[i])

        targetPeriapsis = round(target_a*2) - apoapsis - centralBody.radius
        print("target periapsis "+str(i)+" : " +
              thousandSeparated(targetPeriapsis))

    print()


# return stationary orbit altitude in meters
def stationaryAltitude(centralBody) -> float:
    """
    Compute stationary orbit altitude around given body

    Args:
        centralBody: The orbited body.

    Returns:
        float: stationary orbit altitude in meters
    """
    return (period2semiMajorAxis(centralBody, centralBody.rotationPeriod) - centralBody.radius)



# compute the minimum electricty storage required for a vessel in orbit to not run out when sun is hidden by the orbitting body
# electricConsumption, the sum of consumtion from devices on the vessel
# returns electricty storage quantity 
def electricityStorage(centralBody, apoapsis, periapsis, electricConsumption):

    a = semiMajorAxis(centralBody, apoapsis, periapsis)
    alpha = math.asin( centralBody.radius / a ) * 2

    # print(alpha*180/math.pi)

    orbitPeriod = circularOrbitAltitude2Period(centralBody, a-centralBody.radius)

    darknessTime = orbitPeriod * alpha / (2 * math.pi)
    return darknessTime * electricConsumption


# print(inclinationChangeDeltaV(KspBody.bodies['mun'], 14000, 14000, 90))
# print(inclinationChangeDeltaV(KspBody.bodies['minmus'], 10000, 10000, 90))

# print(thousandSeparated(stationaryAltitude(KspBody.bodies['minmus'])))