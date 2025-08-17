# import csv
#
# with open('weather_data.csv','r') as f:
#     content=csv.reader(f)
#     temperature=[]
#     for row in content:
#         temperature.append(row[1])
#
#     print(temperature)


import pandas

content=pandas.read_csv('weather_data.csv')
maximun=content['temp'].max()
# print(maximun)
# list_temp=content['temp'].to_list()
#
# sum_temp=sum(list_temp)
# print(sum_temp/len(list_temp))

print(content[content.temp==maximun])
print(content[content.day=='Monday'])