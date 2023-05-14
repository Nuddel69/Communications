import socket

class Network():
    def __init__(self, server: str, port: int) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self) -> str:
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode("utf-8")
        except:
            return "Connection failed"

    def send(self, data: str) -> str:
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(e)
            return "Error."

n = Network("127.0.0.1", 5555)

print(n.send("Hello World!"))
