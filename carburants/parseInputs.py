import json


def getInputs():

    for _ in range(2):
        try:
            with open('inputs.json') as inputsFile:
                inputs = json.load(inputsFile)
                return inputs
        except FileNotFoundError:
            with open('inputs_template.json') as templateFile:
                with open('inputs.json', 'w') as inputsFile:
                    inputsFile.write(templateFile.read())
