
from src.models.device import Device
from src.models.mission import Mission
from src.enums.mission_name import MissionName
from src.models.state import State


def main():
    device = Device(1, "Satelite", State.FAIL)
    mission = Mission(MissionName.GALXONE, device)

    '''print(mission.__dict__)
    print(mission.device.__dict__)
    print(mission.device.state.value)
    print(mission.__hash__())'''

    formatted_date = mission.date.strftime("%d%m%Y%H%M%S")

    data = {
        "date": formatted_date.format(mission.date),
        "mission": mission.missionName.name,
        "device": mission.device.name,
        "state": mission.device.state.name
    }

    print(data)


if __name__ == '__main__':
    main()
