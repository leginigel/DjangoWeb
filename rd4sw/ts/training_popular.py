from .training_crawler import other_data, tv_data, android_data, sw1_data
from datetime import datetime

recent = ['','','','']
top = ['','','','']
format = '%Y-%m-%d %H:%M'
list = []
#s = datetime.strptime(time, format)
#item_data[1]['time']

print('Arrange 4 New')

#list[(0time,1cate,2num)]
#1:sw1 2:android 3:tv 4:other
for i in range(1,5):
	try:
		list.append((datetime.strptime(sw1_data[i]['time'], format),1,i))
		list.append((datetime.strptime(android_data[i]['time'], format),2,i))
		list.append((datetime.strptime(tv_data[i]['time'], format),3,i))
		list.append((datetime.strptime(other_data[i]['time'], format),4,i))
	except:
		pass
list.sort(reverse=True)
for j in range(4):
	if list[j][1] == 1:
		top[j] = sw1_data[list[j][2]]
	elif list[j][1] == 2:
		top[j] = android_data[list[j][2]]
	elif list[j][1] == 3:
		top[j] = tv_data[list[j][2]]
	elif list[j][1] == 4:
		top[j] = other_data[list[j][2]]
	print(top[j])

print('Get 4 First')
recent[0] = sw1_data[0]
recent[1] = android_data[0]
recent[2] = tv_data[0]
recent[3] = other_data[0]