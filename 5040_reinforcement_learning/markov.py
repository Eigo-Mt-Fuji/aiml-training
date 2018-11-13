
import numpy as np
import random
random.seed(0)

state_transition = np.array(
                    [[0, 0, 0, 0.3, 5],
                    [0, 1, 0, 0.7, -10],
                    [0, 0, 1, 1, 5],
                    [1, 0, 1, 1, 5],
                    [1, 2, 0, 0.8, 100],
                    [1, 1, 0, 0.2, 1]]
                    )
terminals = [2]

# output can done actions
def actions(state):
    A = state_transition[(state_transition[:, 0] == state)]
    return  np.unique(A[:,2])

# return reward
def R(state, action, after_state, terminals=[2]):
    if state in terminals:
        return 0

    X = state_transition[(state_transition[:,0] == state) & (state_transition[:,1] == after_state) & (state_transition[:,2] == action)]
    return X[0, 4]
# return case and probability
def T(state, action):

    if (state in terminals):
        return [(0, 2)]

    X = state_transition[(state_transition[:, 0] == state)&(state_transition[:, 2] == action)]

    A = X[:, [3, 1]]
    return [tuple(A[i, :]) for i in range(A.shape[0])]
