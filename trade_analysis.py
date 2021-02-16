#!/usr/bin/env python3

import matplotlib.pyplot as plt #used for plotting
import subprocess              #This is being used to concatenate the Linux grep commands
from prettytable import PrettyTable # this is used to form a nice table
from colorama import *           # this is being used for the color of the printed table

def total_orders(myFile): #Calculating the umber of the orders in the resultant file log.txt
    count = 0    
    with open(myFile) as openfile:
        for line in openfile:
            for part in line.split("|"):
                if "35=D" in part:
                    count = count + 1
    return (count)

def nasdaq_orders(file_name): #subprocess use for gretting the count of the 35=D, 39=2|1|5(cancelled and expired) for NASDAQ
    p1 = subprocess.Popen(["grep", "100=NASDAQ", file_name], stdout = subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "35=D"], stdin = p1.stdout, stdout = subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin = p2.stdout, stdout = subprocess.PIPE)
    p2.stdout.close()   
    output = p3.communicate()[0]

    #Counting total number of Filled orders for NASDAQ
    t1 = subprocess.Popen(["grep", "100=NASDAQ", file_name], stdout = subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin = t1.stdout, stdout = subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin = t2.stdout, stdout = subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin = t3.stdout, stdout = subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for NASDAQ
    x1 = subprocess.Popen(["grep", "100=NASDAQ", file_name], stdout = subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin = x1.stdout, stdout = subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin = x2.stdout, stdout = subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin = x3.stdout, stdout = subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for NASDAQ
    y1 = subprocess.Popen(["grep", "100=NASDAQ", file_name], stdout=subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin = y1.stdout, stdout = subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin = y2.stdout, stdout = subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin = y3.stdout, stdout = subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Cancelled orders for NASDAQ
    z1 = subprocess.Popen(["grep", "100=NASDAQ", file_name], stdout = subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin = z1.stdout, stdout = subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin = z2.stdout, stdout = subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin = z3.stdout, stdout = subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf-8"), output3.decode("utf-8"), output4.decode("utf-8"), output5.decode("utf-8")

def nyse_orders(file_name): #subprocess use for gretting the count of the 35=D, 39=2|1|5(cancelled and expired) for NYSE
    #Counting total number of New Orders for NYSE
    p1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE) 
    p2 = subprocess.Popen(["grep", "35=D"], stdin = p1.stdout, stdout = subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin = p2.stdout, stdout = subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]
    
    #Counting total number of Filled orders for NYSE
    t1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE) #output of T1  command would be input to the t2, output of t2 would be input to t3 and so on
    t2 = subprocess.Popen(["grep", "39=2"], stdin = t1.stdout, stdout = subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin = t2.stdout, stdout = subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin = t3.stdout, stdout = subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for NYSE
    x1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin = x1.stdout, stdout = subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin = x2.stdout, stdout = subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin = x3.stdout, stdout = subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for NYSE
    y1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin = y1.stdout, stdout = subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin = y2.stdout, stdout = subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin = y3.stdout, stdout = subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Expired orders for NYSE
    z1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin = z1.stdout, stdout = subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin = z2.stdout, stdout = subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin = z3.stdout, stdout = subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf-8"), output3.decode("utf-8"), output4.decode("utf-8"), output5.decode("utf-8")

def lse_orders(file_name): #subprocess use for gretting the count of the 35=D, 39=2|1|5(cancelled and expired) for LSE
    p1 = subprocess.Popen(["grep", "100=LSE", file_name], stdout = subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "35=D"], stdin = p1.stdout, stdout = subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin = p2.stdout, stdout = subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]

    #Counting total number of Filled orders for LSE
    t1 = subprocess.Popen(["grep", "100=LSE", file_name], stdout = subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin = t1.stdout, stdout = subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin = t2.stdout, stdout = subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin = t3.stdout, stdout = subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for LSE
    x1 = subprocess.Popen(["grep", "100=LSE", file_name], stdout = subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin = x1.stdout, stdout = subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin = x2.stdout, stdout = subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin = x3.stdout, stdout = subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for LSE
    y1 = subprocess.Popen(["grep", "100=LSE", file_name], stdout = subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin = y1.stdout, stdout = subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin = y2.stdout, stdout = subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin = y3.stdout, stdout = subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Cancelled orders for LSE
    z1 = subprocess.Popen(["grep", "100=LSE", file_name], stdout = subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin = z1.stdout, stdout = subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin = z2.stdout, stdout = subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin = z3.stdout, stdout = subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    
    return output.decode("utf-8"), output2.decode("utf-8"), output3.decode("utf-8"), output4.decode("utf-8"), output5.decode("utf-8")

def par_orders(file_name): #subprocess use for gretting the count of the 35=D, 39=2|1|5(cancelled and expired) for PAR
    p1 = subprocess.Popen(["grep", "100=PAR", file_name], stdout = subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "35=D"], stdin = p1.stdout, stdout = subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin = p2.stdout, stdout = subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]

    #Counting total number of Filled orders for PAR
    t1 = subprocess.Popen(["grep", "100=PAR", file_name], stdout = subprocess.PIPE)
    t2 = subprocess.Popen(["grep", "39=2"], stdin = t1.stdout, stdout = subprocess.PIPE)
    t1.stdout.close()
    t3 = subprocess.Popen(["grep", "150=2"], stdin = t2.stdout, stdout = subprocess.PIPE)
    t2.stdout.close()
    t4 = subprocess.Popen(["grep", "-c", "^"], stdin = t3.stdout, stdout = subprocess.PIPE)
    t3.stdout.close()
    output2 = t4.communicate()[0]
    
    #Counting total number of Partial filled orders for PAR
    x1 = subprocess.Popen(["grep", "100=PAR", file_name], stdout = subprocess.PIPE)
    x2 = subprocess.Popen(["grep", "39=1"], stdin = x1.stdout, stdout = subprocess.PIPE)
    x1.stdout.close()
    x3 = subprocess.Popen(["grep", "150=1"], stdin = x2.stdout, stdout = subprocess.PIPE)
    x2.stdout.close()
    x4 = subprocess.Popen(["grep", "-c", "^"], stdin = x3.stdout, stdout = subprocess.PIPE)
    x3.stdout.close()
    output3 = x4.communicate()[0]
    
    #Counting total number of Cancelled orders for PAR
    y1 = subprocess.Popen(["grep", "100=PAR", file_name], stdout = subprocess.PIPE)
    y2 = subprocess.Popen(["grep", "39=5"], stdin = y1.stdout, stdout = subprocess.PIPE)
    y1.stdout.close()
    y3 = subprocess.Popen(["grep", "150=5"], stdin = y2.stdout, stdout = subprocess.PIPE)
    y2.stdout.close()
    y4 = subprocess.Popen(["grep", "-c", "^"], stdin = y3.stdout, stdout = subprocess.PIPE)
    y3.stdout.close()
    output4 = y4.communicate()[0]
    
    #Counting total number of Cancelled orders for PAR
    z1 = subprocess.Popen(["grep", "100=PAR", file_name], stdout = subprocess.PIPE)
    z2 = subprocess.Popen(["grep", "39=5"], stdin = z1.stdout, stdout = subprocess.PIPE)
    z1.stdout.close()
    z3 = subprocess.Popen(["grep", "150=5"], stdin = z2.stdout, stdout = subprocess.PIPE)
    z2.stdout.close()
    z4 = subprocess.Popen(["grep", "-c", "^"], stdin = z3.stdout, stdout = subprocess.PIPE)
    z3.stdout.close()
    output5 = z4.communicate()[0]
    #UTF-8 decode is needed to convert the number o/p into a string , and later to int for our calculations in the "main" function 
    #you cant perform arithementic operations on UTF-8 code, henc, the decode
    return output.decode("utf-8"), output2.decode("utf-8"), output3.decode("utf-8"), output4.decode("utf-8"), output5.decode("utf-8")
    
if __name__ == "__main__":
     my_file='log.txt'
     total = total_orders(my_file)
     
     num_of_NYSE_orders, num_filled_NYSE, partial_NYSE, cancelled_NYSE, expired_NYSE = nyse_orders(my_file) #output of this functions would be assigned to these may variables on the LHS
     num_of_NASDAQ_orders, num_filled_NASDAQ, partial_NASDAQ, cancelled_NASDAQ, expired_NASDAQ = nasdaq_orders(my_file)
     num_of_LSE_orders, num_filled_LSE, partial_LSE, cancelled_LSE, expired_LSE = lse_orders(my_file)
     num_of_PAR_orders,num_filled_PAR, partial_PAR, cancelled_PAR, expired_PAR = par_orders(my_file)
    
     total_fills = int(num_filled_NYSE) + int(num_filled_NASDAQ) + int(num_filled_LSE) + int(num_filled_PAR) #calculating total_fills partial and so on
     total_partial_fills = int(partial_NYSE) + int(partial_NASDAQ) + int(partial_LSE) + int(partial_PAR)
     total_cancels = int(cancelled_NYSE) + int(cancelled_NASDAQ) + int(cancelled_LSE) + int(cancelled_PAR)
     total_expired = int(expired_NYSE)+ int(expired_NASDAQ) + int(expired_LSE) + int(expired_PAR)
     
     y = PrettyTable() #forming a pretty table1
     y.field_names = ["Total Number of Orders"] #Adding a field and then rows
     y.add_row([total])
     
     x = PrettyTable() #2nd pretty table
     x.field_names = ["Market", "TotalOrders", "Fills", "Partial Fills", "Cancelled", "Expired"]
     x.add_row(["-----------", "-----------", "-----------", "-----------", "-----------", "-----------"])
     x.add_row(["NYSE", num_of_NYSE_orders, num_filled_NYSE, partial_NYSE, cancelled_NYSE,expired_NYSE])
     x.add_row(["NASDAQ", num_of_NASDAQ_orders, num_filled_NASDAQ, partial_NASDAQ, cancelled_NASDAQ, expired_NASDAQ])
     x.add_row(["LSE", num_of_LSE_orders,num_filled_LSE,partial_LSE, cancelled_LSE, expired_LSE ])
     x.add_row(["PAR", num_of_PAR_orders, num_filled_PAR, partial_PAR, cancelled_PAR, expired_PAR])
     x.add_row(["-----------", "-----------", "-----------", "-----------", "-----------", "-----------"])
    
     print(Fore.BLACK) #This is to change the forground color and have a colourful table
     print(Back.CYAN)
     print(Style.BRIGHT)
     print(y)
     print(x)
     print(Style.RESET_ALL)#resetting the colour changes done above

     #Creating two plots in one figure
     labels = ['NYSE', 'NASDAQ', 'LSE', 'PAR']
     sizes = [num_of_NYSE_orders, num_of_NASDAQ_orders, num_of_LSE_orders, num_of_PAR_orders]
     colors = ['yellowgreen', 'gold', 'darkorange', 'lightskyblue']
     labels_2 = 'Fills', 'PartialFills', 'Cancels', 'Expired'
     sizes_2 = [total_fills, total_partial_fills, total_cancels, total_expired]
     colors_2 = ['#4CAF50', 'hotpink', 'lightcoral', 'b']
     
     fig1, (plt1,plt2) = plt.subplots(1,2, figsize=(7,7)) #This is importatnt for subplotting

     patches, texts = plt1.pie(sizes, colors = colors, shadow = True, startangle = 90)
     plt1.legend(patches, labels, loc = "best", title = 'Markets: ')
     plt1.pie(sizes, explode = (0.1,0.1,0.1,0.1), colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)

     plt2.legend(patches, labels_2, loc = "best", title = 'Orders: ')
     plt2.pie(sizes_2, explode =(0.1,0.1,0.1,0.1), colors = colors_2, autopct='%1.1f%%', shadow = True, startangle = 90)

     plt1.axis('equal')
     plt2.axis('equal')
     
     plt.title('Market and Order Composition')
     plt.savefig('MarketAndOrderCompostion.png')
     plt.show()
     