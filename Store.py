################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Store.py                                                                    #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for external store or nacelle                               #
################################################################################

import math
from Drag.Component import Component

class Store(Component):
    # store class derived from component
    
    def __init__(self, V, h, L_c, S_wet, percent_lam, A_max, config):
        # instatiation of extrenal store or nacell component
        
        Component.__init__(self, V, h, L_c, S_wet, percent_lam)
        
        self.A_max = A_max
        self.config = config
        self.define_Q()
        
    def define_Q(self):
        # define the interference factor based on the configuration
        
        if(self.config.count('on wing') > 0):
            self.Q = 1.5
        elif(self.config.count('near wing') > 0):
            self.Q = 1.3
        else:
            self.Q = 1.0
        
    def get_f(self):
        # calculate the value of f (used to calculate form factor)
    
        return self.L_c / math.sqrt(4/math.pi * self.A_max)
    
    def get_FF(self):
        # calculate the form factor
        
        return 1 + 0.35/self.get_f()
