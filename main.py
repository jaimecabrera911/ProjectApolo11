import json
import random
from datetime import datetime
from typing import List

from src.data.data import get_data
from src.models.mission import Mission
from src.models.report import Report


def main():
    missions: List[Mission] = get_data()
    missions_data = []
    for mission in missions:
        for device in mission.devices:
            state_random = random.randint(0, len(device.states) - 1)

            missions_data.append(
                Report(datetime.now(), mission.name[0], device.name, device.states[state_random].name))

    for data in missions_data:
        print(data.__dict__)

    '''data_json = json.dumps(missions_data.__str__(), indent=2)
    with open('mission1.json', 'w') as archivo:
        archivo.write(data_json)'''


if __name__ == '__main__':
    main()
