# Yanni Klironomos
#261233238

import math as m

FEET_TO_METER = 1/3.28 #Ratio of 1 meter/3.28 feet
ROCKET_DENSITY = 1.225 #Density of rocket in kg/m^3

def feet_to_meter(length_in_ft):
    length_in_m = length_in_ft * FEET_TO_METER
    rounded_length_in_m = round(length_in_m, 2)
    return rounded_length_in_m
    

def rocket_volume(radius, height_cone, height_cyl):
    cone_volume = m.pi * radius ** 2 * (height_cone/3)
    cylinder_volume = m.pi * (radius)** 2 * height_cyl
    exact_combined_volume = cone_volume + cylinder_volume
    rounded_combined_volume = round(exact_combined_volume, 2)
    return rounded_combined_volume

def rocket_area(radius, height_cone, height_cyl):
    area_cone = m.pi * radius * \
                (radius + m.sqrt(height_cone ** 2 + radius ** 2))
    area_cyl = 2 * m.pi * radius * (height_cyl + radius)
    area_circle = m.pi * radius ** 2
    exact_area_rocket = area_cone + area_cyl - 2 * area_circle
    rounded_area_rocket = round(exact_area_rocket, 2)
    return rounded_area_rocket

def rocket_mass(radius, height_cone, height_cyl):           
    exact_rocket_mass = rocket_volume(radius, height_cone, height_cyl) * 1.225
    rounded_rocket_mass = round(exact_rocket_mass, 2)
    return rounded_rocket_mass
    

def rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time):
    tsiolkovsky_rocket_eqn = rocket_mass(radius, height_cone, height_cyl) * \
                             (m.e ** (velocity_i/elocity_e) - 1)
    if rounded_rocket_mass < 100000:
        return 1360
    if rounded_rocket_mass >= 100000 and rounded_rocket_mass < 400000:
        return 2000
    return 2721 #there is no need for if-else since each case returns a value
    total_mass  = rocket_mass()
    return total_fuel_needed