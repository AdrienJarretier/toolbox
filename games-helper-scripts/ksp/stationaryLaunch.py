
from orbitalPeriod import *


# orbit_1_altitude in meters
# return time to wait before executing transfer in seconds
def tranferTimeOffset(centralBody, orbit_1_altitude):

    angularSpeedCentralBody = 360/centralBody.rotationPeriod

    orbit_1_period = circularOrbitAltitude2Period(
        centralBody, orbit_1_altitude)
    angularSpeedOrbit_1 = 360/orbit_1_period

    m = 360/(angularSpeedOrbit_1-angularSpeedCentralBody)

    orbitalPeriod_2 = apsides2Period(
        centralBody, stationaryAltitude(centralBody), orbit_1_altitude)

    siderealPeriod_1 = 360/(angularSpeedOrbit_1-angularSpeedCentralBody)

    # print("-----------------")
    # print("siderealPeriod_1 : ", siderealPeriod_1)
    # print("angularSpeedOrbit_1 : ", angularSpeedOrbit_1)
    # print("angularSpeedCentralBody : ", angularSpeedCentralBody)
    # print("orbitalPeriod_2 : ", orbitalPeriod_2)
    # print("-----------------")

    teta = (180-(angularSpeedCentralBody * orbitalPeriod_2/2))

    timeOffset = -teta / (angularSpeedOrbit_1 - angularSpeedCentralBody) + siderealPeriod_1

    # print("timeOffset :", timeOffset)

    return timeOffset


def transferTime(centralBody, orbit_1_altitude, startTime):

    offsetTime = tranferTimeOffset(centralBody, orbit_1_altitude)

    return sec2prettyTime(startTime+offsetTime)


apoapsis = 82696
periapsis = 77517

avgAlt = (apoapsis+periapsis)/2

# print("avgAlt :", avgAlt)
print("############################################")
print("## start transfer at t +", transferTime(KspBody.bodies["kerbin"], avgAlt, time2sec(0, 58, 26)))
print("## stationary altitude : ", thousandSeparated(
    stationaryAltitude(KspBody.bodies["kerbin"])))
print("############################################")
