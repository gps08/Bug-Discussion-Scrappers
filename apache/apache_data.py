from bs4 import BeautifulSoup
import requests

bugs=open('apache_bugs','r').read().splitlines()
done=0
for bug in bugs:
	l=bug.split(',')
	save=open(l[0]+'-'+l[1],'w')
	html=requests.get(l[2]).text
	soup=BeautifulSoup(html,'html.parser')
	save.write(soup.title.string.encode('ascii','ignore'))
	if soup.find('div', {'class' :'user-content-block'})!=None:
		save.write(soup.find('div', {'class' :'user-content-block'}).text.encode('ascii','ignore'))
	li=soup.find_all('div', {'class' :'action-body flooded'})
	for i in li:
		save.write(i.get_text().encode('ascii','ignore')+'\n');
	done+=1
	print 'done',done,'of',len(bugs)

save.close()