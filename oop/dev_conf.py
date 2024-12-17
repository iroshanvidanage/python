# example: functions vs classes

import json

# Class-based:

class Configuration(dict):
    def __init__(self, source):
        self.source = source
    
    def fetch(self):
        with open(self.source, 'r') as source:
            self.update(json.loads(source.read()))


conf = Configuration('dev_conf.json')
conf.fetch()
print(f'Class-based: {conf}')


# Function-based:

def configuration_from(source):
    with open(source, 'r') as f:
        return json.loads(f.read())


print(f'Function-based: {configuration_from('dev_conf.json')}')
