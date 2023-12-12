from src.models.state import State


class Device:

    def __init__(self, code: int, name: str, state: State) -> None:
        self.code = code
        self.name = name
        self.state = state
