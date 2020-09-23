################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Aircraft.py                                                                 #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Aircraft                                                #
################################################################################

from . import aero

class Aircraft:
    # aircraft class definition
    
    def __init__(self, name, V, h, S_ref):
        # instantiation of aircraft class
        
        self.name = name
        self.V = V
        self.h = h
        self.S_ref = S_ref
        self.components = {}
        
    def get_mach(self):
        # calculates the mach number for the aircraft
        
        return aero.mach(self.V, self.h)
        
    def add_component(self, name, component):
        # adds specified component to list of components
        
        self.components[name] = component
    
    def total_Cd0(self):
        # adds the parasite drag from each component
        
        Cd0 = 0
        for c in self.components.keys():
            Cd0 += self.components[c].get_Cd0(self.S_ref)
            
        return Cd0
    
    def list_contributions(self):
        # lists contributions to parasite drag
        
        contrib = {}
        for c in self.components.keys():
            contrib[c] = self.components[c].get_Cd0(self.S_ref)
        
        return contrib
            
    def list_percent(self):
        # list percent contributions to parasite drag
        
        Cd0 = self.total_Cd0()
        contrib = {}
        for c in self.components.keys():
            contrib[c] = self.components[c].get_Cd0(self.S_ref)/Cd0*100
        
        return contrib
