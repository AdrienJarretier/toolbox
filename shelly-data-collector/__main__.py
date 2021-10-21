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

        powers = []
        for ip in config['ips']:
            rawContent = urllib.request.urlopen('http://'+ip+'/meter/0').read()

            meter = json.loads(rawContent)

            powers.append({
                'ip': ip,
                'power': meter['power'],
                'timestamp': meter['timestamp']
            })

        pp.pprint(powers)

        timeEnd = time.time()
        elapsedTime = timeEnd-timeBefore
        if RECORD_INTERVAL == 'MIN':
            time.sleep(60-(meter['timestamp'] % 60)+1)
        elif RECORD_INTERVAL == 'SEC':
            time.sleep(max(0, 1-elapsedTime))
        else:
            raise 'wrong RECORD_INTERVAL value'
