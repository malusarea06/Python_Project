import pandas as pd 
import os
class Deliveries:
	

	

	MATCH_ID = 0
	INNING = 1,
	BATTING_TEAM = 2
	BOWLING_TEAM = 3
	OVER = 4 
	BALL = 5 
	BATSMAN = 6
	BOWLER = 7
	WIDE_RUNS = 8
	BYE_RUNS = 9
	LEGBYE_RUNS = 10
	NOBALL_RUNS = 11
	PENALTY_RUNS = 12 
	BATSMAN_RUNS = 13
	EXTRA_RUNS = 15
	TOTAL_RUNS = 16

	data = ""


	def __init__(self):
		self.data = pd.read_csv(os.path.join( os.getcwd()+os.sep+"\\dataset\\",'deliveries.csv'))
		self.colum = [c for c in self.data.columns]
			

	def readMultipleRows(self,data1,**kwargs):
		d = {}
		datafiltered = pd.DataFrame(data = data1)
		for key,value in kwargs.items():
			filtr = datafiltered[key].isin([value])
			d = pd.DataFrame(data = datafiltered[filtr])
			datafiltered = d
		
		return datafiltered	