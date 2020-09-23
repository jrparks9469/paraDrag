################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Flap.py                                                                     #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Flap                                                    #
################################################################################

from Drag.Component import Component

class Flap(Component):
    # flap class derived from component
    
    def __init__(self, span, deflection, S_wet, wing):
        # instatiation of flap component
        
        self.span = span
        self.deflection = deflection
        self.S_wet = S_wet
        self.wing = wing
    
    def get_Cd0(self, S_ref):
        # calculate the contribution of the flap to the parasite drag
        
        Cd0c = 0.0023 * self.span / self.wing.span * self.deflection
        return Cd0c * S_wet / S_ref
