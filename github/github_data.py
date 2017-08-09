import requests
bugs=open('github_bugs','r').read().splitlines()
done=0
for bug in bugs:
	l=bug.split(',')
	save=open(l[0]+'-'+l[1],'w')
	js=requests.get(l[2],auth=('<user>','<pass>')).json()
	save.write(js['title'].encode('ascii','ignore')+'\n')
	save.write(js['body'].encode('ascii','ignore')+'\n')
	js=requests.get(l[2]+'/comments',auth=('<user>','<pass>')).json()
	for i in js:
		save.write(i['body'].encode('ascii','ignore'))
	save.close()
	done+=1
	print 'done',done,'of',len(bugs)