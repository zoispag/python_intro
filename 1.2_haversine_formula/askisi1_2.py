import math as m

lat1, lon1 = input("Enter co-ordinates of point A : [latitude longitude]: ").split(' ')
lat2, lon2 = input("Enter co-ordinates of point B: [latitude longitude]: ").split(' ')

# lat1, lon1 = '40.6', '22.95'
# lat2, lon2 = '37.95', '23.72'

lat1 = m.radians(float(lat1))
lon1 = m.radians(float(lon1))
lat2 = m.radians(float(lat2))
lon2 = m.radians(float(lon2))

dlat = lat1 - lat2
dlon = lon1 - lon2

a = m.sin(dlat/2)**2 + m.cos(lat1) * m.cos(lat2) * m.sin(dlon/2)**2
c = 2 * m.asin(m.sqrt(a))
R = 6372.8

d = R * c

print('The distance between points A and B is about {:.0f} kilometers'.format(d))