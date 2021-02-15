# Import socket module 
import socket 
FORMAT = 'utf-8'
import pandas as pd

def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server
    
    
    while True:
        # with open(r'.\fixmessages.csv', 'r') as f:
        #     for line in f:
        #         if line == ',0':
        #             continue
        #         print('sending to server', line[3:].encode(FORMAT).decode(FORMAT))
        #         s.send(line[2:].encode(FORMAT))
        #         data = s.recv(4068)
        #         print('Received from the server :',str(data.decode(FORMAT))) 
        #     f.close()
        # df = pd.read_csv(r"C:\Users\JerrinJohnJoseph\Desktop\fixmessages.csv")
        #print(df.head)
        # for (columnName, columnData) in df.iteritems(): 
        #     print('Colunm Name : ', columnName) 
        #     print('Column Contents : ', columnData.values)
        #     for i in columnData.values:
        #         print(i, i.encode(FORMAT).decode(FORMAT))
        # for i in df:
        #     print('sending to the server', i.encode(FORMAT).decode(FORMAT))
            # s.send(i.encode(FORMAT))
            # data = s.recv(4068)
            # print('Received from the server :',str(data.decode(FORMAT))) 
        fileHandle = open(r'.\req.txt')   
        for line in fileHandle:
            print('sending to the server', line[:-2].encode(FORMAT).decode(FORMAT))
            s.send(line[:-1].encode(FORMAT)) 
            data = s.recv(4068) 
  
            print('Received from the server :',str(data.decode(FORMAT))) 
            #populate 11= 'x' based on server
            # log this and analyze 
        fileHandle.close()

        # s.send(msg)

  
        # ask the client whether he wants to continue 
        # ans = input('\nDo you want to continue(y/n) :') 
        # if ans == 'y': 
        #     continue
        # else: 
        #     break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 