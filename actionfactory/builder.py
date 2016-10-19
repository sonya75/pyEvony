import time
buildingbasetime = [0,75,300,600,45,60,90,30,0,0,0,0,0,0,0,0,0,0,0,0,270,240,180,750,3600,480,540,360,720,150,450,1800,1800]
class Builder:
	def __init__(self,city):
		self.city=city
	def createbuilding(self,castleid,positionid,buildingtype,tried=0):
		if tried==30:
			raise
		try:
			self.city.client.sendmessage('castle.newBuilding',{'castleId':castleid,'positionId':positionid,'buildingType':buildingtype})
			res=self.city.responsehandler('castle.newBuilding')
			if self.isBuildTime5MinOrLess(buildingtype,1):
				self.city.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'free.speed','castleId':castleid,'positionId':positionid})
				res=self.city.responsehandler('castle.speedUpBuildCommand')
		except Exception as e:
			if ((e.args[0]==-45)|(e.args[0]==-8)):
				time.sleep(2)
				self.createbuilding(castleid,positionid,buildingtype,tried=(tried+1))
				return
			raise e
	def upgradebuilding(self,castleid,positionid,buildingtype=-1,currentlevel=0,tried=0):
		if tried==30:
			raise
		try:
			self.city.client.sendmessage('castle.upgradeBuilding',{'castleId':castleid,'positionId':positionid})
			res=self.city.responsehandler('castle.upgradeBuilding')
			if self.isBuildTime5MinOrLess(buildingtype,currentlevel):
				self.city.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'free.speed','castleId':castleid,'positionId':positionid})
				res=self.city.responsehandler('castle.speedUpBuildCommand')
		except Exception as e:
			if ((e.args[0]==-45)|(e.args[0]==-8)):
				time.sleep(2)
				self.upgradebuilding(castleid,positionid,buildingtype,currentlevel,tried=(tried+1))
				return
			raise e
	def isBuildTime5MinOrLess(self,param1,param2):
		if (param1 == 27)&(param2 == 1):
			return True
		if (param1<0)|(param1>=len(buildingbasetime)):
			return False
		if (buildingbasetime[param1] == 0):
			return False
		x=buildingbasetime[param1]
		y=1
		while y<param2:
			x = x * 2
			y=y+1
		return (x <= 300)
	def speedup(self,castleid,itemid,positionid):
		self.city.client.sendmessage('castle.speedUpBuildCommand',{'itemId':itemid,'castleId':castleid,'positionId':positionid})
		res=self.city.responsehandler('castle.speedUpBuildCommand')
