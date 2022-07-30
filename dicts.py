inf = {
    'city':'moscow',
    'temperature':20}
print(inf['city'])
inf['temperature']=inf['temperature']-5
print(inf['temperature'])
print(inf)

print(inf.get('country','ru'))
inf['date']='27.2019'
print(inf)
print(len(inf))