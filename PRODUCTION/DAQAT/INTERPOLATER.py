def generate_intermediate_waypoints():
    #ask for the waypoints
    start = input("Start Waypoint: ")
    end = input("End Waypoint: ")
    num_waypoints = int(input("How many waypoints in between?: "))

    # extract the values of each part of the arm in the waypoint
    start_vals = [int(x.split('=')[1]) for x in start.split('-')[1:-1]]
    end_vals = [int(x.split('=')[1]) for x in end.split('-')[1:-1]]
    
    # calculate the difference between start and end values
    #in case you arent sure because people do not use it often, zip takes iterable containers and returns a single iterator object. 
    diff_vals = [end_val - start_val for start_val, end_val in zip(start_vals, end_vals)]
    
    # calculate the step for each value for the intermediate waypoints so that they are spaced out evenly
    steps = [diff / (num_waypoints + 1) for diff in diff_vals]
    
    # now generate the set of intermediate waypoints
    waypoints = []
    for i in range(1, num_waypoints + 1):
        intermediate_vals = [round(start_val + step * i, 2) for start_val, step in zip(start_vals, steps)]
        waypoint = f"A-L={intermediate_vals[0]}-R={intermediate_vals[1]}-B={intermediate_vals[2]}-S={intermediate_vals[3]}-E={intermediate_vals[4]}-R={intermediate_vals[5]}-W={intermediate_vals[6]}-C={intermediate_vals[7]}-TD={intermediate_vals[8]}-Z"
        waypoints.append(waypoint)
    
    return waypoints

#test it
print(generate_intermediate_waypoints())

