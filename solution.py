import numpy as np
import statsmodels.api as sm
from bokeh.plotting import figure, output_file, show
def solution():
    f=open("AirPassengers.csv",'r')
    text=f.readlines()[2:]
    X=[]
    Y=[]
    for line in text:
        X.append(float(line.split(",")[1]))
        Y.append(float(line[:-1].split(",")[2]))
        
    output_file("lines.html", title="line plot example")
    
    plot = figure(title="OLS plots",x_axis_label='time', y_axis_label='AirPassengers',width=800, height=700)
    plot.circle(X,Y,radius=0.05, size=20)

    X2=sm.add_constant(X)
    model=sm.OLS(Y,X2)
    results=model.fit()
    
    plot.line(X,results.predict(),legend="AirPassengers="+str(int(results.params[1]))+"*time"+str(int(results.params[0])),line_color="red",line_width=3)
    show(plot)
    return results.summary()
solution()