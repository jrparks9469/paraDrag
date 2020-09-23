################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Spoiler.py                                                                  #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Spoiler                                                 #
################################################################################

from . import aero
from Drag.Component import Component

class Spoiler(Component):
    # spoiler class derived from component
    
    def __init__(self, A_base, wing):
        # instatiation of spoiler component
        
        self.A_base = A_base
        self.wing = wing
    
    def get_Cd0(self, S_ref):
        # calculate the contribution of the flap to the parasite drag
        
        mach = aero.mach(self.wing.V, self.wing.h)
        
        drag_area = (0.139 + 0.419 * (mach - 0.161)**2) * self.A_base
        return drag_area / S_ref
