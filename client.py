import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.50.17"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

fileHandle = open(r"C:\Users\JulianSaraJoseph\Downloads\messages.txt", 'r')

for line in fileHandle:
    fields = line.split('\n')
    print(len(fields), 'length')
    for i in range(len(fields)):
        send(fields[i])
        #print(fields) # prints the first fields value

fileHandle.close()

# input()
# send("Hello Everyone!")
# input()
# send("Hello Tim!")

send(DISCONNECT_MESSAGE)