import numpy as np;
import seaborn as sns; sns.set()

import plotly.plotly as py
import plotly.graph_objs as go
from matplotlib.colors import LogNorm


fh = open("C:\\Users\\kolev\\Documents\\v3_filter_loc.txt", "r")
col = []
col = fh.readline().strip() .split(",")

long=[]
lat=[]
count =1

for line in fh:
    data = line.strip().split(",")

    if(len(data) == 9) and (float(data[7])>39.0 and float(data[7])<41) and (float(data[8])>-78.0 and float(data[8])<-76.0) and int(data[2]) == 3:
            long.append(float(data[7]))
            lat.append(float(data[8]))
            count = count+1

import matplotlib.pyplot as plt

print(count)

x = np.array(long)
y = np.array(lat)

plt.hist2d(y, x, bins=2000, norm=LogNorm())
#plt.colorbar()
plt.show()