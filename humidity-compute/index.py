# rho_w : vapor density [kg/m3]
# rho_ws : vapor density at saturation at actual dry bulb temperature [kg/m3]

# relative humidty (RH)
# fi = rho_w / rho_ws

from asyncore import read

currentRH_times_hundred = 72
currentTemp = 20.7

tmpRH = 71
tmpTemp = 18

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

currentRH = currentRH_times_hundred/100

maxMoisture_CurrentTemp = getMaxMoistureContent(currentTemp)

for temp_times_ten in range(tmpTemp*10-5, tmpTemp*10+5):
    temp = temp_times_ten/10
    for rh_times_hundred in range(tmpRH-5, tmpRH+5):

        rh = rh_times_hundred/100
        moisture = rh * getMaxMoistureContent(temp)

        rh_whenReturningCurrentTemp = moisture / maxMoisture_CurrentTemp

        rh_whenReturningCurrentTemp_times_hundred = round(rh_whenReturningCurrentTemp*100)

        if rh_whenReturningCurrentTemp_times_hundred <= 50:
            print(rh_times_hundred,'%,',temp,'C - ',rh_whenReturningCurrentTemp_times_hundred,'% at',currentTemp,'C')


print('currentRH :', currentRH_times_hundred)
print('currentTemp :', currentTemp)
