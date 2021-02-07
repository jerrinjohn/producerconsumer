#!/usr/bin/env python3

import matplotlib.pyplot as plt
import subprocess
from prettytable import PrettyTable

def total_orders(myFile):
    count = 0    
    with open(myFile) as openfile:
        for line in openfile:
            for part in line.split("|"):
                if "35=D" in part:
                    count = count + 1
    return (count)

def nasdaq_orders(file_name):
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

def nyse_orders(file_name):
    #Counting total number of New Orders for NYSE
    p1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE) 
    p2 = subprocess.Popen(["grep", "35=D"], stdin = p1.stdout, stdout = subprocess.PIPE)
    p1.stdout.close()
    p3 = subprocess.Popen(["grep", "-c", "^"], stdin = p2.stdout, stdout = subprocess.PIPE)
    p2.stdout.close()
    output = p3.communicate()[0]
    
    #Counting total number of Filled orders for NYSE
    t1 = subprocess.Popen(["grep", "100=NYSE", file_name], stdout = subprocess.PIPE)
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

def lse_orders(file_name):
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

def par_orders(file_name):
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
    
    return output.decode("utf-8"), output2.decode("utf-8"), output3.decode("utf-8"), output4.decode("utf-8"), output5.decode("utf-8")

def market_pie_chart(num_of_NYSE_orders, num_of_NASDAQ_orders, num_of_LSE_orders, num_of_PAR_orders):
    # Data to plot
    #labels = 'Python', 'C++', 'Ruby', 'Java'
    labels = 'NYSE', 'NASDAQ', 'LSE', 'PAR'
    sizes = [num_of_NYSE_orders, num_of_NASDAQ_orders, num_of_LSE_orders, num_of_PAR_orders]
    colors = ['yellowgreen', 'gold', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0, 0)  # explode slice
    patches, texts = plt.pie(sizes, colors = colors, shadow = True, startangle = 90)
    plt.legend(patches, labels, loc = "best")
    #plot=>plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    plt.pie(sizes, explode = explode, colors = colors,
    autopct = '%1.1f%%', shadow = True, startangle = 140)
    plt.axis('equal')
    plt.savefig('orderPieChart.png')
    plt.show()

def market_pie_chart2(total_fills, total_partial_fills, total_cancels, total_expired):
    # Data to plot
    #labels = 'Python', 'C++', 'Ruby', 'Java'
    labels = 'Fills', 'PartialFills', 'Cancels', 'Expired'
    sizes = [total_fills, total_partial_fills, total_cancels, total_expired]
    colors = ['yellowgreen', 'gold', 'lightcoral', 'lightskyblue']
    explode = (0, 0, 0, 0)  # explode slice
    patches, texts = plt.pie(sizes, colors = colors, shadow = True, startangle = 90)
    plt.legend(patches, labels, loc = "best")
    #plot=>plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    plt.pie(sizes, explode = explode, colors = colors,
    autopct='%1.1f%%', shadow = True, startangle = 140)
    plt.axis('equal')
    plt.savefig('orderPieChart.png')
    plt.show()

if __name__=="__main__":
     my_file="messages.txt"
     total = total_orders(my_file)
     
     num_of_NYSE_orders, num_filled_NYSE, partial_NYSE, cancelled_NYSE, expired_NYSE = nyse_orders(my_file)
     num_of_NASDAQ_orders, num_filled_NASDAQ, partial_NASDAQ, cancelled_NASDAQ, expired_NASDAQ = nasdaq_orders(my_file)
     num_of_LSE_orders, num_filled_LSE, partial_LSE, cancelled_LSE, expired_LSE = lse_orders(my_file)
     num_of_PAR_orders,num_filled_PAR, partial_PAR, cancelled_PAR, expired_PAR = par_orders(my_file)
    
     total_fills = int(num_filled_NYSE) + int(num_filled_NASDAQ) + int(num_filled_LSE) + int(num_filled_PAR)
     total_partial_fills = int(partial_NYSE) + int(partial_NASDAQ) + int(partial_LSE) + int(partial_PAR)
     total_cancels = int(cancelled_NYSE) + int(cancelled_NASDAQ) + int(cancelled_LSE) + int(cancelled_PAR)
     total_expired = int(expired_NYSE)+ int(expired_NASDAQ) + int(expired_LSE) + int(expired_PAR)
     
     y = PrettyTable()
     y.field_names = ["Total Number of Orders"]
     y.add_row([total])
     
     x = PrettyTable()
     x.field_names = ["Market", "TotalOrders", "Fills", "Partial Fills", "Cancelled", "Expired"]
     x.add_row(["NYSE", num_of_NYSE_orders, num_filled_NYSE, partial_NYSE, cancelled_NYSE,expired_NYSE])
     x.add_row(["NASDAQ", num_of_NASDAQ_orders, num_filled_NASDAQ, partial_NASDAQ, cancelled_NASDAQ, expired_NASDAQ])
     x.add_row(["LSE", num_of_LSE_orders,num_filled_LSE,partial_LSE, cancelled_LSE, expired_LSE ])
     x.add_row(["PAR", num_of_PAR_orders, num_filled_PAR, partial_PAR, cancelled_PAR, expired_PAR])
     
     print(y)
     print(x)
     
     market_pie_chart(num_of_NYSE_orders, num_of_NASDAQ_orders, num_of_LSE_orders, num_of_PAR_orders)
     market_pie_chart2(total_fills, total_partial_fills, total_cancels, total_expired)
     
