#
# searcher.py (Final project)
#
# Description: classes for objects that perform state-space search on Eight 
# Puzzles.  
# Date: 8/10/24
# Name: Benjamin Kim 
# email: benjt@bu.edu


import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        '''the Searcher constructor'''
        #Initialize the data members.
        self.depth_limit = depth_limit
        self.states = []
        self.num_tested = 0

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def should_add(self, state):
        '''returns True if the called Searcher should add state to its list 
        of untested states, and False otherwise.'''
        #If Searcher has a depth limit and state is beyond it, or the state
        #creates a cycle, the method returns False.
        if (self.depth_limit != -1 and state.num_moves > self.depth_limit or 
            state.creates_cycle() == True):
            return False
        
        #Else, the method returns True.
        else:
            return True

    def add_state(self, new_state):
        '''takes a single State object called new_state and adds it to the 
        Searcher‘s list of untested states.'''
        self.states.append(new_state)
        
    def add_states(self, new_states):
        '''takes a list State objects called new_states, and processes the   
        elements of new_states one at a time'''
        #For loop that iterates through each state.
        for state in new_states:
            
            #If self.should_add(state) is true, add the state.
            if self.should_add(state) == True:
                self.add_state(state)

    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        '''performs a full random state-space search, stopping when the goal 
        state is found or when the Searcher runs out of untested states.'''
        #Add the init_state parameter to self.states.
        self.add_state(init_state)
        
        #Attribute the next state we're testing to the variable test
        #and add its successors to self.states. Also increment num_tested
        #by 1.
        test = self.next_state()
        self.num_tested += 1
        succ = test.generate_successors()
        self.add_states(succ)
        
        #If test is already the goal state and there's no need for extra
        #searching, increment num_tested by 1 and return test.
        if test.is_goal() == True:
            self.num_tested += 1
            return test
        
        #Else, while test.is_goal is false, keep testing until the method
        #reaches a state that is the goal state or runs out of 
        #states to test.
        else:
            while test.is_goal() == False:
                #print('test:', test, 'num_tested:', self.num_tested)
                self.num_tested += 1
                test = self.next_state()
                if test.is_goal() == True:
                    return test
                else:
                    succ = test.generate_successors()
                    self.add_states(succ)
                
### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    '''a blueprint for objects that perform breadth first searches instead 
    of random searches.'''
    
    def next_state(self):
        '''returns the state that has been in the list of untested
        states the longest (i.e. the first state that's still in the list).'''
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    '''a blueprint for searcher objects that perform depth-first searches.'''
    
    def next_state(self):
        '''returns the state that has been in the list of untested
        states the shortest (i.e. the first state in the list).'''
        s = self.states[-1]
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    '''a heuristic function that counts the number of misplaced 
    tiles.'''
    return state.board.num_misplaced()

def h2(state):
    return state.board.total_distance()

### Add your other heuristic functions here. ###

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, depth_limit, heuristic):
        '''the GreedySearcher constructor.'''
        #Code that calls the superclass constructor.
        super().__init__(depth_limit)
        
        #Initialize the special data member.
        self.heuristic = heuristic 

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

    def priority(self, state):
        '''takes a state object called state, and returns its priority.'''
        #How the method calculates priority.
        priority = -1 * self.heuristic(state)
        
        return priority

    def add_state(self, state):
        '''adds the sublist [priority, state] to the list of untested 
        states.'''
        self.states.append([self.priority(state), state])

    def next_state(self):
        '''chooses one of the states in self.states with the highest
        priority.'''
        #max will choose one of the sublists with the highest priority.
        s = max(self.states)
        
        #Remove that sublist after we identify it.
        self.states.remove(s)
        
        #Return only the state component of the sublist.
        return s[1]

### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
        
    def priority(self, state):
        '''takes a state object called state, and returns its priority.'''
        return -1 * (self.heuristic(state) + state.num_moves)

if __name__ == '__main__':
    
    #__init__ and __repr__ test cases.
    searcher1 = Searcher(-1)
    print(searcher1)
    
    #should_add test cases.
    b1 = Board('142358607')
    s1 = State(b1, None, 'init')  # initial state
    searcher1 = Searcher(-1)  # no depth limit
    searcher1.add_state(s1)
    searcher2 = Searcher(1)   # depth limit of 1 move!
    searcher1.add_state(s1)
    b2 = b1.copy()
    b2.move_blank('left')
    s2 = State(b2, s1, 'left')    # s2's predecessor is s1
    print(searcher1.should_add(s2))
    print(searcher2.should_add(s2))
    b3 = b2.copy()
    b3.move_blank('right')    
    s3 = State(b3, s2, 'right')
    print(searcher1.should_add(s3))
    
    #add_states test cases.
    b = Board('142358607')
    s = State(b, None, 'init')
    searcher = Searcher(-1)
    searcher.add_state(s)
    print(searcher.states)
    succ = s.generate_successors()
    print(succ)
    print('---------')
    searcher.add_states(succ)             
    print(searcher.states)
    print('---------')
    succ2 = succ[-1].generate_successors()
    print(succ2)
    print(searcher.should_add(succ2[-1]))
    print(succ2[1].creates_cycle())
    searcher.add_states(succ2)
    print(searcher.states)
    print('---------')
    
    #find_solution test case.
    b = Board('142305678')
    s = State(b, None, 'init')   
    print(s)
    searcher = Searcher(-1)
    print(searcher)
    print(searcher.find_solution(s))
    print(searcher)
    print(searcher.num_tested)
    print('---------')
    
    #next_state test case (BFSearcher)
    b = Board('142358607')       
    s = State(b, None, 'init')
    print(s)
    bfs = BFSearcher(-1)
    bfs.add_state(s)
    print(bfs.next_state()) 
    succ = s.generate_successors()
    print(succ)
    bfs.add_states(succ)
    print(bfs.next_state())
    print(bfs.next_state())
    print('---------')
    
    #next_state test case (DFSearcher)
    b = Board('142358607')       
    s = State(b, None, 'init')
    print(s)
    dfs = DFSearcher(-1)
    dfs.add_state(s)
    print(dfs.next_state()) 
    succ = s.generate_successors()
    print(succ)
    dfs.add_states(succ)
    print(dfs.next_state())
    print(dfs.next_state())
    
    #GreedySearcher test cases.
    b = Board('142358607')       
    s = State(b, None, 'init')
    g = GreedySearcher(-1, h1)
    g.add_state(s)
    succ = s.generate_successors()
    g.add_state(succ[1])
    print(g.states)
    print(g.next_state())
    print(g.states)
    print('---------')
    
    #AStarSearcher test cases.
    b = Board('142358607')       
    s = State(b, None, 'init')
    a = AStarSearcher(-1, h1)  
    print(a)
    a.add_state(s)
    succ = s.generate_successors()
    a.add_state(succ[1])
    print(a.states)
    print(a.next_state())
    print(a.states)
    print(a)