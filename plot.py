import csv
import matplotlib.pyplot as pyg
ide = [];
price = [];
with open("data.csv","r") as csvf:
	read = csv.DictReader(csvf)
	for row in read:
		ide.append(row['id'])
		price.append(row['price'])
pyg.plot(ide,price)
pyg.show()
