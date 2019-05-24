from Matches import Matches
import pandas as pandas
class Deliveries:
	
	final_teams = {}
	m = Matches()


	'''This method displays top 4 team of 2016 and 2017 who choose to field after winnig toss'''
	def firsrtQuery(self):

		season  = [2016,2017]

		for s in season:
			data = (self.m.readSingleRow(self.m.data,SEASON = s))	#fetch dataframe according to season
			fdata = (self.m.readSingleRow(data,TOSS_DECISION='field'))   #filer data from 'data'. fetch tems who choose to field
		
			for team in self.m.teams:
				win_toss = (self.m.readSingleRow(fdata,TOSS_WINNER=team))	#filter data on fdata. Teams who win toss.
				winner = (self.m.readSingleRow(win_toss,WINNER=team))		#filter data on toss_winning team. Team who won the toss and match both.
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

d = Deliveries()
d.firsrtQuery()