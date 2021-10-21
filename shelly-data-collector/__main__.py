from os import path
import urllib.request
import json
import pprint
import time
import csv

RECORD_INTERVAL = 'SEC'  # MIN / SEC

pp = pprint.PrettyPrinter(indent=4)

with open('localConfig.json') as configFile:
    config = json.load(configFile)

pp.pprint(config['ips'])

with open(path.join('data', 'data.csv'), 'w', newline='') as dataOutputFile:
    csvWriter = csv.writer(dataOutputFile, delimiter=',')
    csvWriter.writerow(['timestamp']+config['ips'])
    while True:
        timeBefore = time.time()

        powers = {}
        for i in range(len(config['ips'])):
            ip = config['ips'][i]
            rawContent = urllib.request.urlopen('http://'+ip+'/meter/0').read()

            meter = json.loads(rawContent)

            if meter['timestamp'] not in powers:
                powers[meter['timestamp']] = {}

            powers[meter['timestamp']][ip] = meter['power']
            pp.pprint(meter)

        # powers.sort(key=lambda m: m['timestamp'])
        print()
        pp.pprint(powers)
        # print(powers)
        # print(sorted(powers))

        for timestamp in sorted(powers):
            row = [timestamp]
            for ip in config['ips']:
                if ip in powers[timestamp]:
                    row.append(powers[timestamp][ip])
                else:
                    row.append('')

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
