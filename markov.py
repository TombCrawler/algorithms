'''
                 |    A    |    E    |        — Each element denotes the probability weight of the edge                        
     +——+——+——+                                 connecting the two corresponding vertices                                      

      |    A    |   0.6   |   0.4  |          — 0.4 is the probability for state A to go to state E and 0.6 is the probability to remain at the same state  

      |    E    |   0.7   |   0.3   |         — 0.7 is the probability for state E to go to state A and 0.3 is the probability  

     +——+——+——+                                 to remain at the same state  '''

# let's import our library
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
