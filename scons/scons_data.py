from bs4 import BeautifulSoup
import requests

bugs=open('scons_bugs','r').read().splitlines()
done=0
for bug in bugs:

	l=bug.split(',')
	save=open(l[0]+'-'+l[1],'w')
	html=requests.get(l[2]).text
	soup=BeautifulSoup(html,'html.parser')
	
	#comments
	c=1
	while soup.find('div', {'id' :'desc'+str(c)})!=None:
		save.write(soup.find('div', {'id' :'desc'+str(c)}).get_text().encode("ascii","ignore")+'\n')
		c+=1

	done+=1
	print 'done',done,'of',len(bugs)

	save.close()