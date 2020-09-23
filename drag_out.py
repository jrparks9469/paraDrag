####################################n############################################
# Aerodynamic methods - 1.0                                                    #
# /drag_in.py                                                                  #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Module for writing output files                                              #
################################################################################

from Drag.Aircraft import Aircraft
from Drag.Component import Component
from Drag.Diverter import Diverter
from Drag.Flap import Flap
from Drag.Foil import Foil
from Drag.Fuselage import Fuselage
from Drag.Spoiler import Spoiler
from Drag.Store import Store
from . import aero

def write_output(aircraft):
    # write results to a csv file

    # open the file to write
    output = open('./drag_results/{}_{}_{:.3f}_out.csv'.format(aircraft.name, aircraft.h,
                                                 aircraft.get_mach()), 'w')
    
    # write data to the file
    output.write('{}-OUT\n\n'.format(aircraft.name)) # title
    
    output.write('Altitude,{}\n'.format(aircraft.h)) # altitude
    output.write('Mach,{:.4f}\n'.format(aircraft.get_mach())) # mach#
    output.write('Viscosity,{:.8f}\n'.format(aero.atm_dynamic_viscosity(aircraft.h)))
    output.write('Temperature,{:.1f}\n'.format(aero.atm_temp(aircraft.h)))
    output.write('Rho,{:.8f}\n\n'.format(aero.atm_density(aircraft.h))) # rho
    
    output.write('{},{},{},{},{},{}\n'.format('component','CD0','FF','Q',
                                              '%contribution','Re')) # header
    # data corresponding to header                                           
    for c in aircraft.components.keys():
        comp = aircraft.components[c]
        output.write('{},{:.8f},{:.4f},{:.2f},{:.2f},{:.0f}\n'.format(c,
                                            comp.get_Cd0(aircraft.S_ref),
                                            comp.get_FF(),
                                            comp.Q,
                                            aircraft.list_percent()[c],
                                            comp.get_reynolds()))
                                            
    # total parasite drag                                        
    output.write('\nCd0-Total,{:.8f}'.format(aircraft.total_Cd0()))
