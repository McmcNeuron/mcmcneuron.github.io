"""tree utility"""

import numpy as np
from numpy import linalg as LA
import math
from scipy.sparse import csr_matrix
from copy import deepcopy
from numpy.linalg import inv
from sklearn import preprocessing

def branch_order(parent_index):
    """
    Set the branching numbers. It gives bach a vector with the length of
    number of nodes such that in each index of this vector the branching
    number of this node is written: terminal = 0, passig = 1, branching = 2
    dependency:
        nodes_list
    """
    branch_order = np.zeros(len(parent_index))
    unique, counts = np.unique(parent_index[1:], return_counts=True)
    branch_order[unique] = counts
    return branch_order

def dendogram_depth(self, parent_index):
    ancestor_matrix = np.arange(len(parent_index))
    ancestor_matrix = np.expand_dims(ancestor_matrix, axis=0)
    up = np.arange(len(parent_index))
    while(sum(up) != 0):
        up = parent_index[up]
        ancestor_matrix = np.append(ancestor_matrix,
                                    np.expand_dims(up, axis=0),
                                    axis=0)
    return np.sign(ancestor_matrix[:-1, :]).sum(axis=0)
