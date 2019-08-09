import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('confusingdata.csv')

plt.plot(data['year'], data['DAPOClimate'], '--bo',)
line1 = np.polyfit(data['year'], data['DAPOClimate'], 1)
z = np.poly1d(line1)
first_label = "$\Delta APO_{Climate}$" +", "+ "$,slope=$" + "$" + str(np.round(line1[0], 2)) + "$"

#first_label = str(line1[0])

plt.plot(data['year'], z(data['year']),'-b', label = first_label)


plt.plot(data['year'], data['DAPOClimate'] + data["DAPOAtmD"],'--ro')
line2 = np.polyfit(data['year'], data['DAPOClimate'] + data["DAPOAtmD"], 1)
z2 = np.poly1d(line2)
second_label = "$\summation$" + str(line2[0])
second_label = str(line2[0])

second_label = "$\Delta APO_{Climate + AtmD}$" +", "+ "$slope=$" + "$" + str(np.round(line2[0], 2)) + "$"

plt.plot(data['year'], z2( data['year'] ), 'r' , label = second_label)


plt.grid()
plt.legend()
plt.xlabel('year')
plt.savefig('pic.png')
plt.show()


