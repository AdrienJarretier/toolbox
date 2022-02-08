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
def inclinationChangeDeltaV(centralBody, apoapsisAltitude, periapsisAltitude, angle):

    angle = angle * math.pi / 180

    speed = orbitalSpeed(centralBody, apoapsisAltitude, periapsisAltitude)

    dv = 2*speed*math.sin(angle/2)

    return dv


# altitudes in meters
# returns deltaV in meters / second including a 10 % margin
def getDeltavFromInitialOrbitToTarget(centralBody, initialAltitude, targetAltitude, inclinationChange):

    # return orbitalSpeed(centralBody, 0, 0)+transferDeltaV(centralBody, 0, 0, apopasis, periapsis)

    return (transferDeltaV(centralBody, initialAltitude, initialAltitude, targetAltitude, targetAltitude) \
        + inclinationChangeDeltaV(centralBody,
                                  max(initialAltitude, targetAltitude), max(initialAltitude, targetAltitude), inclinationChange)) * 1.1


print(getDeltavFromInitialOrbitToTarget(
    KspBody.bodies['mun'], KspBody.bodies['mun'].soi, 100e3, 90))


print(getDeltavFromInitialOrbitToTarget(
    KspBody.bodies['kerbin'], 74000, 500e3, 0))
