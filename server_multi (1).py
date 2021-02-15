# import socket programming library 
import socket 
  
# import thread module 
from _thread import *
import threading 
  
print_lock = threading.Lock() 
FORMAT = 'ascii'

# thread function 
newDict = {}
X = 0
with open(r'.\response.txt', 'r') as f:
    for line in f:
        newDict[X] = line
        X += 1
def threaded(c): 
    count = 0
    while True: 
  
        # data received from client 
        data = c.recv(4056)
        count += 1
        if not data: 
            print('Bye') 
              
            # lock released on exit 
            print_lock.release() 
            break
        
 
        print(count, '-----number')
            
        if data:
            if count-1 < X:
                print('received from client', count, newDict[count-1])
                print('sending to the client', newDict[count-1].encode(FORMAT).decode(FORMAT))
                c.send(newDict[count-1].encode(FORMAT))
  
    # connection closed 
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 