import serial
import os
import sys
import time

#Global Variables for ease of modification
COM_PORT = "COM3"
BAUD_RATE = 57600
TOF_THRESHOLD = 610  # Threshold for TOF sensor in mm

#function to send all stop
def allstop_com():
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE)
        print("Serial port opened successfully.")
        
        # Send the allstop command
        allstop_command = "A-L=127-R=127-B=26-S=84-E=0-R=144-W=82-C=60-TD=90-X=0-Z"
        ser.write(allstop_command.encode('utf-8'))
        print("Allstop command sent.")
        
    except serial.SerialException as e:
        print(f"Failed to open serial port {COM_PORT}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

#function to send allstop if color sensor is off, else proceed to playback sweep
def sense_det(sensor_packet):
    if sensor_packet  == 0:
        allstop_com()
    else:
        set_arm()

#function to runback preset runs that we have interpolated with INTERPOLATOR.py, these will be the final runs the robot executes at comp
def playback(command_packet):
    #if it receives the sweep log, playback the sweep waypoints
     if command_packet in ["SWEEP_LOG.txt", "CLIMB_POSITION.txt", "DESCENT_POSITION.txt", "CLIMB.txt", "EM_RAMP_CLIMB.txt", "ADJUST_RIGHT.txt","ADJUST_LEFT.txt","DESCENT.txt","WALL_ALIGN.txt"]:
        return 1  # Simulating a successful execution

#function that will set the arm to the climb and descent positions for the ramp, and for crossing the gap
def set_arm(command_packet):
    status = playback(command_packet)
    #If the sweep is executed (returns 1) and the file was SWEEP_LOG (which runs the sweep command), then the arm is ready to be put into the climb position
    if status == 1 and command_packet == "SWEEP_LOG.txt":
        playback("CLIMB_POSITION.txt")

#function that gets us over the ramp (steps 6-8)
def ramp_run(ir_sensor_1, ir_sensor_2, tof_sensor):
    #If both IR Sensors are on Black, both will return true meaning we are aligned (atleast somewhat)
    if ir_sensor_1 == "-IL=1" and ir_sensor_2 == "-IR=1":
        #playback the run up the ramp
        playback("CLIMB.txt")
    #in case we get stuck on ramp, we can have an emergency code to get us up. 5mm is a placeholder for now
    if tof_sensor > 5 and tof_sensor < TOF_THRESHOLD:
        playback("EM_RAMP_CLIMB.txt")
        #If we are pointing left, this means ir_sensor_2 will be false and ir_sensor_1 will be true (ir_sensor_2 is the rightmost sensor)
    if tof_sensor > TOF_THRESHOLD and ir_sensor_1 == "-IL=1" and ir_sensor_2 == "-IR=0":
        playback("ADJUST_RIGHT.txt")
    #now do the opposite if it is pointing right
    if tof_sensor > TOF_THRESHOLD and ir_sensor_1 == "-IL=0" and ir_sensor_2 == "-IR=1":
        playback("ADJUST_LEFT.txt")
    #If our time of flight sensor returns the value we want (greater than 610mm or 2feet) we know we are at the top of the ramp, and if we are still aligned with the line this means we are good to go and descend down the ramp
    if tof_sensor > TOF_THRESHOLD and ir_sensor_1 == "-IL=1" and ir_sensor_2 == "-IR=1":
        playback("DESCENT_POSITION.txt")
        # Start descent
        while True:
            playback("DESCENT.txt")
            
            # Check ir_sensor_1 continuously during descent
            if not ir_sensor_1:  # If ir_sensor_1 detects False, break the loop (the left sensor, ir_sensor_1 has hit, the corner of the yellow line)
                break
        robot_turn_and_wall()
    
    #if for some reason both lines are False, it means the robot is so far askew that its basically over for us anyways. No point adjusting past this.

#turns the robot and sends it to the wall
def robot_turn_and_wall(front_sensor):
    #if the front sensor is within a reasonable tolerance away from the wall, go forward (the reason this wont be fixed is if we went down at an angle and we are not perfectly perpindicular to the wall)
    #if we are angled to far to the left, move the robot a bit to the right, ADJUST_RIGHT.txt should be fine
    while True:

      if front_sensor > 110:
            # If the robot angled too far to the left, adjust it to the right
            playback("ADJUST_RIGHT.txt")
      elif 100 < front_sensor <= 110:
            # If within a reasonable tolerance, initiate the turn left
            playback("TURN_LEFT.txt")
            break  # Exit the loop once the turn command is issued, then we can run the command to go forward
        #chances are the robot is angled to far to the right and is looking at the wall behind the boosters, adjust the robot left
      elif front_sensor < 100:
            playback("ADJUST_LEFT.txt")

    #send the robot to the wall until the front sensor is at a distance where we can pick up the carrots, at t
    while True:
        #If the front_sensor isnt up against the wall, keep going towards it, 2 is a placeholder number
        if front_sensor > 2:
            playback("WALL_RUN.txt")
        else:
            break
    carrot_pickup()

#picks up the carrots
def carrot_pickup():
    playback("CARROT_LOG.txt")
    
#function to get us across the gap
def gap_cross(ir_sensor_1, ir_sensor_2, tof_threshold):
    #We are aligned but not at the top of the ramp
    while ir_sensor_1 == "A-IL=1" and ir_sensor_2 == "I-IR=1" and tof_threshold < TOF_THRESHOLD:
        playback("WALL_TO_GAP.txt")
        break
    #Adjust arm position and cross the gap (should all be done in GAP_CROSS.txt)
    playback("GAP_CROSS.txt")

#function to depot the carrots
def depot(ir_sensor_1, ir_sensor_2):
    #If both IR Sensors are on Black, both will return true meaning we are aligned (atleast somewhat)
    while True:
        if ir_sensor_1 == "-IL=0" and ir_sensor_2 == "-IR=1":
            playback("ADJUST_LEFT.txt")
        elif ir_sensor_1 == "-IL=1" and ir_sensor_2 == "-IR=0":
            playback("ADJUST_RIGHT.txt")
        else:
            break
    playback("DROP_CARROTS.txt")

def button_and_reset():
    #should be intelligent, but for right now we are gonna preprogram it
    playback("GAME_END.txt")

    #restart jetson
    os.system("sudo reboot")

def interpret_sensor_data(sensor_string):
    # Initialize default values for sensor status
    ir_sensor_1_status = "0"
    ir_sensor_2_status = "0"

    # Find the positions of the IR sensor indicators in the string
    ir_sensor_1_pos = sensor_string.find("-IL=")
    ir_sensor_2_pos = sensor_string.find("-IR=")

    # Extract the status if the indicators are found
    if ir_sensor_1_pos != -1:
        ir_sensor_1_status = sensor_string[ir_sensor_1_pos + 4]

    if ir_sensor_2_pos != -1:
        ir_sensor_2_status = sensor_string[ir_sensor_2_pos + 4]

    ir_sensor_1 = f"-IL={ir_sensor_1_status}"
    ir_sensor_2 = f"-IR={ir_sensor_2_status}"

    return ir_sensor_1, ir_sensor_2

def main():
    # Example sensor values to start with
    # Real inputs will come from the imported SensorFactory will figure out the syntax for that later today, it is currently 2:50 am and I want to sleep
    ir_sensor_1, ir_sensor_2, tof_sensor, front_sensor = True, True, 600, 105

    # Sequentially execute tasks starting from sensor_packet which will be imported
    sense_det(sensor_packet)  
    set_arm("SWEEP_LOG.txt")
    ramp_run(ir_sensor_1, ir_sensor_2, tof_sensor)
    robot_turn_and_wall(front_sensor)
    carrot_pickup()
    gap_cross(ir_sensor_1, ir_sensor_2, tof_sensor)  # note: pass tof_sensor, not tof_threshold
    depot(ir_sensor_1, ir_sensor_2)
    button_and_reset()
