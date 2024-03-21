import serial

# 4 functions, SWEEP function that runs SWEEP.txt, GAP CROSS Function that follows the yellow line across the gap, and END GAME Function that makes the robot hit the button, and interpreter
COM_PORT = "COM3"
BAUD_RATE = 57600
LEFT_IR_PIN = 3
RIGHT_IR_PIN = 2

#Command to open the serial, check for color sensor green, and sweep the arm
def sweep_arm():
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE)
        print("Serial port opened successfully.")
        
        # Send the allstop command
        allstop_command = "A-L=127-R=127-B=26-S=84-E=0-R=144-W=82-C=60-TD=90-X=0-Z"
        ser.write(allstop_command.encode('utf-8'))
        print("Allstop command sent.")

        # Assuming color_sensor is a function that returns True if the sensor is green
        if color_sensor():  # This function needs to be defined based on your sensor reading mechanism
            with open("SWEEP.txt", "r") as sweep_file:
                sweep_command = sweep_file.read()
                ser.write(sweep_command.encode('utf-8'))
            print("Sweep command executed.")
            
    except serial.SerialException as e:
        print(f"Failed to open serial port {COM_PORT}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the serial port if it's open
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Serial port closed.")

#Go up ramp by following line with ir sensors, turn, go to second corner, turn, go to the gap ramp, cross, and thug that shit out
def gap_cross():
    #If both ir_sensors are true, go continue 

#turn robot into red button when gap_cross is complete
def end_game():

#interprets the serial string from servos 
def interpreter():
