import requests
#from lxml import html
from bs4 import BeautifulSoup as bs
from django.http import Http404

data = {'username':'nigel.yu',
        'password':'nigel711',
        'utf8':'✓',
        'login':'登入 »'}
login_url = 'http://10.61.22.16:3000/redmine/login/'

#Get Token
session_requests = requests.session()
try:
    res = session_requests.get(login_url)
    print("Redmine:"+ str(res.status_code))
except:
    print("Redmine:"+ str(res.status_code))
    print("Failed to Connect Redmine")
    raise Http404("Failed to Connect Redmine")
    
soup = bs(res.text, 'lxml')
data['authenticity_token'] = soup.find(attrs={'name':'authenticity_token'})['value']

#Login
req = session_requests.post(login_url, data = data)
print("login")


#for i in range(len(r_id)):
#	print('http://10.61.22.16:3000/redmine/issues/' + r_id[i].a.string)
	
#result2 = session_requests.get('http://10.61.22.16:3000/redmine/issues/38393')
#sp2 = bs(result2.text, 'lxml')
#description = sp2.find('div', class_='wiki').p.string
