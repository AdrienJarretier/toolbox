from KspBody import KspBody

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


def reverseDeltaV(centralBody, currentAltitude, deltaV):
    currentSpeed = orbitalSpeed(centralBody, currentAltitude, currentAltitude)

    deltav = abs(finalSpeed-halfTransferApoapsisSpeed)+abs(halfTransferPeriapsisSpeed - currentSpeed)

    return currentSpeed

print(reverseDeltaV(KspBody.bodies['kerbin'], 74000, 870))
