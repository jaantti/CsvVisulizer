import csv
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

with open('test.csv', newline='') as file:
  reader = csv.DictReader(file)
  print(reader.fieldnames)
  for row in reader:
    y.append(row['val1'])
    x.append(row['time'])

#x = np.linspace(0, 2, 100)

plt.plot(x, y, label='linear')
#plt.plot(x, x**2, label='quadratic')
#plt.plot(x, x**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()
