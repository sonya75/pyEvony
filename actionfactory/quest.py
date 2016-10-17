class Quest:
	def __init__(self,city,castleid=None):
		global castleId
		self.city=city
		castleId=castleid
	def completequest(self,questid,castleid=castleId):
		self.city.client.sendmessage('quest.award',{'questId':553,'castleId':castleid})
		res=self.city.responsehandler('quest.award')