"""Asymmetric"""

from copy import deepcopy
import numpy as np
from collections import Counter
import pickle
from sympy.solvers import solve
from sympy import nsolve
from sympy import Symbol
from numpy import sqrt as sqrt

def get_stat(database, dim=100):
    """
    Get Statistics of database
    """
    BB = 0
    BD = 0
    DD = 0
    Co = 0
    nB = 0
    I = 0
    nonI = 0
    B = np.zeros(dim)
    C = np.zeros(dim)
    D = np.zeros(dim)
    Bmain = np.zeros(dim)
    Dmain = np.zeros(dim)
    BBdepth = np.zeros(dim)
    BDdepth = np.zeros(dim)
    DDdepth = np.zeros(dim)

    for i in range(len(database)):
        n = database[i]
        BB += n.features['branch branch'][0]
        BD += n.features['branch die'][0]
        DD += n.features['die die'][0]
        Co += n.features['Npassnode'][0]
        B += n.make_fixed_length_vec(n.features['branch depth'], dim)
        C += n.make_fixed_length_vec(n.features['continue depth'], dim)
        D += n.make_fixed_length_vec(n.features['dead depth'], dim)
        Bmain += n.make_fixed_length_vec(n.features['main branch depth'], dim)
        Dmain += n.make_fixed_length_vec(n.features['main dead depth'], dim)
        nB += n.features['Nbranch'][0] - (n.features['initial with branch'][0]+1)
        I += n.features['initial with branch'][0]+1
        nonI += n.features['all non trivial initials'][0]
        BBdepth += n.make_fixed_length_vec(n.features['branch branch depth'], dim)
        BDdepth += n.make_fixed_length_vec(n.features['branch die depth'], dim)
        DDdepth += n.make_fixed_length_vec(n.features['die die depth'], dim)
    I = float(I)
    nB = float(nB)
    return float(BB), float(BD), float(DD), float(Co), B.astype(float), C, D, Bmain, Dmain, nB, I, nonI, BBdepth, BDdepth, DDdepth

def asy_ratio(BB, BD, DD):
    return float(BD*BD)/float(4*BB*DD)
