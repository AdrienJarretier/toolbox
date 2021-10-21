import urllib.request
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('localConfig.json') as configFile:
    config = json.load(configFile)

pp.pprint(config['ips'])

for ip in config['ips']:
    rawContent = urllib.request.urlopen('http://'+ip+'/meter/0').read()

    meter = json.loads(rawContent)

    pp.pprint(meter)
