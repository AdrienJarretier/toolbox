from time import sleep
import zipfile
import xml.etree.ElementTree as ET
from math import radians, cos, sin, asin, sqrt

from parseInputs import getInputs
from downloadData import downloadIfLocalTooOld


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    r = 6371
    return c * r


baseFileName = 'PrixCarburants_instantane'

path_to_zip_file = baseFileName+'.zip'

print()
newDataDownloaded = downloadIfLocalTooOld(path_to_zip_file)
print("-------- Data downloaded.")

sleep(2)

if newDataDownloaded:
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall()

xmlFile = baseFileName+'.xml'

tree = ET.parse(xmlFile)
root = tree.getroot()

INPUTS = getInputs()

AVERAGE_SPEED = INPUTS["vitesse_moyenne_kmh"]
FUEL_CAPACITY = INPUTS["capacite_reservoir_litres"]  # L
FUEL_CONSUMPTION = INPUTS["consommation_moyenne_l/100km"]/100  # L/KM
ORIGIN_LOCATION = INPUTS["coordonnees_origines"][0]
FUELS_SOLD = INPUTS["carburants_requis"]


def parseXmlPdv(xmlPdv):

    address = xmlPdv.find('adresse').text
    city = xmlPdv.find('ville').text
    cp = xmlPdv.attrib['cp']
    lat = float(xmlPdv.attrib['latitude'])/100000
    lon = float(xmlPdv.attrib['longitude'])/100000
    horaires = xmlPdv.find('horaires')
    has24Auto = horaires is not None and horaires.attrib['automate-24-24'] == '1'

    return {
        'address': address,
        'city': city,
        'cp': cp,
        'lat': lat,
        'lon': lon,
        'prices': child.iter('prix'),
        'horaires': horaires,
        'has24Auto': has24Auto
    }


class PointDeVente:

    def __init__(self, address, city, cp, lat, lon, priceDic) -> None:
        self.address = address
        self.city = city
        self.cp = cp
        self.lat = lat
        self.lon = lon
        self.priceDic = priceDic
        self.priceDic['valeur'] = float(self.priceDic['valeur'])

        self.distance = self.distanceFrom(
            ORIGIN_LOCATION[0], ORIGIN_LOCATION[1])  # km

        self.consumedFuelToGo = FUEL_CONSUMPTION*self.distance

        self.fullTankPrice = self.consumedFuelToGo*2 * \
            self.priceDic['valeur']+(FUEL_CAPACITY/2)*self.priceDic['valeur']

    def distanceFrom(self, lat, lon):
        return haversine(self.lon, self.lat, lon, lat)

    def print(self):
        print()
        print(self.address)
        print(self.city, self.cp)
        print(self.lat, ',', self.lon)
        print('\t', self.priceDic)

    def __str__(self):
        return self.address + '\n' + self.city + ', ' + self.cp + '\n' + str(self.lat) + ',' + str(self.lon) + '\n' + '\t' + str(self.priceDic)


pdvs = []


for child in root:

    parsed = parseXmlPdv(child)

    for prix in parsed['prices']:

        if prix.attrib['nom'].lower() in FUELS_SOLD:
            priceDic = prix.attrib
            pdv = PointDeVente(parsed['address'], parsed['city'],
                               parsed['cp'], parsed['lat'], parsed['lon'], priceDic)
            try:
                consumedFuel = pdv.distance * FUEL_CONSUMPTION
                # if parsed['has24Auto'] and consumedFuel*3 < FUEL_CAPACITY/2:
                if consumedFuel*3 < FUEL_CAPACITY/2:
                    pdvs.append(pdv)

            except AttributeError as e:
                print()
                print('--------- AttributeError ---------')
                pdv.print()
                exit()


pdvs.sort(key=lambda pdv: -pdv.fullTankPrice)


def hourToPretty(timeInHour):

    return str(int(timeInHour)) + ' h ' + str(int(timeInHour*60) % 60)


for pdv in pdvs:

    speed = AVERAGE_SPEED  # km / h
    time = pdv.distance/speed

    print('----------------------------------------------------------------------')
    print(pdv)
    print("distance : ", pdv.distance)

    print("temps aller-retour : ", hourToPretty(time*2))

    print('prix plein : ', pdv.fullTankPrice)
