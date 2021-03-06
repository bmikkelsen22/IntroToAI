import sys
import os.path
import game
from collections import deque
from queue import PriorityQueue

def iddfs(initial_state, goal_state):
	node_count = 0
	max_depth = 0
	
	while True: 
		frontier = deque()
		explored = {}
		depth = 0
		frontier.append(initial_state) 
		max_depth += 1

		while frontier:
			current_state = frontier.pop()
			if current_state == goal_state:
				print("nodes expanded: " + str(node_count)) 
				return current_state
			else:
				if current_state.depth >= max_depth:
					continue #skip this node, too deep

				node_count += 1
				explored[current_state] = True
				
				one_chicken = game.moveChicken(current_state)
				if one_chicken.ok() == True:
					if one_chicken not in explored and one_chicken not in frontier:
						frontier.append(one_chicken)
				
				two_chicken = game.moveTwoChickens(current_state)
				if two_chicken.ok() == True:
					if two_chicken not in explored and two_chicken not in frontier:
						frontier.append(two_chicken)

				one_wolf = game.moveWolf(current_state)
				if one_wolf.ok() == True:
					if one_wolf not in explored and one_wolf not in frontier:
						frontier.append(one_wolf)

				wolf_and_chicken = game.moveWolfAndChicken(current_state)
				if wolf_and_chicken.ok():
					if wolf_and_chicken not in explored and wolf_and_chicken not in frontier:
						frontier.append(wolf_and_chicken)

				two_wolves = game.moveTwoWolves(current_state)
				if two_wolves.ok():
					if two_wolves not in explored and two_wolves not in frontier:
						frontier.append(two_wolves)



def dfs(initial_state, goal_state):
		frontier = deque()
		explored = {}
		node_count = 0

		frontier.append(initial_state) 

		while True:
				if not frontier:
						print("nodes expanded: " + str(node_count))
						return None
				else:
						current_state = frontier.pop()
						if current_state == goal_state:
								print("nodes expanded: " + str(node_count)) 
								return current_state
						else:
								node_count += 1
								explored[current_state] = True
								
								one_chicken = game.moveChicken(current_state)
								if one_chicken.ok() == True:
										if one_chicken not in explored and one_chicken not in frontier:
												frontier.append(one_chicken)
								
								two_chicken = game.moveTwoChickens(current_state)
								if two_chicken.ok() == True:
										if two_chicken not in explored and two_chicken not in frontier:
												frontier.append(two_chicken)

								one_wolf = game.moveWolf(current_state)
								if one_wolf.ok() == True:
										if one_wolf not in explored and one_wolf not in frontier:
											frontier.append(one_wolf)

								wolf_and_chicken = game.moveWolfAndChicken(current_state)
								if wolf_and_chicken.ok():
										if wolf_and_chicken not in explored and wolf_and_chicken not in frontier:
											frontier.append(wolf_and_chicken)

								two_wolves = game.moveTwoWolves(current_state)
								if two_wolves.ok():
										if two_wolves not in explored and two_wolves not in frontier:
											frontier.append(two_wolves)


def astar(initial_state, goal_state):
		frontier = PriorityQueue()
		explored = {}
		node_count = 0

		initial_state.heuristic(goal_state)
		frontier.put(initial_state) 

		while True:
				if frontier.empty():
						print("nodes expanded: " + str(node_count))
						return None
				else:
						current_state = frontier.get()
						if current_state == goal_state:
								print("nodes expanded: " + str(node_count)) 
								return current_state
						else:
								node_count += 1
								explored[current_state] = True
								
								one_chicken = game.moveChicken(current_state)
								if one_chicken.ok() == True:
										if one_chicken not in explored and one_chicken not in frontier.queue:
												one_chicken.heuristic(goal_state)
												frontier.put(one_chicken)
								
								two_chicken = game.moveTwoChickens(current_state)
								if two_chicken.ok() == True:
										if two_chicken not in explored and two_chicken not in frontier.queue:
												two_chicken.heuristic(goal_state)
												frontier.put(two_chicken)

								one_wolf = game.moveWolf(current_state)
								if one_wolf.ok() == True:
										if one_wolf not in explored and one_wolf not in frontier.queue:
												one_wolf.heuristic(goal_state)
												frontier.put(one_wolf)

								wolf_and_chicken = game.moveWolfAndChicken(current_state)
								if wolf_and_chicken.ok():
										if wolf_and_chicken not in explored and wolf_and_chicken not in frontier.queue:
												wolf_and_chicken.heuristic(goal_state)
												frontier.put(wolf_and_chicken)

								two_wolves = game.moveTwoWolves(current_state)
								if two_wolves.ok():
										if two_wolves not in explored and two_wolves not in frontier.queue:
												two_wolves.heuristic(goal_state)
												frontier.put(two_wolves)



def bfs(initial_state, goal_state):
		frontier = deque()
		explored = {}
		node_count = 0

		frontier.append(initial_state) 

		while True:
				if not frontier:
						print("nodes expanded: " + str(node_count)) 
						return None
				else:
						current_state = frontier.popleft()
						if current_state == goal_state:
								print("nodes expanded: " + str(node_count)) 
								return current_state
						else:
								node_count += 1
								explored[current_state] = True
								
								one_chicken = game.moveChicken(current_state)
								if one_chicken.ok() == True:
										if one_chicken not in explored and one_chicken not in frontier:
												frontier.append(one_chicken)
								
								two_chicken = game.moveTwoChickens(current_state)
								if two_chicken.ok() == True:
										if two_chicken not in explored and two_chicken not in frontier:
												frontier.append(two_chicken)

								one_wolf = game.moveWolf(current_state)
								if one_wolf.ok() == True:
										if one_wolf not in explored and one_wolf not in frontier:
											frontier.append(one_wolf)

								wolf_and_chicken = game.moveWolfAndChicken(current_state)
								if wolf_and_chicken.ok():
										if wolf_and_chicken not in explored and wolf_and_chicken not in frontier:
											frontier.append(wolf_and_chicken)

								two_wolves = game.moveTwoWolves(current_state)
								if two_wolves.ok():
										if two_wolves not in explored and two_wolves not in frontier:
											frontier.append(two_wolves)

def printSoln(solution):
	i = 0
	curr = solution
	solnString = ""
	while curr.pred:
		i += 1
		solnString = str(curr) + "\n" + solnString
		curr = curr.pred
	solnString = str(curr) + "\n" + solnString

	print("nodes in solution: %d" % i)
	print(solnString)
	return solnString

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
		
		mode = sys.argv[3]
		output_file = open(sys.argv[4], "w+")
		initial_file = open(sys.argv[1], "r")
		goal_file = open(sys.argv[2], "r")
		if initial_file.mode == 'r' and goal_file.mode == 'r':
				initial = initial_file.readlines()
				initialnums = [] 
				for i in initial:
					i = i.rstrip() 
					initialnums += i.split(",")
					initialnums = list(map(int, initialnums)) 
					#initial_state = Game() 
					#put initialnums into the game state
				
				initial_state = game.Game(initialnums[1], initialnums[0], initialnums[2] == 1, initialnums[4], initialnums[3], initialnums[5] == 1) 

				goal = goal_file.readlines()
				goalnums = []
				for i in goal:
					i = i.rstrip() 
					goalnums += i.split(",")
					goalnums = list(map(int, goalnums)) 
					#put goalnums into the game goal state

				
				goal_state = game.Game(goalnums[1], goalnums[0], goalnums[2] == 1, goalnums[4], goalnums[3], goalnums[5] == 1) 
				
				if mode == 'bfs':
						solution = bfs(initial_state, goal_state)
				elif mode == 'dfs':
						solution = dfs(initial_state, goal_state)
				elif mode == 'iddfs':
					solution = iddfs(initial_state, goal_state)
				elif mode == 'astar':
					solution = astar(initial_state, goal_state)
				
				if solution:
					solnString = printSoln(solution)
					output_file.write(solnString)
				else:
					print("no solution")
main() 

