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


print(orbitalSpeed(KspBody.bodies['kerbin'], 80000,80000))