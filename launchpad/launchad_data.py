from bs4 import BeautifulSoup
import requests

bugs=open('launchpad_bugs','r').read().splitlines()
done=0
for bug in bugs:
	l=bug.split(',')
	save=open(l[0]+'-'+l[1],'w')
	html=requests.get(l[2]).text
	soup=BeautifulSoup(html,'html.parser')
	
	#title
	save.write(soup.title.string.encode('ascii','ignore')+'\n')
	
	#description
	if soup.find('div', {'class' :'yui3-editable_text-text'})!=None:
		save.write(BeautifulSoup(soup.find('div', {'class' :'yui3-editable_text-text'}).text,'html.parser').get_text().encode('ascii','ignore')+'\n')
	
	#comments
	li=soup.find_all('div', {'class' :'comment-text'})
	for i in li:
		save.write(i.get_text().encode('ascii','ignore')+'\n');
	done+=1
	print 'done',done,'of',len(bugs)

save.close()