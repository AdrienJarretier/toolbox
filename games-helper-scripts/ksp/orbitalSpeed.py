import KspBody

# apoapsisAltitude, periapsisAltitude  in meters from surface
# return semi major axis, the mean from max radius and min raidus from the center of the body


# def semiMajorAxis(centralBody, apoapsisAltitude, periapsisAltitude):

#     return ((apoapsisAltitude+periapsisAltitude)/2) + centralBody.radius


def orbitalSpeed(centralBody: KspBody.KspBody, apoapsisAltitude: float, periapsisAltitude: float, currentAltitude: float = None) -> float:
    """
    Compute orbital speed at a given altitude on the given orbit around the given body

    Args:
        centralBody: The orbited body.
        apoapsisAltitude, periapsisAltitude : altitudes in meters
        currentAltitude: OPTIONAL, in meters from surface, if ommited, compute speed from an assumed circular orbit at an average altitude

    Returns:
        float: orbital speed in m/s at the current altitude
    """

    return KspBody.orbitalSpeed(centralBody.radius, centralBody.standardGravitationalParameter, apoapsisAltitude, periapsisAltitude, currentAltitude)


# print(orbitalSpeed(KspBody.bodies['kerbin'], 80000,80000))
