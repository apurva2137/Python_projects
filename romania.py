import csv

data=[]

with open('dataset.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
   
    for row in csv_reader:
        data.append(row)
       
def probability(data, num, insta):
    count = 0
    for datas in data:
        if datas[num].strip() == insta.strip():
            count += 1
    return count / len(data)

print(probability(data, 4, 'yes'))


outlook = {}
outlook["sunny"]=probability(data,0,'sunny')
outlook["rainy"]=probability(data,0,'rainy')
outlook["overcast"]=probability(data,0,'overcast')


tempreture = {}
tempreture["hot"]=probability(data,1,'hot')
tempreture["mild"]=probability(data,1,'mild')
tempreture["cold"]=probability(data,1,'cold')


Humidity = {}
Humidity["high"]=probability(data,2,'high')
Humidity["normal"]=probability(data,2,'normal')


windy = {}
windy["true"]=probability(data,3,'true')
windy["false"]=probability(data,3,'false')

play = {}
play["yes"]=probability(data,4,'yes')
play["no"]=probability(data,4,'no')






       
def play(data):
   
       
               
play(data)