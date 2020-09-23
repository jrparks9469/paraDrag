################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Diverter.py                                                                 #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Flow Diverter                                           #
################################################################################

from Drag.Component import Component

class Diverter(Component):
    # diverter class derived from component
    
    def __init__(self, V, h, L_c, S_wet, percent_lam, d, config):
        # instatiation of flow diverter component
        
        Component.__init__(self, V, h, L_c, S_wet, percent_lam)
        
        self.d = d
        self.Q = 1.0
        self.config = config
    
    def get_FF(self):
        # calculate the form factor
        
        if(self.config.count('single') > 0):
            return 1 + 2*self.d/self.L_c
        else:
            return 1 + self.d/self.L_c
