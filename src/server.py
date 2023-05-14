'''
Server
'''

import socket
from _thread import start_new_thread

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

pos = [(0,0), (100,100)]

def parse_pos(string: str) -> tuple[int, int]:
    pos = string.split(",")
    return int(pos[0]), int(pos[1])

def stringify_pos(pos:  tuple[int, int]) -> str:
    return f"{pos[0]},{pos[1]}"

def threaded_client(conn: socket.socket, player: int) -> None:
    '''
    Client-instance listener
    '''

    conn.send(str.encode(stringify_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            pos[player] = parse_pos(data)

            if not data:
                print("Disconnected")
                break

            print("Received: ", data)
            print("Sending : ", reply)
            if player == 1:
                reply = pos[0]
            else:
                reply = pos[1]

            conn.sendall(str.encode(stringify_pos(reply)))
        except ValueError:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
