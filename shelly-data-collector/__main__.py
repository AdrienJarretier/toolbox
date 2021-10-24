from os import path
import urllib.request
import json
import pprint
import time
import csv

from parseConfig import loadConfig

config = loadConfig()

RECORD_INTERVAL = 'SEC'  # MIN / SEC

POWERS_FIFO_SIZE = config['dataCollectionSettings']['POWERS_FIFO_SIZE']

DATA_COLLECTION_TOTAL_TIME_SEC = config['dataCollectionSettings']['COLLECTION_TOTAL_TIME_SEC']


def periodUnitTime(struct_time=None):
    if struct_time == None:
        struct_time = time.localtime()

    return int(struct_time.tm_sec/5)


powers = {}


def dataCollection(dataFileName):

    timeDataCollectStart = time.localtime()
    unitTimeDataCollectStart = periodUnitTime(timeDataCollectStart)
    with open(path.join('data', dataFileName), 'w', newline='') as dataOutputFile:
        csvWriter = csv.writer(dataOutputFile, delimiter=',')
        csvWriter.writerow(['timestamp']+config['ips'])

        # while time.localtime().tm_min == timeDataCollectStart.tm_min:
        while periodUnitTime() == unitTimeDataCollectStart:

            timeBefore = time.time()

            for i in range(len(config['ips'])):
                ip = config['ips'][i]
                rawContent = urllib.request.urlopen(
                    'http://'+ip+'/meter/0').read()

                meter = json.loads(rawContent)

                if meter['timestamp'] not in powers:
                    powers[meter['timestamp']] = {}

                powers[meter['timestamp']][ip] = meter['power']
                # pp.pprint(meter)

            # powers.sort(key=lambda m: m['timestamp'])
            # print()
            # pp.pprint(powers)
            # print(powers)

            powersTimestamps = sorted(powers)
            print(powersTimestamps)

            if len(powersTimestamps) >= POWERS_FIFO_SIZE:

                while len(powersTimestamps) >= POWERS_FIFO_SIZE:

                    oldestTimestamp = powersTimestamps[0]

                    row = [oldestTimestamp]
                    for ip in config['ips']:
                        if ip in powers[oldestTimestamp]:
                            row.append(powers[oldestTimestamp][ip])
                        else:
                            row.append('')

                    del powers[oldestTimestamp]
                    del powersTimestamps[0]

                    print(row)
                    csvWriter.writerow(row)

                dataOutputFile.flush()

            timeEnd = time.time()
            elapsedTime = timeEnd-timeBefore
            if RECORD_INTERVAL == 'MIN':
                time.sleep(60-(meter['timestamp'] % 60)+1)
            elif RECORD_INTERVAL == 'SEC':
                time.sleep(max(0, 1-elapsedTime))
            else:
                raise 'wrong RECORD_INTERVAL value'


pp = pprint.PrettyPrinter(indent=4)

pp.pprint(config['ips'])

scriptTimeStart = time.time()

while time.time() - scriptTimeStart < DATA_COLLECTION_TOTAL_TIME_SEC:
    dataCollection('data-'+time.strftime('%Y-%m-%d_%H-%M-%S')+'.csv')
