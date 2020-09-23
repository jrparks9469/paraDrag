################################################################################
# Aircraft Component Parasite Drag - 1.0                                       #
# /Component.py                                                                #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Class definition for Component                                               #
################################################################################

from . import aero

class Component:
    # Generic class for component of an aircraft in a given flight condition
    
    def __init__(self, V, h, L_c, S_wet, percent_lam):
        # instatiation of aircraft component
    
        self.V = V
        self.h = h
        self.L_c = L_c
        self.Q = 1.0
        self.S_wet = S_wet
        self.percent_lam = percent_lam
        
        self.rho = aero.atm_density(self.h)
        self.mu = aero.atm_dynamic_viscosity(self.h)
        
    def get_reynolds(self):
        # calculate the reynolds number for the component
        
        return aero.reynolds(self.rho,
                             self.V,
                             self.L_c,
                             self.mu)
    
    def get_mach(self):
        # calculate the mach number for the component
        
        return aero.mach(self.V,
                         self.h)
    
    def get_cf(self):
        # calculate the friction coefficients for the component
        
        lam = aero.cf_lam(self.get_reynolds())
        turb = aero.cf_turb(self.get_reynolds(),
                            self.get_mach())
                            
        cf = lam*self.percent_lam + turb*(1-self.percent_lam)
        return cf
        
    def get_Cd0(self, S_ref):
        # calculate the contribution of this component to the parasite drag
        # given the reference area
        
        return self.get_cf() * self.get_FF() * self.Q * self.S_wet / S_ref
