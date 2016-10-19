import time
class Quest:
	def __init__(self,city,castleid=None):
		global castleId
		self.city=city
		self.castleid=castleid
		self.qcompleted=[]
	def completequest(self,questid,castleid=None,wait=True,tried=0):
		if tried==60:
			return
		if castleid==None:
			castleid=self.castleid
		self.city.client.sendmessage('quest.getQuestType',{'castleId':castleid,'type':1})
		qlist=self.city.responsehandler('quest.getQuestType')
		for p in qlist['data']['types']:
			if p['isFinish']:
				self.city.client.sendmessage('quest.getQuestList',{'castleId':castleid,'typeId':p['typeId']})
				res=self.city.responsehandler('quest.getQuestList')
				for q in res['data']['quests']:
					if q['isFinish']:
						self.city.client.sendmessage('quest.award',{'questId':q['questId'],'castleId':castleid})
						res=self.city.responsehandler('quest.award')
						self.qcompleted.append(q['questId'])
		if questid in self.qcompleted:
			time.sleep(1)
			return
		else:
			if wait:
				time.sleep(1)
				self.completequest(questid,castleid,tried=(tried+1))
				return
	def special(self):
		while True:
			self.city.client.sendmessage('quest.getQuestList',{'castleId':(self.castleid),'typeId':66})
			res=self.city.responsehandler('quest.getQuestList')
			if res['data']['quests'][0]['isFinish']:
				break
			time.sleep(1)
		while True:
			self.city.client.sendmessage('quest.award',{'questId':3,'castleId':(self.castleid)})
			res=self.city.responsehandler('quest.award')
			self.city.client.sendmessage('quest.getQuestList',{'castleId':(self.castleid),'typeId':66})
			res=self.city.responsehandler('quest.getQuestList')
			if res['data']['quests'][0]['questId']!=3:
				break
			time.sleep(1)
		self.qcompleted.append(3)
