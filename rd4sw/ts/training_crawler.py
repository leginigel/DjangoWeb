from .redmine_login import session_requests
from bs4 import BeautifulSoup as bs

def training(cate):

	item_data = {}
	url = ""
	
	if cate == 'swone':
		url = 'http://10.61.22.16:3000/redmine/projects/2017-m97dx/issues'
	elif cate == 'android':
		url = 'http://10.61.22.16:3000/redmine/projects/eulopz/issues'
	elif cate == 'tv':
		url = 'http://10.61.22.16:3000/redmine/projects/euloij/issues'
	elif cate == 'other':
		url = 'http://10.61.22.16:3000/redmine/projects/euloqb/issues'
	
	#Crawler
	print("Crawler " + cate.upper() + " Training")
	result1 = session_requests.get(url)
	sp1 = bs(result1.text, 'lxml')

	print("Get Redmine Item")
	owner = sp1.find_all('td','assigned_to')
	subject = sp1.find_all(class_='subject')
	updated_time = sp1.find_all(class_='updated_on')
	r_id = sp1.find_all(class_='id')

	for i in range(len(r_id)):
		print(cate.upper() + " Crawler #" + r_id[i].a.string)
		result2 = session_requests.get(
			'http://10.61.22.16:3000/redmine/issues/' + r_id[i].a.string)
		sp2 = bs(result2.text, 'lxml')
		try:
			des = sp2.find('div', class_='description').find('div', class_='wiki')
			description = str(des)
		except:
			description = ''

		item_data.update({
			i : {'rid' : r_id[i].a.string,
				 'owner' : owner[i].string,
				 'subject' : subject[i].a.string,
				 'time' : updated_time[i].string,
				 'description' : description}
			})
	return item_data
	
sw1_data = training('swone')
#sw2_data = training('swtwo')
android_data = training('android')
tv_data = training('tv')
other_data = training('other')