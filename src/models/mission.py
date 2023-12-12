import datetime

from datetime import datetime

from src.enums.mission_name import MissionName
from src.models.device import Device


class Mission:

    def __init__(self, missionName: MissionName, device: Device) -> None:
        self.missionName = missionName
        self.date = datetime.now()
        self.device = device

    def __hash__(self) -> int:
        return hash((self.date, self.missionName, self.device.name))
