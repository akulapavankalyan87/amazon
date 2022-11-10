import pandas as pd
import matplotlib.pyplot as plt

def line_plot(x,y,z):
    """This function is used for line plot"""
    plt.figure(figsize=(15, 10))
    plt.plot(x,y,marker=".",mec="r",mfc="r",label="Opening Value")
    plt.plot(x,z,c="r",marker=".",mec="b",mfc="b",label="Closing Value")
    plt.legend()
    plt.grid(ls="dotted")
    f1 = {'color':'red','size':'20'}
    plt.title("Amazon Opening and Closing share value of August Month 2022",fontdict=f1)
    plt.xlabel("Date",fontdict=f1)
    plt.ylabel("Opening and Closing price",fontdict=f1)
    plt.show()
    plt.close()
    
def bar_plot(x,y):
    """This function is used for bar graph"""
    plt.figure(figsize=(15, 10))
    plt.bar(x,y,width=0.2)
    f1 = {'color':'red','size':'20'}
    plt.title("Date vs Volume",fontdict=f1)
    plt.xlabel("Date",fontdict=f1)
    plt.ylabel("Volume",fontdict=f1)
    plt.show()
    plt.close()
    
def scatter_plot(x,y,z):
    """This function is used for scatter plot"""
    plt.figure(figsize=(20, 10))
    plt.scatter(x,y,c="b",s=50,label="Low Value")
    plt.scatter(x,z,c="r",s=50,label="High Value")
    plt.legend()
    f1 = {'color':'red','size':'20'}
    plt.title("Scatter plot between high and low values and date",fontdict=f1)
    plt.xlabel("Date",fontdict=f1)
    plt.ylabel("High and Low Values",fontdict=f1)
    plt.show()
    plt.close()
    
def piechart(x,y):
    """This function is for pie chart"""
    profit = 0
    loss = 0
    z = len(x)
    for i in range(z):
        if(x[i]>y[i]):
            loss+=1
        if(x[i]<y[i]):
            profit+=1
    profit_percentage = round((profit/z)*100,2)
    loss_percentage = 100-profit_percentage
    l1 = ["Profit"+"("+str(profit_percentage)+"%)","Loss"+"("+str(loss_percentage)+"%)"]
    l2 = [profit,loss]
    
    plt.pie(l2,labels=l1)
    f1 = {'color':'red','size':'20'}
    plt.title("Estimation of profit and loss over a period",fontdict=f1)
    plt.show()
    
# Parsing the data and extracting the data
data = pd.read_csv("AMZN.csv",header = None)
date = data[0][1:]
open_value = [float(i) for i in data[1][1:]]
high_value = [float(i) for i in data[2][1:]]
low_value = [float(i) for i in data[3][1:]]
close_value = [float(i) for i in data[4][1:]]
volume = [int(i) for i in data[6][1:]]

line_plot(date,open_value,close_value)
bar_plot(date,volume)
scatter_plot(date,low_value,high_value)
piechart(open_value,close_value)