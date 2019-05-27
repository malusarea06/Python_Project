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
		self.data = pd.read_csv(os.path.join( os.getcwd()+os.sep+"\\dataset\\",'matches.csv'))
		self.colum = [c for c in self.data.columns]
		total_seasons = set(self.data[self.colum[self.SEASON]])
		self.teams = set(self.data[self.colum[self.TEAM1]])
		
	'''This method returns multiple rows in Dataframe. Arguments list consist of filter values'''
	def readMultipleRows(self,data1,**kwargs):
	
		d = {}
		datafiltered = pd.DataFrame(data = data1)
		for key,value in kwargs.items():
			filtr = datafiltered[key].isin([value])
			d = pd.DataFrame(data = datafiltered[filtr])
			datafiltered = d
		
		return datafiltered	
	