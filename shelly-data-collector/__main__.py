from os import path
import urllib.request
import json
import pprint
import time
import csv


def dataCollection(dataFileName):

    timeDataCollectStart = time.localtime()
    with open(path.join('data', dataFileName), 'w', newline='') as dataOutputFile:
        csvWriter = csv.writer(dataOutputFile, delimiter=',')
        csvWriter.writerow(['timestamp']+config['ips'])

        powers = {}
        while time.localtime().tm_min == timeDataCollectStart.tm_min:

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

            timestamps = sorted(powers)
            print(timestamps)

            if len(timestamps) >= WRITE_TO_FILE_INTERVAL_S:

                while len(timestamps) >= WRITE_TO_FILE_INTERVAL_S:

                    oldestTimestamp = timestamps[0]

                    row = [oldestTimestamp]
                    for ip in config['ips']:
                        if ip in powers[oldestTimestamp]:
                            row.append(powers[oldestTimestamp][ip])
                        else:
                            row.append('')

                    del powers[oldestTimestamp]
                    del timestamps[0]

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


RECORD_INTERVAL = 'SEC'  # MIN / SEC

WRITE_TO_FILE_INTERVAL_S = 4

# FILE_ROTATION_PERIOD = 'DAY'

pp = pprint.PrettyPrinter(indent=4)

with open('localConfig.json') as configFile:
    config = json.load(configFile)

pp.pprint(config['ips'])

dataCollection('data-'+time.strftime('%Y-%m-%d_%H-%M-%S')+'.csv')
