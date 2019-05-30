from Modules.Matches import Matches
from Modules.Deliveries import Deliveries
import operator
from functools import reduce
import pandas as pandas
from prettytable import PrettyTable

class RunAll:
	
	final_teams = {}
	m = Matches()
	d = Deliveries()
	f_count,s_count,total_Score=0,0,0
	'''This method displays top 4 team of 2016 and 2017 who choose to field after winnig toss'''
	def firsrtQuery(self):

		season  = [2016,2017]

		for s in season:
			data = (self.m.readMultipleRows(self.m.data,SEASON = s,TOSS_DECISION='field'))	#fetch dataframe according to season. fetch tems who choose to field			
			for team in self.m.teams:
				winner = (self.m.readMultipleRows(data,TOSS_WINNER=team,WINNER=team))		#filter data on data. Teams who won the toss and match both.
				if(winner.shape[0] > 0):
					self.final_teams.update({team : winner.shape[0]})

			result = self.sort_dict(self.final_teams) #Returns list of tuples
			print("{}\t\t{}\t\t\t{}".format('YEAR','TEAM','COUNT'))
			print("----------------------------------------------------")

			for i in range(0,4):
				print("{}\t\t{}\t\t\t{}".format(s,result[i][0],result[i][1]))

			print("\n\n")	

	
	'''This method return list of tuples sorted in descending order.
		This method sorts the team in descending order depending on win count'''
	def sort_dict(self,dictnry):
		winner_teams = list(dictnry.items())
		
		for i in range(len(winner_teams)-1,-1,-1):
			for j in range(i):
				if winner_teams[j][1] < winner_teams[j+1][1]:
					winner_teams[j] , winner_teams[j+1] = winner_teams[j+1] , winner_teams[j] 
		
		return winner_teams

	

	'''  This method displays total fours,six and total runs with respect to Team and year'''
	def secondQuery(self):

		for s in self.m.total_seasons	:		
			data = (self.m.readMultipleRows(self.m.data,SEASON = s))	#get all matches from particular season
			
			t = PrettyTable(['YEAR','Team Name','Four Count','Six count','Total Score'])
			
			for team in self.m.teams:
				filterd = (self.m.readMultipleRows(data,TEAM1 = team))		#get matches according to team in same season from TEAM1
				fil = (self.m.readMultipleRows(data,TEAM2=team))		#get matches according to team in same season from TEAM1
				combine  = pandas.concat([filterd,fil])					#get total matches of single team
				match_id = set(combine[self.m.colum[self.m.MATCH_ID]])		#get match_id for particular  team
				self.total_Score = 0
				self.f_count = 0
				self.s_count = 0
				for m_id in match_id :
					ddata = self.d.readMultipleRows(self.d.data,MATCH_ID = m_id,BATTING_TEAM=team)		#from deliveries.py get all innings detail for respective match_id
					fourd = self.d.readMultipleRows(self.d.data,MATCH_ID = m_id,BATTING_TEAM=team,TOTAL_RUNS=4)	#count number of four's for team
					sixd = self.d.readMultipleRows(self.d.data,MATCH_ID = m_id,BATTING_TEAM=team,TOTAL_RUNS=6)	#count number of six for team
					#print(ddata.shape[0])		
					if len(ddata['TOTAL_RUNS']) > 0:	
						self.total_Score =self.total_Score + reduce(operator.add,ddata['TOTAL_RUNS'])	#count total score for particular team
						self.f_count =self.f_count + fourd.shape[0]
						self.s_count =self.s_count + sixd.shape[0]
					else:
						continue
				t.add_row([s,team,self.f_count,self.s_count,self.total_Score])		#add data to table 
			print(t) #print tabular data
			t.clear_rows()					

d = RunAll()
#d.firsrtQuery()
d.secondQuery()

