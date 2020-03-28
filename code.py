# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how toa read it.
ipl_data = np.genfromtxt(path,delimiter=',',skip_header=True,dtype=str)

# Number of unique matches 


 # How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.
unique_matches = len(set(ipl_data[:,0]))
print("The no. of unique matches in dataset is",unique_matches)
# Number of unique teams
team_1 = set(ipl_data[:,3])

team_2 = set(ipl_data[:,4])

unique_teams = team_1.union(team_2)
print("The set of unique teams that played matches are",unique_teams)
 # this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras
extras = ipl_data[:,17]

extras_int = map(int,extras)
print("The Sum of extras in all deliveries",sum(extras_int))
 # An exercise to make you familiar with indexing and slicing up within data.

# Delivery number when a given player got out

 # Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
given_batsman = 'ST Jayasuriya'
is_out = ipl_data[:,-3] == given_batsman
output_data = ipl_data[:,[11,-2]]
print("Array of deliveries is\n",output_data[is_out])
# Number of times Mumbai Indians won the toss
given_team = 'Mumbai Indians'
toss_winner_data = ipl_data[:,5]
toss_winner_given_team = toss_winner_data == given_team
filtered_match_number = ipl_data[toss_winner_given_team,0]
print('The Number of Matches',given_team,'won is',len(set(filtered_match_number)))
 # this exercise will help you get the statistics on one particular team

# Filter record where batsman scored six and player with most number of sixex
runs_data = ipl_data[:,-7].astype(int)
runs_data_mask = runs_data == 6
filtered_sixes_record = ipl_data[:,-10][runs_data_mask]
from collections import Counter
batsmen_sixes = Counter(filtered_sixes_record)
print(batsmen_sixes)
print(max(batsmen_sixes,key = batsmen_sixes.get))
 # An exercise to know who is the most aggresive player or maybe the scoring player 







