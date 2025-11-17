#MapPlot.py
#Name:
#Date:
#Assignment:

import cars
import pandas
import matplotlib.pyplot as plt
car = cars.get_car()


years = []
mpgs = []
for tire in car:
    mpg = tire["Fuel Information"]["City mpg"]
    year = tire["Identification"]["Year"]
    years.append(year)
    mpgs.append(mpg)
    #print(make, year)

df = pandas.DataFrame({"Year": years,
                        "City mpg": mpg})
print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'City mpg')
plt.plot(years, mpgs, 'ro')
plt.savefig("output")