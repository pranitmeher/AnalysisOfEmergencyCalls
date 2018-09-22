import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
from matplotlib.colors import LogNorm


fh = open("C:\\Users\\kolev\\Documents\\v3_filter_loc.txt", "r")
col = []
col = fh.readline().strip() .split(",")

time = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(len(time))
count =1

for line in fh:
    data = line.strip().split(",")

    if(len(data) == 9) and (float(data[7])>39.0 and float(data[7])<41) and (float(data[8])>-78.0 and float(data[8])<-76.0) and int(data[2]) == 3:

            k = (int(data[5].split(":")[0]))
            time[k] = time[k] +1
            count = count+1


print(time)
