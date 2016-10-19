def cleanlines(x):
	y=[]
	for p in x:
		if "PROGRESSREPORT" not in p:
			y.append(p)
	return y
def countlines(x):
	return len([p for p in x if (len(p)>0)&(p[0]=='\t')])
def counttab(x):
	i=0
	for i in range(0,len(x)):
		if x[i]!='\t':
			break
	return i
def addprogress(x):
	q=[]
	x=cleanlines(x)
	total=countlines(x)
	i=1
	for t in x:
		f=counttab(t)
		if f==0:
			q.append(t)
			continue
		pro=round(i*100/total)
		i=i+1
		pre=''.join(['\t' for u in range(0,f)])
		msg=pre+"print(\"PROGRESSREPORT"+str(pro)+"\")\n"
		q.append(msg)
		q.append(t)
	return q
