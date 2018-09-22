import gmplot as gmap
import gmaps

gmaps.configure(api_key="AIzaSyB33EJd1GZHrXi-lOScPv4lZ3P5gycT2Xo")

lat = [39.2741,	39.3741,	39.3409,	39.3091,	39.2871,	39.2929,	39.3515,	39.2911,	39.2378,	39.3193]

lon = [-76.6341,	-76.668,	-76.6753,	-76.6479,	-76.6721,	-76.6123,	-76.578,	-76.5663,	-76.6078,	-76.5863 ]

# locc=[]
# for i in range(len(lat)):
#        locc.append([lat[i],lon[i]])

gmap = gmap.GoogleMapPlotter(39.3072, -76.6206, 12)

gmap.scatter(lat,lon, 'r', size=400, marker=False)


gmap.draw("mymappoints10.html")
