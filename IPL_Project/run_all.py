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
		t = PrettyTable(['YEAR','TEAM','COUNT'])
		for s in season:
			data = (self.m.readMultipleRows(self.m.data,SEASON = s,TOSS_DECISION='field'))	#fetch dataframe according to season. fetch tems who choose to field			
			for team in self.m.teams:
				winner = (self.m.readMultipleRows(data,TOSS_WINNER=team,WINNER=team))		#filter data on data. Teams who won the toss and match both.
				if(winner.shape[0] > 0):
					self.final_teams.update({team : winner.shape[0]})

			result = self.sort_dict(self.final_teams) #Returns list of tuples
			

			for i in range(0,4):
				t.add_row([s,result[i][0],result[i][1]])
				

			print(t)
			t.clear_rows()	

	
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
				self.total_Score,self.f_count,self.s_count = 0,0,0
				
				for m_id in match_id :
					ddata = self.d.readMultipleRows(self.d.data,MATCH_ID = m_id,BATTING_TEAM=team)		#from deliveries.py get all innings detail for respective match_id
					fourd = self.d.readMultipleRows(self.d.data,MATCH_ID = m_id,BATTING_TEAM=team,BATSMAN_RUNS=4)	#count number of four's for team
					sixd = self.d.readMultipleRows(self.d.data,MATCH_ID = m_id,BATTING_TEAM=team,BATSMAN_RUNS=6)	#count number of six for team
						
					if len(ddata['TOTAL_RUNS']) > 0:	
						
						batsmen_run = reduce(operator.add,ddata['BATSMAN_RUNS'])
						penlty_runs = reduce(operator.add,ddata['PENALTY_RUNS'])
						extra_runs = reduce(operator.add,ddata['EXTRA_RUNS'])
						no_ball = reduce(operator.add,ddata['NOBALL_RUNS'])
						legbye = reduce(operator.add,ddata['LEGBYE_RUNS'])
						bye = reduce(operator.add,ddata['BYE_RUNS'])
						wide = reduce(operator.add,ddata['WIDE_RUNS'])
						self.total_Score =self.total_Score + batsmen_run + penlty_runs + extra_runs + no_ball + legbye + bye + wide	#count total score for particular team
						self.f_count =self.f_count + fourd.shape[0]
						self.s_count =self.s_count + sixd.shape[0]
					else:
						continue
				t.add_row([s,team,self.f_count,self.s_count,self.total_Score])		#add data to table 
			print(t) #print tabular data
			t.clear_rows()					

	
	''' This method displays top 10 best economy rate bowlers'''
	def thirdQuery(self):

		b_count = 0
		bowlrs = {}
		t = PrettyTable(['YEAR','BOWLER','ECONOMY'])

		for s in self.m.total_seasons:
			match_data = self.m.readMultipleRows(self.m.data,SEASON = s)		#get season wise matches
			match_id = set(match_data[self.m.colum[self.m.MATCH_ID]])
			bowlrs.clear()
			for bow in self.d.bowlers:
			
				b_count,total_runs,economy = 0,0,0
				for m in match_id:
					match_d = self.d.readMultipleRows(self.d.data,MATCH_ID=m,BOWLER=bow)	#get all the matches that bowler has played
					
					if match_d.shape[0] > 0:
						b_count =b_count + len(set(match_d[self.d.colum[self.d.OVER]]))
						batsmen_run = reduce(operator.add,match_d['BATSMAN_RUNS'])
						penlty_runs = reduce(operator.add,match_d['PENALTY_RUNS'])
						extra_runs = reduce(operator.add,match_d['EXTRA_RUNS'])
						no_ball = reduce(operator.add,match_d['NOBALL_RUNS'])
						wide = reduce(operator.add,match_d['WIDE_RUNS'])
						total_runs = total_runs + batsmen_run + penlty_runs + extra_runs + no_ball + wide

				if(b_count > 10):
					economy = total_runs/b_count		#calculate economy
					bowlrs.update({bow: economy})
						
				else:
					continue
		
			result = self.sort_dict(bowlrs)
			for i in range(len(result)-1,len(result)-11,-1):
				t.add_row([s,result[i][0],round(result[i][1],2)])
			print(t)
			t.clear_rows()

	'''This method displays team having highest net run rate of each season'''
	def fourthQuery(self):

		final_t = {}
		t = PrettyTable(['YEAR','Team Name'])
		print('Team Having Highest Run Rate')
		for s in self.m.total_seasons:
			
			final_t.clear()
			season_data = self.m.readMultipleRows(self.m.data,SEASON=s)		#get season wise data
			
			for team in self.m.teams:
				filterd = (self.m.readMultipleRows(season_data,TEAM1 = team))		#get matches according to team in same season from TEAM1
				fil = (self.m.readMultipleRows(season_data,TEAM2=team))		#get matches according to team in same season from TEAM1
				combine  = pandas.concat([filterd,fil])					#get total matches of single team
				match_id = set(combine[self.m.colum[self.m.MATCH_ID]])
				runrate,over,total,total2,over1 = 0,0,0,0,0
				for m in match_id:
					scored = self.d.readMultipleRows(self.d.data,MATCH_ID=m,BATTING_TEAM=team)		#record when team batted
					conceded = self.d.readMultipleRows(self.d.data,MATCH_ID=m,BOWLING_TEAM=team)	#record when team bowled
					if len(scored['TOTAL_RUNS']) > 0 and len(conceded['TOTAL_RUNS']) > 0:		
						batsmen_run = reduce(operator.add,scored['BATSMAN_RUNS'])
						penlty_runs = reduce(operator.add,scored['PENALTY_RUNS'])
						extra_runs = reduce(operator.add,scored['EXTRA_RUNS'])
						no_ball = reduce(operator.add,scored['NOBALL_RUNS'])
						legbye = reduce(operator.add,scored['LEGBYE_RUNS'])
						bye = reduce(operator.add,scored['BYE_RUNS'])
						wide = reduce(operator.add,scored['WIDE_RUNS'])
						over =over + len(set(scored[self.d.colum[self.d.OVER]]))
						total = total + batsmen_run + penlty_runs + extra_runs + no_ball + legbye + bye + wide  #calculate total runs scored

						batsmen_r = reduce(operator.add,conceded['BATSMAN_RUNS'])
						penlty_r = reduce(operator.add,conceded['PENALTY_RUNS'])
						extra_r = reduce(operator.add,conceded['EXTRA_RUNS'])
						no_b = reduce(operator.add,conceded['NOBALL_RUNS'])
						legb = reduce(operator.add,conceded['LEGBYE_RUNS'])
						byee = reduce(operator.add,conceded['BYE_RUNS'])
						widee = reduce(operator.add,conceded['WIDE_RUNS'])
						over1 =over1 + len(set(scored[self.d.colum[self.d.OVER]]))
						total2 = total2 + batsmen_r + penlty_r + extra_r + no_b + legb + byee + widee	#calculate total runs conceded
				
				if (over > 0) or (over1 > 0):	
					runrate = (total/over) - (total2/over1)		#calculate net runrate
				
				final_t.update({team:runrate})				
			result = self.sort_dict(final_t)
			t.add_row([s,result[0][0]])
		print(t)
			
d = RunAll()
#d.firsrtQuery()
#d.secondQuery()
#d.thirdQuery()
#d.fourthQuery()