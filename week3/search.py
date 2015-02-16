# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import sys
from game import Directions
from util import PriorityQueue
import collections

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
        successor to the current state, 'action' is the action
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


def trySearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """

    print "initialNode: ", problem.getStartState()
    print "initialSuccessors: ", problem.getSuccessors(problem.getStartState())
    north = problem.getSuccessors(problem.getStartState())[0][0]
    print "northSuccessors: ", problem.getSuccessors(north)

    # from game import Directions
    s = Directions.STOP
    return [s]


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
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    startState = problem.getStartState();
    if problem.isGoalState(startState):
        return []   

    actions = []
    customActions = {}
    closedNodes = []
    currPriority = sys.maxint;

    fringe = PriorityQueue();
    customPush(fringe, startState, None, currPriority)

    while fringe.isEmpty() == False:

        popTuple = customPop(fringe, customActions)
        node = popTuple[0]
        nodePriority = popTuple[1]
        customActions = popTuple[2]
        if problem.isGoalState(node):
            actions = getActionsFromCustomActions(customActions)
            print("Actions Found: ", actions)
            return actions

        if node not in closedNodes:
            closedNodes.append(node)
            successors = problem.getSuccessors(node)
            currPriority = nodePriority - 1
            for childNode, direction, cost in successors:
                customPush(fringe, childNode, direction, currPriority) 

    print "Search Failed"
    return []

def customPush(fringe, node, direction, priority):
    fringe.push((node, priority, direction), priority)

def customPop(fringe, customActions):
    nodeTuple = fringe.pop()
    node = nodeTuple[0]
    priority = nodeTuple[1]
    action = nodeTuple[2]

    if action != None:
        customActions[priority] = action

    return (node, priority, customActions)

def getActionsFromCustomActions(customActions):

    actionsArray = sorted(customActions.items())
    actionStrings = []
    for priority, actionString in actionsArray:
        actionStrings.append(actionString)

    actionStrings.reverse()

    actions = []
    for actionStr in actionStrings: 
        action = getActionFromActionString(actionStr)
        actions.append(action)
    return actions

def getActionFromActionString(actionString):
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST
    z = Directions.STOP

    if actionString == "North":
        return n
    elif actionString == "South":
        return s
    elif actionString == "East":
        return e
    elif actionString == "West":
        return w
    else:
        return z

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
