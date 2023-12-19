from datetime import datetime


class Report:
    def __init__(self, date: datetime, mission: str, device: str, state: str):
        self.date = date
        self.mission = mission
        self.device = device
        self.state = state
        self.hash = self.__hash__()

    def __hash__(self) -> int:
        return hash((self.date, self.mission, self.device, self.state))
