################################################################################
# Aerodynamic methods - 1.0                                                    #
# /drag_in.py                                                                  #
# Author: John Parks                                                           #
# Date: 4/15/2019                                                              #
#                                                                              #
# Module for reading input files                                               #
################################################################################

from Drag.Aircraft import Aircraft
from Drag.Component import Component
from Drag.Diverter import Diverter
from Drag.Flap import Flap
from Drag.Foil import Foil
from Drag.Fuselage import Fuselage
from Drag.Spoiler import Spoiler
from Drag.Store import Store
    
def define_diverter(v, h, data):
    # define a diverter component give list of data
    
    L_c = float(data[0])
    S_wet = float(data[1])
    percent_lam = float(data[2])
    d = float(data[3])
    config = data[4]
    
    return Diverter(v, h, L_c, S_wet, percent_lam, d, config)

def define_flap(aircraft, data):
    # define a flap given list of data
    
    span = float(data[0])
    deflection = float(data[1])
    S_wet = float(data[2])
    wing = aircraft.components['wing']
    
    return Flap(span, deflection, S_wet, wing)

def define_foil(v, h, data):
    # define a foil given a list of data
    
    L_c = float(data[0])
    S_wet = float(data[1])
    percent_lam = float(data[2])
    t_c = float(data[3])
    x_c = float(data[4])
    sweep = float(data[5])
    span = float(data[6])
    config = data[7]
    
    return Foil(v, h, L_c, S_wet, percent_lam, 
                     t_c, x_c, sweep, span, config)

def define_fuselage(v, h, data):
    # define a fuselage component given list of data
    
    L_c = float(data[0])
    S_wet = float(data[1])
    percent_lam = float(data[2])
    A_max = float(data[3])
    u = float(data[4])
    config = data[5]
    
    return Fuselage(v, h, L_c, S_wet, percent_lam, A_max, u, config)

def define_spoiler(aircraft, data):
    # define a spoiler given a list of data
    
    A_base = float(data[0])
    wing = aircraft.components['wing']
    
    return Spoiler(A_base, wing)
    
def define_store(v, h, data):
    # define a store given a list of data
    
    L_c = float(data[0])
    S_wet = float(data[1])
    percent_lam = float(data[2])
    A_max = float(data[3])
    
    return Store(v, h, L_c, S_wet, percent_lam, A_max)

def read_aircraft_file():
    # read an .csv file containing aircraft data

    # open file
    file_name = input('File Name --> ')
    data = open(file_name, 'r')

    # read the aircraft name and flight conditions
    name = data.readline()[:-1].replace(',', '')
    data.readline()
    v = float(data.readline().split(',')[1])
    h = float(data.readline().split(',')[1])
    S_ref = float(data.readline().split(',')[1])

    # define the aircraft
    aircraft = Aircraft(name, v, h, S_ref)

    # read each component
    data.readline()
    for component in data:
        local_data = component.split(',')
        name = local_data[0]
        
        # create the component
        if(name.count('diverter') > 0):
            local_component = define_diverter(v, h, local_data[1:])
        elif(name.count('flap') > 0):
            local_component = define_flap(aircraft, local_data[1:])
        elif(name.count('wing') + name.count('stab') > 0):
            local_component = define_foil(v, h, local_data[1:])
        elif(name.count('fuselage') > 0):
            local_component = define_fuselage(v, h, local_data[1:])
        elif(name.count('spoiler') > 0):
            local_component = define_spoiler(aircraft, local_data[1:])
        else:
            local_component = define_store(v, h, local_data[1:])
        
        # add component to the aircraft
        aircraft.add_component(name, local_component)
    
    return aircraft
