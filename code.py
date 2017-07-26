import csv
from copy import deepcopy
temp=[]
li=[]
count=-1
d = {}
with open('number.csv','r')as csvf:
	reader=csv.reader(csvf)
	for x in list(reader)[0]:
		count+=1
		if x=='' and count%2!=0:
			d['id']=count
			li.append(deepcopy(d))
		elif x=='' and count%2==0:
			temp.append(count)
		else:
			d['id']=int(x)
			li.append(deepcopy(d))
		
size=count-len(temp)
with open('fruits.csv','r') as csvf:
	reader=csv.reader(csvf)
	count=-1
	for fruit in list(reader)[0]:
		count+=1
		if count not in temp:
			for d in li:
				if d['id']==int(count):
					d['name']=fruit
					
	i=0
	for d in li:
		if d['name']=="":
			d['name']=li[(i-9)%size]['name']
			i+=1	
count=-1	
with open('rotten.csv','r') as csvf:
	read=csv.reader(csvf)
	for waste in list(read)[0]:
		count+=1
		for d in li:
			if d['id'] ==count:
				if waste =='0':
					waste='f'
				if waste == '1':
					waste='t'
				d['rot']=waste
count=-1
with open('price.csv','r') as csvf:
	read=csv.reader(csvf)
	for cost in list(read)[0]:
		count+=1
		for d in li:
			if d['id']== count:
				if cost == '':
					d['price']=0.0
				else:
					d['price']=float(cost)
				if d['rot']=='t':
					d['price']=0.0
with open("data.csv","w") as csvf:
	fieldnames = ['id','name','price','rot']
	writ = csv.DictWriter(csvf,fieldnames);
	writ.writeheader();
	for d in li:
		writ.writerow(d);
with open("number.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['id'] for d in li])
with open("fruits.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['name'] for d in li])
with open("price.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['price'] for d in li])
with open("rotten.csv","w") as csvf:
	writ = csv.writer(csvf)
	writ.writerow([d['rot'] for d in li])


			
			
