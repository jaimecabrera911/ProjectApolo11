import random
from datetime import datetime


class Project:
    def __init__(self, mission, device_type):
        self.mission = mission
        self.device_type = device_type
        self.date = datetime.now().strftime("%d%m%y%H%M%S")
        self.device_state = random.choice(self.get_device_states())

    @staticmethod
    def get_device_states():
        return ["excelente", "bueno", "advertencia", "defectuoso", "inoperable", "desconocido"]

    @staticmethod
    def get_missions():
        return ["ORBONE","CLNM","TMRS","GALXON","GALXON"]

    def generate_file_content(self):
        file_content = f"Fecha: {self.date}\n"
        file_content += f"Misión: {self.mission}\n"
        file_content += f"Tipo de dispositivo: {self.device_type}\n"
        file_content += f"Estado del dispositivo: {self.device_state}\n"
        file_content += f"Hash: {self.__hash__()}\n"
        return file_content

    def __hash__(self) -> int:
        return hash((self.mission,self.device_type,self.date,self.device_state))



