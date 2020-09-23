################################################################################
# Aerodynamic methods - 1.0                                                    #
# /aero.py                                                                     #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Module for aerodynamic methods                                               #
################################################################################

import math

# CONSTANTS

# gas constant
R = 1716 # ft^2/s^2 R

# heat capacity ratio
gamma = 1.4

#FUNCTIONS

def reynolds(rho, v, l, mu):
    # Calculates Reynolds number
    # Given: density, freestream, characteristic length, viscosity
    
    return rho*v*l/mu
    
def cf_lam(re):
    # Calculates skin friction for laminar flow
    # Given: Reynolds number
    
    return 1.328/math.sqrt(re)
    
def cf_turb(re, m):
    # Calculates skin friction for turbulent flow
    # Given: Reynolds number, Mach number
    
    return 0.455 / ((math.log10(re)**2.58) * (1+0.144*(m**2))**0.65)
    
def atm_temp(h):
    # Calculates temperature of standard atmosphere
    # Given: altitude
    
    if(h < 36089):
        return (59 - 0.00356616*h) + 459.67
    elif(h < 82345):
        return 389.97
    else:
        return (-205.05 + 0.00164*h) + 459.67
        
def atm_pressure(h):
    # Calculates pressure of standard atmosphere
    # Given: altitude
    
    if(h < 36089):
        return 2116.22 * (atm_temp(h)/518.67)**5.25592
    elif(h < 65617):
        return 472.676 * math.exp(-4.80638e-5*(h-36089.2))
    else:
        return 51.97 * (atm_temp(h)/389.98)**-11.388
        
def atm_density(h):
    # Calculates density of standard atmosphere
    # Given: altitude
    
    return atm_pressure(h)/(R * atm_temp(h))

def atm_dynamic_viscosity(h):
    # Calculates the dynamic viscosity of standard atmosphere
    # Given: altitude
    
    mu_0 = 3.737e-7
    temp = atm_temp(h)
    temp_0 = atm_temp(0)
    
    return mu_0 * (temp/temp_0)**1.5 * ((temp_0 + 198.72)/(temp + 198.72))

def a(h):
    # Calculates speed of sound (dry air)
    # Given: altitude
    
    return math.sqrt(gamma * R * atm_temp(h))
    
def mach(v, h):
    # Calculate the mach number
    # Given: freestream velocity, altitude
    
    return v/a(h)

def dynamic_pressure(v, h):
    # Calculates the dynamic pressure at velocity
    # Given: altitude, airspeed
    
    rho = atm_density(h)
    
    return 0.5 * rho * v**2
