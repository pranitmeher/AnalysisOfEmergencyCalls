import numpy as np;
import seaborn as sns; sns.set()

fh = open("C:\\Users\\kolev\\Documents\\v3_filter_loc.txt", "r")
col = []
col = fh.readline().strip() .split(",")

long=[]
lat=[]

for line in fh:
    data = line.strip().split(",")

    if(len(data) == 9) and (float(data[7])>39.0 and float(data[7])<41) and (float(data[8])>-78.0 and float(data[8])<-76.0):
            long.append(float(data[7]))
            lat.append(float(data[8]))

import matplotlib.pyplot as plt


x = np.array(long)
y = np.array(lat)


heatmap, xedges, yedges = np.histogram2d(x, y, bins=(200, 200))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

plt.clf()
plt.ylabel('y')
plt.xlabel('x')
plt.imshow(heatmap, extent=extent)
plt.show()

#
# ax = sns.heatmap(heatmap,cmap="YlGnBu")
#
# # ax = sns.heatmap(heatmap)
# plt.show()