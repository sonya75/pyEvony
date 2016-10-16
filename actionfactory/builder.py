buildingbasetime = [0,75,300,600,45,60,90,30,0,0,0,0,0,0,0,0,0,0,0,0,270,240,180,750,3600,480,540,360,720,150,450,1800,1800]
class Builder:
	def __init__(self,city):
		self.city=city
	def createbuilding(self,castleid,positionid,buildingtype):
		self.city.client.sendmessage('castle.newBuilding',{'castleId':castleid,'positionId':positionid,'buildingType':buildingtype})
		res=self.city.responsehandler('castle.newBuilding')
		if res['data']['ok']!=1:
			raise Exception('Building creation failed.')
		if self.isBuildTime5MinOrLess(buildingtype,1):
			self.city.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'free.speed','castleId':castleid,'positionId':positionid})
			res=self.city.responsehandler('castle.speedUpBuildCommand')
			if res['data']['ok']!=1:
				raise Exception('Free speed-up failed.')
	def upgradebuilding(self,castleid,positionid,buildingtype=-1,currentlevel=0):
		self.city.client.sendmessage('castle.upgradeBuilding',{'castleId':castleid,'positionId':positionid})
		res=self.city.responsehandler('castle.upgradeBuilding')
		if res['data']['ok']!=1:
			raise Exception('Building upgrade failed')
		if self.isBuildTime5MinOrLess(buildingtype,currentlevel):
			self.city.client.sendmessage('castle.speedUpBuildCommand',{'itemId':'free.speed','castleId':castleid,'positionId':positionid})
			res=self.city.responsehandler('castle.speedUpBuildCommand')
			if res['data']['ok']!=1:
				raise Exception('Free speed-up failed.')
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
