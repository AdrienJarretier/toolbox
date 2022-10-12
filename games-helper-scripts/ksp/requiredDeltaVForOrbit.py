from KspBody import KspBody
from orbitalSpeed import orbitalSpeed
from utils import *
import math



# altitudes in meters
# returns deltaV in meters / second
def transferDeltaV(centralBody, origApoapsis, origPeriapsis, targetApoapsis, targetPeriapsis):

    origSpeed = orbitalSpeed(centralBody, origApoapsis,
                             origPeriapsis, origPeriapsis)
    halfTransferPeriapsisSpeed = orbitalSpeed(
        centralBody, targetApoapsis, origPeriapsis, origPeriapsis)

    halfTransferApoapsisSpeed = orbitalSpeed(
        centralBody, targetApoapsis, origPeriapsis, targetApoapsis)
    finalSpeed = orbitalSpeed(
        centralBody, targetApoapsis, targetPeriapsis, targetApoapsis)

    return abs(finalSpeed-halfTransferApoapsisSpeed)+abs(halfTransferPeriapsisSpeed - origSpeed)


# altitudes in meters
# angle in degrees
# returns deltaV in meters / second
def inclinationChangeDeltaV(centralBody: KspBody, apoapsisAltitude: float, periapsisAltitude: float, angle: float) -> float:
    """
    Compute Delta V required to change inclination of an orbit

    Args:
        centralBody: The orbited body.
        apoapsisAltitude, periapsisAltitude : altitudes in meters
        angle : in degrees

    Returns:
        float: deltaV in meters / second
    """

    angle = angle * math.pi / 180

    speed = orbitalSpeed(centralBody, apoapsisAltitude, periapsisAltitude)

    dv = 2*speed*math.sin(angle/2)

    return dv


# altitudes in meters
# returns deltaV in meters / second including a 10 % margin
def getDeltavFromInitialOrbitToTarget(centralBody: KspBody, initialAltitude: float, targetAltitude: float, inclinationChange: float) -> float:
    """
    Compute Delta V required to go from one initial orbit altitude to another (assuming circular)

    Args:
        centralBody: The orbited body.
        initialAltitude, targetAltitude : altitudes in meters
        inclinationChange : in degrees

    Returns:
        float: deltaV in meters / second
    """

    # return orbitalSpeed(centralBody, 0, 0)+transferDeltaV(centralBody, 0, 0, apopasis, periapsis)

    return (transferDeltaV(centralBody, initialAltitude, initialAltitude, targetAltitude, targetAltitude)
            + inclinationChangeDeltaV(centralBody,
                                      max(initialAltitude, targetAltitude), max(initialAltitude, targetAltitude), inclinationChange))


# print()

# print(getDeltavFromInitialOrbitToTarget(
#     KspBody.bodies['mun'], KspBody.bodies['mun'].soi, 100e3, 90))


# print(type(getDeltavFromInitialOrbitToTarget(
#     KspBody.bodies['kerbin'], 74000, 500e3, 0)))
