import yaml
from models.models import Sensor

def load():
    confs = yaml.load(open('configs/1.yaml','r'), Loader=yaml.Loader)
    return [ Sensor(c) for c in confs['sensors'] ]
 