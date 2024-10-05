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
                                                       
            