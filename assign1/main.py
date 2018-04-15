import sys
import os.path

#print("sup")

def main():

		if len(sys.argv) != 5:
			print("Not enough command line arguments. Please try again.")
			sys.exit()
		#print("Yay, enough arguments.")
		if not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
				print("A file does not exist. Please try again.")
				sys.exit()
		if sys.argv[3] not in ('bfs', 'dfs', 'iddfs', 'astar'):
			print("Mode incorrect. Please try again.")
			sys.exit() 
		
		output_file = open(sys.argv[4], "w+")
		initial_file = open(sys.argv[1], "r")
		goal_file = open(sys.argv[2], "r")
		if initial_file.mode == 'r' and goal_file.mode == 'r':
				print("cool, lets parse these files.") 
				initial = initial_file.readlines()
				for i in initial:
					print(i) 
					i = i.rstrip() 
					initialnums = i.split(",")
					initialnums = list(map(int, initialnums)) 
					print(initialnums) 
					#put initialnums into the game state

				goal = goal_file.readlines()
				for i in goal:
					print(i) 
					i = i.rstrip() 
					goalnums = i.split(",")
					goalnums = list(map(int, goalnums)) 
					print(goalnums) 
					#put goalnums into the game goal state

main() 

