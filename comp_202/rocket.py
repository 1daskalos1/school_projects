# Yanni Klironomos
#261233238

import math as m

#Constants for PART I
FEET_TO_METER = 1/3.28 # [m/ft]: Ratio of 1 meter/3.28 feet
ROCKET_DENSITY = 1.225 # [kg/m^3]: Density of rocket
SMALL_ROCKET_MASS_THRESHOLD = 100000 # [kg]: Mass threshold for small rockets
MEDIUM_ROCKET_MASS_THRESHOLD = 400000  #[kg]: Mass threshold for medium rockets
#Note that large rockets have a mass >= 400000 kg
QUEBEC_TAX = 0.15 # [%] Tax for launching rocket in Mtl

#Constants for PART II
MIN_BOX_WEIGHT = 20 # [kg]
MAX_BOX_WEIGHT = 500 # [kg]
MIN_BOX_VOLUME = 0.125 # [m^3]
ACCELERATION_OF_GRAVITY = 9.81 # [m/s^2]


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
    exact_rocket_mass = rocket_volume(radius, height_cone, height_cyl) \
                        * ROCKET_DENSITY
    rounded_rocket_mass = round(exact_rocket_mass, 2)
    return rounded_rocket_mass
    

def rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time):
    # Obtain the rounded rocket mass from the rocket_mass() fnc
    rounded_rocket_mass = rocket_mass(radius, height_cone, height_cyl)
    
    #The fuel to exit the atmosphere uses the Tsiolkovsky rocket equation
    fuel_to_exit_atmosphere = rocket_mass(radius, height_cone, height_cyl) * \
                             (m.e ** (velocity_i/velocity_e) - 1)
    
   # Fuel needed to reach orbit based on rocket mass
    if rounded_rocket_mass < SMALL_ROCKET_MASS_THRESHOLD:
        small_rocket_fuel_for_orbit = 1360 * time
        fuel_for_orbit = small_rocket_fuel_for_orbit
   
    elif rounded_rocket_mass >= SMALL_ROCKET_MASS_THRESHOLD and \
         rounded_rocket_mass < MEDIUM_ROCKET_MASS_THRESHOLD:
        medium_rocket_fuel_for_orbit = 2000 * time
        fuel_for_orbit =  medium_rocket_fuel_for_orbit
   
    else:
        large_rocket_fuel_for_orbit = 2721 * time
        fuel_for_orbit = large_rocket_fuel_for_orbit
    
    total_fuel_needed = fuel_to_exit_atmosphere + fuel_for_orbit
    rounded_total_fuel = round(total_fuel_needed, 2)
    return rounded_total_fuel

def calculate_cost(radius, height_cone, height_cyl, velocity_e, velocity_i,\
                   time, tax):
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
    
    
    
############################################################################
#PART TWO ##################################################################
############################################################################

def compute_storage_space(radius, height_cyl):
    rounded_storage_space_width = round(m.sqrt(2) * radius, 2)
    rounded_storage_space_length = round(m.sqrt(2) * radius, 2)
    rounded_storage_space_height = round(height_cyl / 2, 2)
      
    return rounded_storage_space_width, \
           rounded_storage_space_length, \
           rounded_storage_space_height





def load_rocket(initial_weight, radius, height_cyl):
    storage_width, storage_length, storage_height = \
                   compute_storage_space(radius, height_cyl)
    volume_storage = storage_width * storage_length * storage_height
    

    max_weight_limit_of_added_items = 0.05 * initial_weight
    max_volume_limit_of_added_items = 0.40 * volume_storage


    if (max_weight_limit_of_added_items == True) \
       or (max_volume_limit_of_added_items == True):
        print("No more items can be added")
        return(round(initial_weight, 2))
    
    elif:
        msg = "Please enter the weight of the next item (type \"Done\" when" \
              "you are done filling the rocket"

        current_volume = 0
        current_weight = 0
    
        while (input(msg) != 'Done') or \
          ((current_volume <= max_volume_limit_of_added_items and\
            current_weight <= max_volume_limit_of_added_items)):
        
            x = input("Enter item width")
            y = input("Enter item length")
            z = input("Enter item height")
            
            volume_box = x * y * z
            current_volume += volume_box
            
            weight_box = float(input(msg))
            current_weight += weight_box
            
            if weight_box < 20 or weight_box > 500 \
               or (current_weight >= max_weight_limit_of_added_items):
                print("Item could not be added")
            
            if (volume_box < 0.125) \
               or (current_volume >= max_volume_limit_of_added_items):
                print("Item could not be added")
                                                       
            




        
def projectile_sim(simulation_time, interval, initial_velocity, angle_rad):
    height = -1/2 * ACCELERATION_OF_GRAVITY * (simulation_time **2)\
             + initial_velocity * sin 
    
def rocket_main():
    print("Welcome to the Rocket Simulation!")
    