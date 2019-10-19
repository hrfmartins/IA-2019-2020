import pickle
import math

with open("coords.pickle", "rb") as fp:   # Unpickling
    coords = pickle.load(fp)

distance = []
for element in coords:
    d = []
    for el in coords:
        if element == el:
                d.append(0)
        else:
            a = element[0] - el[0]
            b = element[1] - el[1]
            dist = math.sqrt(a**2 + b**2)
            d.append(dist)
    distance.append(d)

print(distance)
