# -*- coding: utf8 -*-
import re
import requests
from bs4 import BeautifulSoup

user= '13520149'
password = 'xxxxxxx'

def get(fp):
	soup =BeautifulSoup(fp,"html.parser")
	tags= soup.find_all('table')
	dem=0
	for tag in tags:
		print tag.get_text() + "##"+str(dem)
		dem=dem+1

	text=tags[4].get_text()
	with open("gettext.txt","w+") as wr:
		wr.write(text)
		wr.close()

def test(file):
	text=list()
	soup = BeautifulSoup(file,"html.parser")
	tags= soup.find_all('table',{"class":"event"})
	for tag in tags:
		text.append(tag.get_text())
	return text
	


r =requests.Session()

r.data = {'username':user,'password':password}
link = str('https://courses.uit.edu.vn/login/index.php')
s = r.post(link,data=r.data)
#with open("courses.html") as fp:
soup =BeautifulSoup(s.text,"html.parser")
tags= soup.find_all(id=re.compile('(calendar_tooltip_).'))
i=1
for tag in tags:
	if '#' == str(tag.get('href')):
		continue
	html=r.get(str(tag.get('href')))
	with open("text/text"+str(i),"wb+") as file:
		handle = test(html.text)
		for a in handle:
			t = a.encode('utf-8', 'replace')#.decode('utf-8')
			file.write(t)
			file.write("############")
			file.close
			i=i+1






	#with open("EVENT.html") as fp:



'''

######################################################################################################
s=r.get(str('https://daa.uit.edu.vn/user/login%26homepage?destination=node'))#name=13520149&pass=jetjokers24895&form_build_id=form-r495K7NhyeiePjBoMbaevHbKd05G7boL7gO4CFNUyVY&form_id=user_login_block&op=%C4%90%C4%83ng+nh%E1%BA%ADp: undefined
find = str(r'<div class="item-list"><\/div><input type="hidden" name="form_build_id" value="(.+)" \/>')
test =re.search(find,s.text)
form= test.group(1)
r.data={'name':'13520149','pass':'jetjokers24895','form_build_id':form,'form_id':'user_login_block','op':str('%C4%90%C4%83ng+nh%E1%BA%ADp: undefined')}
s1=r.post(str('https://daa.uit.edu.vn/user/login%26homepage?destination=node'),data=r.data)
s2=r.get('https://daa.uit.edu.vn/sinhvien/bang-dieu-khien')
print s2.text
'''