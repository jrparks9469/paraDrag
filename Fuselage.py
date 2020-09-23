################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Fuselage.py                                                                 #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Fuselage                                                #
################################################################################

import math
from Drag.Component import Component

class Fuselage(Component):
    # fueslage class derived from component
    
    def __init__(self, V, h, L_c, S_wet, percent_lam, A_max, u, config):
        # instatiation of fuselage component
        
        Component.__init__(self, V, h, L_c, S_wet, percent_lam)
        
        self.A_max = A_max
        self.Q = 1.0
        self.u = u
        self.config = config
        
    def get_f(self):
        # calculate the value of f (used to calculate form factor)
    
        return self.L_c / math.sqrt(4/math.pi * self.A_max)
    
    def get_FF(self):
        # calculate the form factor
        
        f = self.get_f()
        FF = 1 + 60/(f**3) + f/400
        
        if(self.config.count('square') > 0):
            return 1.4 * FF
        elif(self.config.count('boat') > 0):
            return 1.5 * FF
        elif(self.config.count('two-piece') > 0):
            return 1.4 * FF
        else:
            return FF
        
    def get_Cd0(self, S_ref):
        # calculate the contribution of the fuselage to the parasite drag
        # taking the aft upsweep into account
        
        drag_area = 3.83 * self.u**2.5 * self.A_max
        upsweep_drag_coeff = drag_area / S_ref
        Cd0c = self.get_cf() * self.get_FF() * self.Q * self.S_wet / S_ref
        
        return Cd0c + upsweep_drag_coeff
