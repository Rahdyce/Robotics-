def generate_intermediate_waypoints():
    #ask for the waypoints
    start = input("Start Waypoint: ")
    end = input("End Waypoint: ")
    num_waypoints = int(input("How many waypoints in between?: "))

    # extract the values of each part of the arm in the waypoint
    start_parts = start.split('-')
    end_parts = end.split('-')
    
    # Extract X value as integer for processing
    start_x_value = int([part for part in start_parts if part.startswith("X=")][0].split('=')[1])
    end_x_value = int([part for part in end_parts if part.startswith("X=")][0].split('=')[1])

    # Determine X value for intermediate waypoints based on the rule provided
    intermediate_x_value = 1 if end_x_value == 1 else start_x_value

    # exclude 'A', 'X=value', and 'Z' to only get the numeric parts
    start_vals = [int(x.split('=')[1]) for x in start_parts if "=" in x and not x.startswith("X=")]
    end_vals = [int(x.split('=')[1]) for x in end_parts if "=" in x and not x.startswith("X=")]

    # calculate the difference between start and end values including X
    diff_vals = [end_val - start_val for start_val, end_val in zip(start_vals + [start_x_value], end_vals + [end_x_value])]
    
    # calculate the step for each value for the intermediate waypoints so that they are spaced out evenly
    steps = [diff / (num_waypoints + 1) for diff in diff_vals]
    
    # generate the set of intermediate waypoints
    waypoints = []
    for i in range(1, num_waypoints + 1):
        intermediate_vals = [round(start_val + step * i) for start_val, step in zip(start_vals + [start_x_value], steps)]
        # format
        waypoint_parts = [f"L={intermediate_vals[0]}", f"R={intermediate_vals[1]}", f"B={intermediate_vals[2]}",
                          f"S={intermediate_vals[3]}", f"E={intermediate_vals[4]}", f"R={intermediate_vals[5]}",
                          f"W={intermediate_vals[6]}", f"C={intermediate_vals[7]}", f"TD={intermediate_vals[8]}", f"X={intermediate_x_value}"]
        waypoint = "A-" + "-".join(waypoint_parts) + "SF-0-Z"
        waypoints.append(waypoint)
    
    return waypoints
