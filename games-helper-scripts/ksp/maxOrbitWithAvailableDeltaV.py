from KspBody import KspBody



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
