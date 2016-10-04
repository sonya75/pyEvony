from evony import *
import string 
import random
import json
import time
import pyamf
import sys
from pyamf import sol
def createacc(server):
	num=random.randint(9,12)
	email=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
	email=email+'@gmail.com'
	try:
		x=Client(server,email,'aaaaaa',True)
		x.close()
		print('Successfully created account for email address '+email+' on server '+server)
		return email,'aaaaaa'
	except:
		return
def getsolpath(path):
	path=path.split(os.sep)
	if len(path)==0:
		print('Invalid path')
		raise
	path=path[1:]
	p=os.path.expanduser('~')
	path=(os.sep).join(path)
	p=os.path.join(p,'AppData','Roaming','Macromedia','Flash Player','#SharedObjects')
	p=os.path.join(p,os.listdir(p)[0])
	p=os.path.join(p,'localhost',path)
	return p
def buildacc(server,email,password,buildaccscript='buildacc.txt'):
	d=open(buildaccscript,'r').read()
	num=random.randint(5,8)
	name=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
	d=d.replace('put_some_random_name_here',name)
	d=d.replace('\n','\r')
	num=random.randint(2,5)
	name=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
	d=d.replace('put_flagname_here',name)
	num=random.randint(3,7)
	name=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(num))
	d=d.replace('put_cityname_here',name)
	e=json.loads(open('Alts.json','r').read())
	if email not in e:
		print('Email is not found in Alts.json')
		raise
	s=e[email]
	if len(s.keys())!=1:
		print('This account has more than one city')
		raise
	castleid=s.keys()[0]
	solname='citytab'+str(castleid)
	script=sol.SOL(solname)
	ss=os.path.join(getsolpath(os.getcwd()),'roboevony.exe')
	if not os.path.exists(ss):
		os.makedirs(ss)
	solpath=os.path.join(ss,(solname+'.sol'))
	configpath=os.path.join(ss,'config.sol')
	config={'username': email, 'password': 'aaaaaa', 'autoScript': True, 'autoLogin': True, 'server': server, 'autoLoginMinTime': '1', 'autoRun': True, 'autoLoginMaxTime': '10'}
	conf=sol.SOL('config')
	conf['now']=config
	c=open(configpath,'wb')
	sol.save(conf,c)
	c.close()
	script['now']=d
	c=open(solpath,'wb')
	sol.save(script,c)
	c.close()
	os.system('start /min roboevony.exe')
	print('Succesfully started building account '+email+' on server '+server)
number=sys.argv[1]
server=sys.argv[2]
i=0
while i<number:
	try:
		d,dd=createacc(server)
		buildacc(server,d,dd)
		time.sleep(20)
		i=i+1
	except:
		continue