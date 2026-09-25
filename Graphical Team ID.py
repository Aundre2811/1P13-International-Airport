import turtle

def passenger_data():
 
    file = open("passenger_data_v2.txt", "r")
    passenger_data_list = []
    for line in file:
        temp_passenger_list = []
        for item in line.strip().split(","):
            temp_passenger_list.append(item)

        passenger_data_list.append(temp_passenger_list)

    return passenger_data_list


def fleet_data():
    
    """
    This function takes the data from the fleet data CSV file and 
    ouputs a 2D list of all the different flight as well as a bunch of
    different important pieces of information about each flight, such as
    the destination and the max baggage weight.
    """
    
    # Open the file to read the data
    file = open("fleet_data.txt", "r")
    # Create an empty list to store all the lists in
    output_list = []
    for line in file:
        # Make a sub-list for each row
        temp_list = []
        # Split the line and append it to the sub-list
        for item in line.strip().split(","):
            temp_list.append(item)
 
        # Append the sub-list to the main list
        output_list.append(temp_list)
 
    return output_list


## Alex ##
def overweight(passenger_info, fleet_info):
    """
    This function takes information from the passenger data and fleet data
    programs and compares the weight of each person's bag to the max weight
    accepted on the flight, returning 2 lists, the first of each flight,
    with the number of overweight bags onboard, and the second with each
    person who owns an overweight bag, along with how much more the bag
    weighs than is accepted.
    """
    # Creating empty lists to be the outputted lists    
    count_for_plane = []
    exceed_list = []

    for flight in fleet_info:

        # Take out the items needed from the list and assign them to variables
        model, gate, destination, max_weight = flight[0], flight[4], flight[5], flight[7]

        # Create a variable to count the number of overweight passengers
        count = 0

        for passenger in passenger_info:

            # Take out the items needed from the list and assign them to variables
            first_name, initial, passenger_gate, passenger_destination, weight = (
                passenger[0], passenger[1], passenger[2], passenger[3], passenger[6]
                ) 

            # Make sure the passenger is on the right plane
            if passenger_gate == gate and passenger_destination == destination:

                # Check if the passenger is overweight
                if weight > max_weight:
                    count += 1

                    # Calculate how for overweight the bag is
                    excess_weight = round(float(weight) - float(max_weight), 1)

                    # Append the customer's info to the main list
                    exceed_list.append([first_name, initial, gate, excess_weight])

        # Append the flight's info to the main list
        count_for_plane.append([model, count])

    return count_for_plane, exceed_list


exceeded_count, exceeded_passenger_details = overweight(passenger_data(), fleet_data())







## Aundre ##

def daily_data(passenger_data_list):
    """
    Function to determine number of business and economy passengers using each gate with the use of 2D list.
    The parameter passed is the passenger data list which contains the information about gates and the number
    of business and economy passengers. The function finally returns a 2D list which contains gate numbers as
    well as the corresponding number of economy and business passengers passing through those specific gates
    """
 
    # Defining empty list for daily data
    daily_data = []

    # Loops through passenger information in passenger_data_list
    for passenger_info in passenger_data_list:
        gate_number= passenger_info[2] # Checks for the gate number of the passenger
        seat = passenger_info[4] # Checks whether the passenger is business or economy
        gate_exists = False # Initializes boolean value false, to check if the gate is already in the daily data list

        for entry in daily_data: # Loops through each list representing each gate inside the daily data list
            if entry[0] == gate_number: # Checks if the gate number being checked is already contained in the daily data list

                if seat == 'B':  # Checks if passenger is in business
                    entry[1] += 1 # Adds 1 to the total number of business passengers at that gate
 
                else:  # If the passenger is in economy 
                    entry[2] += 1 # Adds 1 to the total number of economy passengers at that gate
                gate_exists = True # Defines gate_exists as true (meaning the gate is already in daily data list)

                break # Exits loop
            
        if not gate_exists: # Checks if the gate is not in daily data list

            if seat == 'B':
                 daily_data.append([gate_number, 1, 0]) # Appends new list to daily data list for new gate with one business passenger

            else: # If passenger is in economy
                 daily_data.append([gate_number, 1, 0]) # Appends new list to daily data list for new gate with one economy passenger

    return daily_data # returns daily_data







## Navia ##
def oversold():
    
    """
    This function Takes information from the daily_data, passenger_data and 
    fleet_data functions to find the ammount of over sold buisness and econpmy 
    seats for each flight
    """
    
    ## Go through each list in fleet_data and get the flight number, plane model and number of business and economy seats available
    oversold_b_list = []
    oversold_e_list = []
    
    # Get data from fleet_data and daily_data
    fleet_Data = fleet_data()
    daily_Data = daily_data(passenger_data())
    
    # Go through each list in fleet_data and get the flight number, plane model and number of buissens and econaly seata availible
    for lists in fleet_Data:
       flight_num = lists[4]
       plane_model = lists[0]
       e_seats_avl = lists[2]
       b_seats_avl = lists[1]
       
       # Go through each list in daily_data and check what flight number in daily_data matches the flight number in fleet_data
       for lists in daily_Data:
           flight_num_match = lists[0]
           if flight_num == flight_num_match:
               
               # Collect number of buisness and economy seats sold
               e_seats_sold = lists [2]
               b_seats_sold = lists[1]
               temp_list = []
               oversold_e = e_seats_sold - int(e_seats_avl)
               oversold_b = b_seats_sold - int(b_seats_avl)
               
               # If there is a negative amount of 
               if oversold_e < 0:
                   oversold_e = 0
               if oversold_b < 0:
                   oversold_b = 0 
               
                   
               # Add buissnes oversold to list
               temp_list.append(plane_model)
               temp_list.append(oversold_b)
               oversold_b_list.append(temp_list)
               
               # Add econamy oversold to list
               temp_list = []
               temp_list.append(plane_model)
               temp_list.append(oversold_e)
               oversold_e_list.append(temp_list)
    return oversold_b_list, oversold_e_list

## Minh ##
def layover(passenger_data, fleet_data):
    """
    Function to get the number of layover passenger once they reach their destination on each plane and 
    their infomation into 2 2D lists

    Parameters
    ----------
    passenger_data : 2D Lists
        A 2D list containning all the passengers' data (first/last name, destination, gate, status,etc...).
    fleet_data : 2D Lists
        A 2D list containning all the planes' data (plane model, seats, gate, destination, etc...).

    Returns
    -------
    plane_data : 2D List
        Lists of all the plane model and number of passengers laying over from the plane.
    individual_data : 2D List
        Lists containing first and last name of passengers laying over .

    """
    plane_data = []
    individual_data = []
    
    #Getting the Gate of all the plane into the plane data for easier comparasion 
    for plane in fleet_data:
        plane_gate = []#Temperary list to append to the main plane_data list
        plane_gate.append(plane[4])
        plane_gate.append(0)
        plane_data.append(plane_gate)
        
    #Check each passenger if they have layover status 
    for passenger in passenger_data:
        if passenger[7] == "Layover":
            gate = passenger[2]
            #Based on the passenger's gate, add one (number of layover passenger) to that plane
            plane_data[find_plane(plane_data, gate)][1] += 1
            
            #Append to that passenger's data to individual data
            individual_data.append([passenger[0], passenger[1], gate])
            
    change_gate_to_plane_model(plane_data, fleet_data)
            
    return plane_data, individual_data
    
def find_plane(plane_data, gate):
    """
    Function that find the index of the plane in the plane_data list based on its gate

    Parameters
    ----------
    plane_data : 2D List
        List of all planes and their gate in index 0.
    gate : String
        The gate that is getting searched.

    Returns
    -------
    i : Integer
        index of the plane in the plan_data list.

    """
    # Go through the list, return and exit when found the plane with the correct gate
    for i in range(len(plane_data)):
        if plane_data[i][0] == gate:
            return i
        
def change_gate_to_plane_model(plane_data, fleet_data):
    """
    Change all the plane's gate into its corresponding plane model (mutating the list given in the parameter itself)

    Parameters
    ----------
    plane_data : 2D list
        2D list of all the planes' gate and number of layover passenger.
    fleet_data : 2D list
        List of all the planes' model and their corresponding gate.

    Returns
    -------
    None.

    """
    for i in range(len(plane_data)):
        plane_data[i][0] = fleet_data[i][0]
        
### Ameera ###
def time_delay():
    """
    This function processes passenger and fleet data to determine the number 
    of late layover passengers for each plane model and returns the results 
    in a nested list.
    """
    
    ## Load passenger and fleet data
    passengers = passenger_data()  ## 2D list of passenger info
    fleet = fleet_data()  ## 2D list of fleet info

    ## List to store late layover data for each plane
    big_list = []

    for fleet_item in fleet:
        ## Start with an empty list for this plane's data
        little_list = []

        ## Extract plane model and gate/flight ID from fleet_data
        plane_model = fleet_item[0]  ## Plane model is at index 0
        gate = fleet_item[4]  ## Flight ID or gate is at index 4

        ## Initialize a counter for late layover passengers
        total_layover = 0

        ## Check each passenger to see if they match this plane's gate and are late/laying over
        for passenger in passengers:
            if passenger[2] == gate and passenger[7] == "Layover" and passenger[6] == "Late":
                total_layover += 1

        ## Add plane model and total late layovers to the list
        little_list.append(plane_model)
        little_list.append(total_layover)
        big_list.append(little_list)

    return big_list


def graphical_teamID():
    """
    This function uses the turtle graphics module to visually display 
    plane data, including the plane model, oversold seats (business 
    and economy), overweight bags, layover passengers, and late layover 
    passengers. Each plane is represented by a rectangle with the 
    corresponding data displayed below it.
    """


    ## Get data from required functions
    oversold_business, oversold_economy = oversold()  ## Lists for oversold seats
    overweight_data, _ = overweight(passenger_data(), fleet_data())  ## List of overweight bag counts
    layover_data, _ = layover(passenger_data(), fleet_data())  ## List of layover passengers
    late_layover_data = time_delay()  ## List of late layover passengers

    ## Initialize the turtle
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    ## Set up the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)

    ## Starting positions and dimensions
    x_start = -670  ## Starting x-coordinate
    y_start = 200   ## Starting y-coordinate
    width = 170     ## Rectangle width
    height = 50     ## Rectangle height
    x_spacing = 15  ## Horizontal spacing between rectangles

    ## Main loop to draw 7 repetitions
    x = x_start  ## Initial x-coordinate
    for i in range(len(fleet_data())):
        
        plane_model = fleet_data()[i][0]
        oversold_b = oversold_business[i][1] 
        oversold_e = oversold_economy[i][1]
        overweight_count = overweight_data[i][1] if i < len(overweight_data) else 0
        layover_count = layover_data[i][1] if i < len(layover_data) else 0
        late_layover_count = late_layover_data[i][1] if i < len(late_layover_data) else 0
        
        ## Draw rectangle
        t.penup()
        t.goto(x, y_start)
        t.pendown()
        t.fillcolor("lightcyan")
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
        t.end_fill()

        ## Write plane model inside the rectangle
        t.penup()
        t.goto(x + 10, y_start - height / 2)
        t.write(plane_model, align="left", font=("Arial", 12, "normal"))

        ## Write Oversold Business below the rectangle
        t.goto(x, y_start - height - 20)
        t.write(f"Oversold Business: {oversold_b}", align="left", font=("Arial", 8, "normal"))

        ## Write Oversold Economy below
        t.goto(x, y_start - height - 40)
        t.write(f"Oversold Economy: {oversold_e}", align="left", font=("Arial", 8, "normal"))

        ## Write Overweight Bags below
        t.goto(x, y_start - height - 60)
        t.write(f"Overweight Bags: {overweight_count}", align="left", font=("Arial", 8, "normal"))

        ## Write Layover below
        t.goto(x, y_start - height - 80)
        t.write(f"Layover: {layover_count}", align="left", font=("Arial", 8, "normal"))

        ## Write Late Layover below
        t.goto(x, y_start - height - 100)
        t.write(f"Late Layover: {late_layover_count}", align="left", font=("Arial", 8, "normal"))

        ## Move x-coordinate for the next rectangle
        x += width + x_spacing

    ## Wait for the user to close the window
    screen.mainloop()


''' RUNNING THE CODE '''
passenger_info = passenger_data()
fleet_info = fleet_data()

overweight_count, overweight_passenger_details = overweight(passenger_info, fleet_info)
daily_gate_data = daily_data(passenger_info)
oversold_business_data, oversold_economy_data = oversold()

layover_plane_data, layover_individual_details = layover(passenger_info, fleet_info)
late_layover_data = time_delay()

graphical_teamID()
