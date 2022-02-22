# rho_w : vapor density [kg/m3]
# rho_ws : vapor density at saturation at actual dry bulb temperature [kg/m3]

# relative humidty (RH)
# fi = rho_w / rho_ws

from asyncore import read
from math import ceil, floor

currentTemp = 19.9

tmpRH = 62
tmpTemp = 21.2

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


def getMaxMoistureContent(temp):
    ti = maximumMoistureContentKnown[0][0]
    i = 0
    while ti <= temp:
        i += 1
        ti = maximumMoistureContentKnown[i][0]

    tempLow = maximumMoistureContentKnown[i-1][0]
    maxMoistureLow = maximumMoistureContentKnown[i-1][1]
    tempHi = ti
    maxMoistureHigh = maximumMoistureContentKnown[i][1]

    # print(tempLow, maxMoistureLow, '-', tempHi, maxMoistureHigh, end='')

    return (temp-tempLow)/(tempHi-tempLow)*(maxMoistureHigh-maxMoistureLow)+maxMoistureLow

# for tTest in range(5*10,10*10+1):
#     print(tTest/10,'- ', end = '')
#     maxMoistContent = getMaxMoistureContent(tTest/10)
#     print(' : ', maxMoistContent)

tempBeforeOpening = currentTemp
maxMoisture_tempBeforeOpening = getMaxMoistureContent(tempBeforeOpening)

print()

tempConfidenceInterval = 2*0.0
rhConfidenceInterval = 5*0.0
for temp_times_ten in range(floor((tmpTemp-tempConfidenceInterval)*10), ceil((tmpTemp+tempConfidenceInterval)*10)+1):
    temp = temp_times_ten/10
    for rh_times_hundred in range(floor(tmpRH-rhConfidenceInterval), ceil(tmpRH+rhConfidenceInterval)+1):

        rh = rh_times_hundred/100
        moisture = rh * getMaxMoistureContent(temp)

        rh_whenReturning_tempBeforeOpening = moisture / maxMoisture_tempBeforeOpening

        rh_whenReturning_tempBeforeOpening_times_hundred = round(rh_whenReturning_tempBeforeOpening*100)

        if rh_whenReturning_tempBeforeOpening_times_hundred <= 50:
            print(rh_times_hundred,'%,',temp,'C - ',rh_whenReturning_tempBeforeOpening_times_hundred,'% at',currentTemp,'C')


print()
print('temperature before opening windows :', tempBeforeOpening)
print()
print('currentRH :', tmpRH)
print('currentTemp :', tmpTemp)
print()
print('target temps for 50% RH when returning at',tempBeforeOpening,':',)
# print()
# print()
# print('RH at',targetTemp,':',rh_whenReturningTargetTemp_times_hundred)
