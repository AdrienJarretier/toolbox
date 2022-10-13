# rho_w : vapor density [kg/m3]
# rho_ws : vapor density at saturation at actual dry bulb temperature [kg/m3]

# relative humidty (RH)
# fi = rho_w / rho_ws

from asyncore import read
from math import ceil, floor

currentRH = 78
currentTemp = 25



TARGET_RH_TIMES_HUNDRED = 50

tmpRH = 73
tmpTemp = 19.1

# currentRH_times_hundred = int(input("current RH : "))
# currentTemp = float(input("current temp : "))

# The maximum moisture content possible in air - at saturation -
# varies with temperature (10-3 kg/m3)
maximumMoistureContentKnown = [
    [0, 4.89],
    [5, 6.82],
    [10, 9.39],
    [15, 12.8],
    [20, 17.3],
    [30, 30.4],
    [40, 51.1]
]


def interpolate(fixedIndex, fixedValue):
    ti = maximumMoistureContentKnown[0][fixedIndex]
    i = 0
    while ti <= fixedValue:
        i += 1
        ti = maximumMoistureContentKnown[i][fixedIndex]

    tempLow = maximumMoistureContentKnown[i-1][fixedIndex]
    maxMoistureLow = maximumMoistureContentKnown[i-1][1-fixedIndex]
    tempHi = ti
    maxMoistureHigh = maximumMoistureContentKnown[i][1-fixedIndex]

    return (fixedValue-tempLow)/(tempHi-tempLow)*(maxMoistureHigh-maxMoistureLow)+maxMoistureLow


def getMaxMoistureContent(temp):
    return interpolate(0, temp)


def getTempForGivenMaxMoisture(maxMoistureContent):
    return interpolate(1, maxMoistureContent)

# Given a high temperature before opening windows,
# and admiting a given constant RH
# Computes the max temperature at which the air needs to go down
# to get the given target RH when temp goes back up
# assuming the abs moisture will stay constant after having closed the windows


def computeLowTempTarget(highTempBeforeOpening, RHBeforeOpening_timesHundred, targetRH_timesHundred=50):

    targetRh = targetRH_timesHundred / 100
    RHBeforeOpening = RHBeforeOpening_timesHundred / 100

    targetMoisture = getMaxMoistureContent(highTempBeforeOpening) * targetRh

    targetMaxMoisture = targetMoisture / RHBeforeOpening

    return getTempForGivenMaxMoisture(targetMaxMoisture)


tempBeforeOpening = currentTemp
rhBeforeOpening = currentRH

maxMoisture_tempBeforeOpening = getMaxMoistureContent(tempBeforeOpening)

# print()

# tempConfidenceInterval = 2*0.0
# rhConfidenceInterval = 5*0.0
# for temp_times_ten in range(floor((tmpTemp-tempConfidenceInterval)*10), ceil((tmpTemp+tempConfidenceInterval)*10)+1):
#     temp = temp_times_ten/10
#     for rh_times_hundred in range(floor(tmpRH-rhConfidenceInterval), ceil(tmpRH+rhConfidenceInterval)+1):

rh = tmpRH/100
moisture = rh * getMaxMoistureContent(tmpTemp)

rh_whenReturning_tempBeforeOpening = moisture / maxMoisture_tempBeforeOpening

rh_whenReturning_tempBeforeOpening_times_hundred = round(
    rh_whenReturning_tempBeforeOpening*100)

#         if rh_whenReturning_tempBeforeOpening_times_hundred <= 50:
#             print(rh_times_hundred, '%,', temp, 'C - ',
#                   rh_whenReturning_tempBeforeOpening_times_hundred, '% at', currentTemp, 'C')



print()
print('temperature before opening windows :', tempBeforeOpening)
print()
print('currentRH :', tmpRH)
print('currentTemp :', tmpTemp)
print()
print('target temp with', rhBeforeOpening, '% RH for '+str(TARGET_RH_TIMES_HUNDRED)+'% RH when returning at', tempBeforeOpening, ':',
      ceil(computeLowTempTarget(tempBeforeOpening, rhBeforeOpening, TARGET_RH_TIMES_HUNDRED)*10)/10)
print()
print('RH at', tempBeforeOpening, ':',
      rh_whenReturning_tempBeforeOpening_times_hundred)
print()
print('target temp with', tmpRH, '% RH for '+str(TARGET_RH_TIMES_HUNDRED)+'% RH when returning at', tempBeforeOpening, ':',
      ceil(computeLowTempTarget(tempBeforeOpening, tmpRH, TARGET_RH_TIMES_HUNDRED)*10)/10)
