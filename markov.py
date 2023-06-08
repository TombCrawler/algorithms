'''
                 |    A    |    E    |        — Each element denotes the probability weight of the edge                        
     +——+——+——+                                 connecting the two corresponding vertices                                      

      |    A    |   0.6   |   0.4  |          — 0.4 is the probability for state A to go to state E and 0.6 is the probability to remain at the same state  

      |    E    |   0.7   |   0.3   |         — 0.7 is the probability for state E to go to state A and 0.3 is the probability  

     +——+——+——+                                 to remain at the same state  '''

import scipy.linalg
import numpy as np

state = ["A", "E"]

MyMatrix = np.array([[0.6, 0.4], [0.7, 0.3]])
print("\nMyMatrix")
print(MyMatrix)

# Simulating a random walk on our Markov chain
# with 20 steps. 
n = 20

# decide which state to start with
StartingState = 0
CurrentState = StartingState

# printing the stating state using state
# dictionary
print(state[CurrentState], "--->", end=" ")

while n-1:
	CurrentState = np.random.choice([0, 1], p=MyMatrix[CurrentState])
	
	# printing the path of random walk
	print(state[CurrentState], "--->", end=" ")
	n -= 1
print("stop")

# Let us find the stationary distribution of our
# Markov chain by Finding Left Eigen Vectors
MyValues, left = scipy.linalg.eig(MyMatrix, right=False, left=True)

print("left eigen vectors = \n", left, "\n")
print("eigen values = \n", MyValues)

# Pi is a probability distribution so the sum of
# the probabilities should be 1 To get that from
# the above negative values we just have to normalize
pi = left[:, 0]
pi_normalized = [(x/np.sum(pi)).real for x in pi]
x, y = pi_normalized
print(f"Get 1: x + y = {x + y}")


'''
1,
The statistical system contains a finite number of states.
  meaning that there is a limited and countable number of 
  distinct possible outcomes or configurations that the system can be in.
  In statistics, a system refers to a process or phenomenon under consideration,
  and its states represent the different possible values or configurations that 
  the system can exhibit. For example, if you're flipping a fair coin, the states of 
  the system could be "heads" or "tails," resulting in a finite number of two states.

2,
The states are mutually exclusive and collectively exhaustive.
   Mutually exclusive: 
   This means that the states or categories within a system 
   do not overlap or intersect. In other words, if one state occurs, then the other states 
   cannot occur simultaneously. Each state is unique and independent of the others. 
   For example, when flipping a fair coin, the states "heads" and "tails" are 
   mutually exclusive because if the coin lands on heads, it cannot be tails at the same time.

   Collectively exhaustive: 
   This means that the states or categories within a system cover all possible 
   outcomes or possibilities. When considering all the states together, there are 
   no other potential outcomes that are not accounted for. The set of states represents 
   a complete and comprehensive description of the system. Going back to 
   the coin example, "heads" and "tails" are collectively exhaustive 
   because they encompass all possible outcomes of a coin flip.

3,
The transition probability from one state to another state is constant over time

Overall,   
Markov processes are fairly common in real-life problems and Markov chains can be 
easily implemented because of their memorylessness property. Using Markov chain can 
simplify the problem without affecting its accuracy.
Let us take an example to understand the advantage of this tool, suppose my friend is 
suggesting to have a meal. I may say that I do not want a pizza as I have that one hour ago. 
But Is it appropriate if I say that I do not want a pizza because I have it two months ago? 
That means in this case, my probability of picking a meal is entirely dependent on 
my immediately preceding meal. It is the effectiveness of the Markov Chain.
'''