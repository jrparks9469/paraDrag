################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Foil.py                                                                     #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Airfoils                                                #
################################################################################

import math
from . import aero
from Drag.Component import Component

class Foil(Component):
    # foil class derived from component
    
    def __init__(self, V, h, L_c, S_wet, percent_lam,
                 t_c, x_c, sweep, span, config):
        # instatiation of foil component
        
        Component.__init__(self, V, h, L_c, S_wet, percent_lam)
        
        self.t_c = t_c
        self.x_c = x_c
        self.sweep = sweep
        self.span = span
        self.config = config
        self.define_Q()
        
    def define_Q(self):
        # define the interference factor based on the configuration
        
        if(self.config.count('wing') > 0):
            if(self.config.count('low') > 0 and \
               self.config.count('unfilletted') > 0):
                self.Q = 1.25
            else:
                self.Q = 1.0
        elif(self.config.count('tail') > 0):
            if(self.config.count('h ') > 0):
                self.Q = 1.08
            elif(self.config.count('v ') > 0):
                self.Q = 1.03
            else:
                self.Q = 1.04
        else:
            self.Q = 1.0
    
    def get_FF(self):
        # calculate the form factor
        
        x_c = self.x_c
        t_c = self.t_c
        sweep = self.sweep
        M = aero.mach(self.V, self.h)
        
        return (1 + 0.6/x_c*t_c + 100*(t_c**4)) * \
               (1.34*(M**0.18)*(math.cos(sweep)**0.28))
