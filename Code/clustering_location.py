import numpy as np;
import seaborn as sns; sns.set()

import plotly.plotly as py
import plotly.graph_objs as go
from matplotlib.colors import LogNorm
import csv


fh = open("C:\\Users\\kolev\\Documents\\v3_filter_loc.txt", "r")
col = []
col = fh.readline().strip() .split(",")

col2 = []
col2.append(col[7])
col2.append(col[8])
long=[]
lat=[]
count =1
loc = []
with open("C:\\Users\\kolev\\Documents\\just_location.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(col2)

    for line in fh:
        data = line.strip().split(",")

        if(len(data) == 9) and (float(data[7])>39.0 and float(data[7])<41) and (float(data[8])>-78.0 and float(data[8])<-76.0):
                loc.clear()
                loc.append(float(data[7]))
                loc.append(float(data[8]))
                writer.writerow(loc)
                count = count+1

print(count)





#
# import matplotlib.pyplot as plt
#
# print(count)
#
# x = np.array(long)
# y = np.array(lat)
#
# plt.hist2d(y, x, bins=2000, norm=LogNorm())
# #plt.colorbar()
# plt.show()