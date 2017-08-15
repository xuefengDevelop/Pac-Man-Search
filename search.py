# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    nodeStack = util.Stack()
    visited = []
    path = []
    startNode = (problem.getStartState(),visited,path)
    nodeStack.push(startNode)
    
    "start while loop to find the path"
    
    while  nodeStack.isEmpty() is False:
        (node, visited, path) = nodeStack.pop()
        "check results before go to successors"
        if problem.isGoalState(node):
            return path
        for successor, direction, cost in problem.getSuccessors(node) :
            if successor not in visited:
                newNode = (successor,visited+[successor],path+[direction])
                nodeStack.push(newNode)


    return None
    util.raiseNotDefined()






def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    "the only change here is that queue structure, so we can search from 1 layer to another layer"
    "not like Stack, we pop and search all the way to the goal node, but we need to expand more to find"
    "the goal node"
    "use queue to store all the same layer node,and always pop first node in the layer"
    nodeQueue = util.Queue()
    visited = []
    path = []
    startNode = (problem.getStartState(),path)
    nodeQueue.push(startNode)
    
    "start while loop to find the path"
    
    while  nodeQueue.isEmpty() is False:
        node, path = nodeQueue.pop()

        if problem.isGoalState(node):
            return path
        visited.append(node)
        for successor, direction, cost in problem.getSuccessors(node) :
            if successor not in visited:
                visited.append(successor)
                newNode = (successor,path+[direction])
                nodeQueue.push(newNode)

    return None
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    "we use PriorityQueue data structure, 'smart queue' "
    "struture and help us to find the lower cost of action"
    "use PriorityQueue to detect which route is shortest, and pop the shortest route"
   
    nodePriorityQueue = util.PriorityQueue()
    visited = []
    path = []
    totalCost = 0
    startNode =(problem.getStartState(),path)
    nodePriorityQueue.push((startNode),totalCost)
    
    "start while loop to find the correct path"
    
    while  nodePriorityQueue.isEmpty() is False:
        node,path = nodePriorityQueue.pop()
        
        visited.append(node)
        
        if problem.isGoalState(node):
            return path
        
        for successor, direction, cost in problem.getSuccessors(node) :
            if successor not in visited:
                visited.append(successor)
                newNode =(successor,path + [direction])
                nodePriorityQueue.push(newNode,problem.getCostOfActions(path + [direction]))
            if problem.isGoalState(successor):
                newNode =(successor,path + [direction])
                nodePriorityQueue.push(newNode,problem.getCostOfActions(path + [direction]))

    return None

    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    "it is very similar to UCS, just change the totalcost to the heuristic + cost  "
    nodePriorityQueue = util.PriorityQueue()
    visited = []
    path = []
    totalCost = heuristic(problem.getStartState(),problem)
    startNode =(problem.getStartState(),path)
    nodePriorityQueue.push((startNode),totalCost)
    
    "start while loop to find the correct path"
    
    while  nodePriorityQueue.isEmpty() is False:
        node,path = nodePriorityQueue.pop()
        
        visited.append(node)
        
        if problem.isGoalState(node):
            return path
        for successor, direction, cost in problem.getSuccessors(node) :
            if successor not in visited:
                visited.append(successor)
                newNode =(successor,path+[direction])
                totalCost = problem.getCostOfActions(path + [direction]) + heuristic(successor,problem)
                nodePriorityQueue.push(newNode,totalCost)
            if problem.isGoalState(successor):
                newNode =(successor,path + [direction])
                totalCost = problem.getCostOfActions(path + [direction]) + heuristic(successor,problem)
                nodePriorityQueue.push(newNode,totalCost)


    return None

    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
