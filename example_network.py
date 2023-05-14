from src.network import Network

class GameNetwork(Network):
    def __init__(self, server: str, port: int) -> None:
        super().__init__(server, port)
        self.pos = self.connect()

    def getPos(self) -> str:
        return self.pos
