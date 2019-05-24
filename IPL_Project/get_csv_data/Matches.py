import pandas as pd
import os
class Matches:
	
	#Column Index Numbers
	MATCH_ID = 0
	SEASON = 1
	CITY = 2
	DATE = 3
	TEAM1 = 4
	TEAM2 = 5
	TOSS_WINNER = 6
	TOSS_DECISION = 7
	RESULT = 8
	WINNER = 9

	data = ""
	colum = []
	teams = []
	def __init__(self):
		self.data = pd.read_csv(os.path.join( os.getcwd()+os.sep+os.pardir+"\\dataset\\",'matches.csv'))
		self.colum = [c for c in self.data.columns]
		total_seasons = set(self.data[self.colum[self.SEASON]])
		self.teams = set(self.data[self.colum[self.TEAM1]])
		
	
	def readSingleRow(self,dataf,**kwargs):
		
		
		#print(self.data[["MATCH_ID","TEAM1"]])
		d = {}
		for key,value in kwargs.items():
			f2 = dataf[key].isin([value])
			d = pd.DataFrame(data = dataf[f2])
			return d

		print("Out of loop")
		#print(d)
		#f = self.data["SEASON"].isin(["2017"])
		#f1 = self.data["TOSS_DECISION"].isin(["field"])
		#d = self.data[f & f1].to_dict()
