from bs4 import BeautifulSoup
import requests

bugs=open('atlassian_bugs','r').read().splitlines()
done=0
for bug in bugs:
	l=bug.split(',')
	save=open(l[0]+'-'+l[1],'w')
	html=requests.get(l[2]).text
	soup=BeautifulSoup(html,'html.parser')
	#title
	save.write(soup.item.title.text.encode('ascii','ignore')+'\n')
	#description
	save.write(BeautifulSoup(soup.item.description.text,'html.parser').get_text().encode('ascii','ignore')+'\n')
	#comments
	li=soup.find_all('comment')
	for i in li:
		save.write(BeautifulSoup(i.text,'html.parser').get_text().encode('ascii','ignore')+'\n')
	done+=1
	print 'done',done,'of',len(bugs)

save.close()