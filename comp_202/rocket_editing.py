# Yanni Klironomos
#261233238

import math as m

# GLOBAL CONSTANTS FOR PART 1

FEET_TO_METER = 1/3.28 # [m/ft]: Ratio of 1 meter/3.28 feet
ROCKET_DENSITY = 1.225 # [kg/m^3]: Density of rocket

SMALL_ROCKET_MASS_THRESHOLD = 100000 # [kg]: Mass threshold for small rockets
MEDIUM_ROCKET_MASS_THRESHOLD = 400000  #[kg]: Mass threshold for medium rockets
#Note: Large rockets have a mass >= 400000 kg

SMALL_ROCKET_FUEL_BURN_RATE = 1360 # [kg/s]: Burn rate of small-mass rocket
MEDIUM_ROCKET_FUEL_BURN_RATE = 2000 # [kg/s]: Burn rate of medium-mass rocket
LARGE_ROCKET_FUEL_BURN_RATE = 2721 # [kg/s]: Burn rate of large-mass rocket


QUEBEC_TAX = 0.15 # [%] Tax for launching rocket in Mtl



def feet_to_meter(length_in_ft):
    """
    Converts an inputted length fom feet into meters
    
    Parameter:
        length_in_feet: a positive float [unit: feet]
    Returns:
        rounded_length_in_m: a positive float (rounded to 2 decimal places)
                            [unit: meters]

    Examples:
    >>> feet_to_meter(2.22)
    0.68
    >>> feet_to_meter(0)
    0.0
    >>> feet_to_meter(10.0)
    3.05
    
    """
    length_in_m = length_in_ft * FEET_TO_METER
    rounded_length_in_m = round(length_in_m, 2)
    return rounded_length_in_m

def rocket_volume(radius, height_cone, height_cyl):
    """
    Calculates the volume of a given rocket. The rocket is modelled by a cone
    stacked on a cylinder
    
    Parameter:
        radius: a positive float [unit: meters]
        height_cone: a positive float [unit: meters]
        height_cyl: a positive float [unit: meters]
        
    Returns:
        rounded_combined_volume: a positive float rounded to 2 decimal places
                                 [unit: meters^3]

    Examples:
        >>> rocket_volume(1.0, 2.0, 3.0)
        11.52
        >>> rocket_volume(12.5, 14.0, 15.0)
        9653.85
        >>> rocket_volume(0.0, 5.0, 10.0)
        0.0
    
    """
    cone_volume = m.pi * (radius ** 2) * (height_cone / 3)
    cylinder_volume = m.pi * (radius) ** 2 * height_cyl
    rounded_combined_volume = round(cone_volume + cylinder_volume, 2)
    return rounded_combined_volume

def rocket_area(radius, height_cone, height_cyl):
    """
    Calculates the total surface area of a rocket.
    
    Parameter:
        radius: a positive float [unit: meters]
        height_cone: a positive float [unit: meters]
        height_cyl: a positive float [unit: meters]
    Returns:
        rounded_area_rocket: a positive float (rounded to 2 decimal places)
                            [unit: meters^2]

    Examples:
    >>> rocket_area(1.1, 2.8, 4.9)
    48.06
    >>> rocket_area(0.0, 12.8, 8.9)
    0.0
    >>> rocket_area(11.6, 28.4, 17.7)
    2830.77
    
    """
    area_cone = m.pi * radius * \
                (radius + m.sqrt(height_cone ** 2 + radius ** 2))
    area_cyl = 2 * m.pi * radius * (height_cyl + radius)
    area_circle = m.pi * radius ** 2
    exact_area_rocket = area_cone + area_cyl - 2 * area_circle
    rounded_area_rocket = round(exact_area_rocket, 2)
    return rounded_area_rocket

def rocket_mass(radius, height_cone, height_cyl):
    """
    Calculates the total rocket mass using an approximate density of
    1.225 kg/m^3.
    
    Parameter:
        radius: a positive float [unit: meters]
        height_cone: a positive float [unit: meters]
        height_cyl: a positive float [unit: meters]
    Returns:
        rounded_rocket_mass: a positive float (rounded to 2 decimal places)
                            [unit: kg]

    Examples:
    >>> rocket_mass(1.0, 2.4, 6.8)
    29.25
    >>> rocket_mass(1.0, 0.0, 11.1)
    42.72
    >>> rocket_mass(12.9, 14.6, 12.4)
    11057.93
    """
    
    exact_rocket_mass = rocket_volume(radius, height_cone, height_cyl) \
                        * ROCKET_DENSITY
    rounded_rocket_mass = round(exact_rocket_mass, 2)
    return rounded_rocket_mass
    
def rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time):
    """
    Calculates the total rocket fuel by summing the rocket fuel needed to exit
    a planet's atmosphere (using the Tsiolkovsky's eqn) and the amount of fuel
    needed for the rest of the trip (orbit).
    
    Parameter:
        radius: a positive float [unit: meters]
        height_cone: a positive float [unit: meters]
        height_cyl: a positive float [unit: meters]
        velocity_e: a positive float [exhaust velocity; unit: meters/seconds]
        velocity_i: a positive float [initial velocity; unit: meters/seconds]
        time: a positive float [unit: seconds]
    Returns:
        rounded_total_fuel: a positive float (rounded to 2 decimal places)
                            [unit: kg]

    Examples:
    >>> rocket_mass(1.0, 2.4, 6.8)
    29.25
    >>> rocket_mass(1.0, 0.0, 11.1)
    42.72
    >>> rocket_mass(12.9, 14.6, 12.4)
    11057.93
    """
    
    # Obtain the rounded rocket mass from the rocket_mass() fnc
    rounded_rocket_mass = rocket_mass(radius, height_cone, height_cyl)
    
    #The fuel to exit the atmosphere uses the Tsiolkovsky rocket equation
    fuel_to_exit_atmosphere = rocket_mass(radius, height_cone, height_cyl) * \
                             (m.e ** (velocity_i/velocity_e) - 1)
    
   # Fuel needed to reach orbit based on rocket mass
    if rounded_rocket_mass < SMALL_ROCKET_MASS_THRESHOLD:
        small_rocket_fuel_for_orbit = SMALL_ROCKET_FUEL_BURN_RATE * time
        fuel_for_orbit = small_rocket_fuel_for_orbit
   
    elif rounded_rocket_mass >= SMALL_ROCKET_MASS_THRESHOLD and \
         rounded_rocket_mass < MEDIUM_ROCKET_MASS_THRESHOLD:
        medium_rocket_fuel_for_orbit = MEDIUM_ROCKET_FUEL_BURN_RATE * time
        fuel_for_orbit =  medium_rocket_fuel_for_orbit
   
    else:
        large_rocket_fuel_for_orbit = LARGE_ROCKET_FUEL_BURN_RATE * time
        fuel_for_orbit = large_rocket_fuel_for_orbit
    
    total_fuel_needed = fuel_to_exit_atmosphere + fuel_for_orbit
    rounded_total_fuel = round(total_fuel_needed, 2)
    return rounded_total_fuel


def calculate_cost(radius, height_cone, height_cyl, velocity_e, velocity_i,\
                   time, tax):
    """
    Caqlculates the approximate cost of building and launching the rocket.
    
    Parameter:
        radius: a positive float [unit: meters]
        height_cone: a positive float [unit: meters]
        height_cyl: a positive float [unit: meters]
        velocity_e: a positive float [exhaust velocity; unit: meters/seconds]
        velocity_i: a positive float [initial velocity; unit: meters/seconds]
        time: a positive float [unit: seconds]
        tax: boolean 
    Returns:
        rounded_total_price: a positive float (rounded to 2 decimal places)
                            [unit: $]

    Examples:
    >>> calculate_cost(42.0, 69.0, 28.0, 40.0, 0.0, 12.0, True)
    303997.5
    >>> calculate_cost(11.1, 12.9, 19.2, 84.3, 64.7, 11.1, False)
    182148.14
    >>> calculate_cost(800.0, 200.0, 300.0, 400.0, 900.0, 1100.0, True)
    53825232708.63
    """
    
    cost_of_materials = rocket_area(radius, height_cone, height_cyl) * 5
    cost_of_fuel = \
                 rocket_fuel(radius, height_cone, height_cyl, \
                             velocity_e, velocity_i, time) * 6.1
    price_before_tax = cost_of_materials + cost_of_fuel
     
    if tax == True:  
        total_price = price_before_tax * QUEBEC_TAX + price_before_tax
    else:
        total_price = price_before_tax
    rounded_total_price = round(total_price, 2)
    return rounded_total_price
    