# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
from util import Stack
from util import Queue
from util import PriorityQueue

# from searchAgents import manhattanHeuristic
import searchAgents

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state(successor is kind of state and GameState!!!!), 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    path = Stack()
    explored = []
    def depthSearch(state):        
        
        explored.append(state)#record that this node is explored
        
        if problem.isGoalState(state): #check if goal
            return True  #return to the higher level of the "depthSearch" 
        
        suc = problem.getSuccessors(state)  #get a list of triples(successor, action, stepCost)   
                                            #the successor is the next state
                                            #e.g. [((5, 4), 'South', 1), ((4, 5), 'West', 1)] 
#         suc = [triple for triple in suc if not triple[0] in explored]
#         for triple in suc:
#             explored.append(triple[0])
                
        for triple in suc: # for every triple(successor, action, stepCost)  
            if explored.__contains__(triple[0]):#check if the state is searched
                continue           
            if depthSearch(triple[0]): #the recursive
                path.push(triple[1])    # if the lower level return true, record the action
                return True            # which means this level also has found goal state
         
        return False   

    depthSearch(problem.getStartState()) #The first call
    
    route = []
    while (not path.isEmpty()):
        action = path.pop()
        #print action
        route.append(action) #return a list of action
    return route
    
            

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    queue = Queue()
    explored = []
    
    queue.push((problem.getStartState(), [])) #what in the queue is the (state, path)
    explored.append(problem.getStartState())
    while not queue.isEmpty():
        tuple = queue.pop()
        currentPath = tuple[1]
        
        
        if problem.isGoalState(tuple[0]):
            return currentPath
                    
        suc = problem.getSuccessors(tuple[0])
        for triple in suc:
            if explored.__contains__(triple[0]):
                continue
            explored.append(triple[0])
            path = currentPath + [triple[1]]
            queue.push((triple[0], path))
  

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    queue = PriorityQueue()
    explored = []
    
    queue.push((problem.getStartState(), [], 0), 0) #what in the queue is the (state, path,cost)
    explored.append(problem.getStartState())
    while not queue.isEmpty():
        tuple = queue.pop()
        #print tuple[0], tuple[2]
        currentPath = tuple[1]
        #print currentPath
        currentCost = tuple[2]
                
        if problem.isGoalState(tuple[0]):
            return currentPath
                    
        suc = problem.getSuccessors(tuple[0])
        for triple in suc:
            if explored.__contains__(triple[0]):
                continue
            if not problem.isGoalState(triple[0]):
                explored.append(triple[0])
            path = currentPath + [triple[1]]
            cost = currentCost + triple[2]
            queue.push((triple[0], path, cost), cost)
            
                
           
            
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    #print 'A* is called'
    queue = PriorityQueue()
    explored = []
      
    queue.push((problem.getStartState(), [], 0), 0) #what in the queue is the (state, path,cost)
    explored.append(problem.getStartState())
    while not queue.isEmpty():
        tuple = queue.pop()
        currentPath = tuple[1]
        currentCost = tuple[2]
                  
        #explored.append(tuple[0])
                  
        if problem.isGoalState(tuple[0]):
            return currentPath
                      
        suc = problem.getSuccessors(tuple[0])
        for triple in suc:
            if explored.__contains__(triple[0]):
                continue
            if not problem.isGoalState(triple[0]):
                explored.append(triple[0])
            path = currentPath + [triple[1]]
            cost = currentCost + triple[2]
            fn = cost + heuristic(triple[0], problem)
            queue.push((triple[0], path, cost), fn)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


