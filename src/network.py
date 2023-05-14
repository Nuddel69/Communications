import socket

class Network():
    def __init__(self, server: str, port: int) -> None:
        '''
        Initiates a network-client instance
        '''

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.id = self.connect()

    def connect(self) -> str:
        '''
        Connects the client to a server

        returns:
            - Connection status
        '''

        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode("utf-8")
        except:
            return "Connection failed"

    def send(self, data: str) -> str:
        '''
        Sends an encoded string
        
        Returns:
            - Either echoes the sent message, or prints an error
        '''

        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode("utf-8")
        except socket.error as e:
            print(e)
            return "Error."

if __name__ == "__main__":
    print(Network("127.0.0.1", 5555).send("Hello World!"))
