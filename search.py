import random
import util, queue

class SearchProblem:


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

    def expand(self, state):

        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
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

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):

    "*** YOUR CODE HERE ***"
    #declaring queue for storing frontiers
    frontier=queue.Queue()
    
    #explored = dict()
    explored=dict()

    #stroring current state in a variable
    position = problem.getStartState()
    
    vertex = {"from":None,"to":None,"current_pos":position}
    frontier.put(vertex)

    #till frontier is not empty iterate to find path
    
    util.raiseNotDefined()






# Abdellah Bouchama 191931025176

# backtracking implementation
# python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs





# a function to check if the next suggested move will lead to a visited location
def is_not_visited(list, posx, posy):
    if(list):
        for i in range(len(list)):
            # changed from if((list[i][0] == posx) & (list[i][1] == posy)): to  if(list[i] == [posx, posy]):
            if(list[i] == [posx, posy]):
                return False
    else: 
        return True
    return True


def greedy_s(problem):
    # two empty arrays to store the final path ands the visited points
    path = []
    visited_points = []

    # X and Y position = the first position
    posX = problem.startState[0]
    posY = problem.startState[1]

    ifs_list = []

    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    e = Directions.EAST
    n = Directions.NORTH

    cpt = 0
    
    for i in range (100000):
        # break the loop is our position = the goal's position
        if((posX == problem.goal[0]) & (posY == problem.goal[1])):
            print("done")
            break

        # periorities:
        # south => west => east => north
        # the goal will still be found if we mix up the direction's order

        # deleted isValidMove() function and replaced it with a simple condition 

        # start 
        ifs_list = [([posX, posY-1], s), ([posX-1, posY], w), ([posX+1, posY], e), ([posX, posY+1], n)] # [s, w, e, n] with its directions
        #random.shuffle(ifs_list)
        value = random.randint(0, 3)
        # print(value)

        d = random.choice(ifs_list)

        condition = d[0]
        result = d[1] 

        
        if((not problem.walls[condition[0]][condition[1]])):
            if(is_not_visited(visited_points, condition[0], condition[1])):
                visited_points.append([posX,posY])
                path.append(result)
                posX = condition[0]
                posY = condition[1]
            else:
                cpt = cpt + 1
            
        
        if(cpt == 1):
            cpt = 0
            # if dead End pop last visited position
            print("\n\ndead end!!\n\n")
            visited_points.pop()

    print(i)

        
        # else:
        #     # if dead End pop last visited position
        #     print("\n\ndead end!!\n\n")
        #     visited_points.pop()


        # if((not problem.walls[posX][posY+1]) & is_not_visited(visited_points, posX, posY+1)):    # north
        #     visited_points.append([posX,posY])
        #     path.append(n)
        #     posY = posY+1
        # elif((not problem.walls[posX][posY-1]) & is_not_visited(visited_points, posX, posY-1)):    # south
        #     visited_points.append([posX,posY])
        #     path.append(s)
        #     posY = posY-1
        # elif((not problem.walls[posX-1][posY]) & is_not_visited(visited_points, posX-1, posY)):      # west
        #     visited_points.append([posX,posY])
        #     path.append(w)
        #     posX = posX-1
        # elif((not problem.walls[posX+1][posY]) & is_not_visited(visited_points, posX+1, posY)):    # east
        #     visited_points.append([posX,posY])
        #     path.append(e)
        #     posX = posX+1
        # else:
        #     # if dead End pop last visited position
        #     print("\n\ndead end!!\n\n")
        #     visited_points.pop()
            
    #print(path)
    # return path
    return path

    util.raiseNotDefined()







def nullHeuristic(state, problem=None):

    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = greedy_s
