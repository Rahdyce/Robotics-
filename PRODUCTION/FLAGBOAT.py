import serial
import os
from DataFactory2 import DataFactory2
from CommandFactory import CommandFactory

# Constants
COM_PORT = "/dev/ttyACM0"
BAUD_RATE = 57600

# Initialize factory instances
data_factory = DataFactory2()
command_factory = CommandFactory()

def main():
    global data_factory, command_factory
    ser = None
    try:
        # Open the serial port
        ser = serial.Serial(COM_PORT, BAUD_RATE)
        print("Serial port opened successfully.")

        # Perform operations once the color sensor detects green
        if color_sensor_is_green(ser):
            sweep_arm(ser)
            gap_cross(ser)
            end_game(ser)

    except serial.SerialException as e:
        print(f"Failed to open serial port {COM_PORT}: {e}")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial port closed.")

    # Reboot the Nvidia Jetson
    os.system("sudo reboot")

#Method should be fine now
def color_sensor_is_green(ser):
    global data_factory
    try:
        while True:
            data = ser.readline().decode('utf-8').strip()
            data_factory.interpret(data)
            if data_factory.ColorSensor:  # True if green detected
                print("Color sensor detects green.")
                return True
            else:
                print("Color sensor does not detect green.")
    except Exception as e:
        print(f"An error occurred while reading the color sensor status: {e}")
        return False

#function to sweep arm
def sweep_arm(ser):
    #Path to the list of command to sweep the arm
    file_path = r'C:\Users\david\OneDrive\Documents\IEEE\SWEEP_ARM.txt'
    #Read all the lines of the SWEEP_ARM.txt and Then push the command until all commands are done
    #Strip the line in case of empty space
    file = open(file_path, 'r',encoding='utf-8')
    data_factory.interpret(data_factory)
    

# Implement gap_cross by running the commands in the GAP_CROSS.txt file, and if it reads HOLD in the GAP_CROSS.txt, it will run a hard_poll, and will then resume executing the commands in the GAP_CROSS.txt
def gap_cross(ser):
    file_path = r'C:\Users\david\OneDrive\Documents\IEEE\GAP_CROSS.txt'
    adj_left_path = r'C:\Users\david\OneDrive\Documents\IEEE\ADJUST_LEFT.txt'
    adj_right_path = r'C:\Users\david\OneDrive\Documents\IEEE\ADJUST_RIGHT.txt'
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            curr_command = file.readlines()
            command_factory(command_factory, curr_command)

        for line in curr_command:
            if line.startswith("HOLD"):
                left_line_on = data_factory.reader(data_factory, 0)
                right_line_on = data_factory.reader(data_factory, 1)
                # Check if we need to go right or go left
                if left_line_on == False and right_line_on == True and data_factory.reader(data_factory, 3) > 345:
                    command_factory.interpret("ADJUST_LEFT")
                    command_factory.command(adj_left_path)
                    print("ADJUST LEFT WAS RUN")
                if left_line_on == True and right_line_on == False and data_factory.reader(data_factory, 3) > 345:
                    command_factory.interpret("ADJUST_RIGHT")
                    command_factory.command(adj_right_path)
                    print("ADJUST RIGHT WAS RUN")        
            else:
                # Execute regular command
                ser.write(line.encode('utf-8'))
                print(f"Sending: {line.strip()}")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Completed gap_cross execution.")

#NO DELAY FOR THIS METHOD, it will take the commands from GAME_END, run the appropiate commandFactory function to the robot
def end_game(ser):
    # Implement the end_game function, using `ser` to communicate
    file_path=r'C:\Users\david\OneDrive\Documents\IEEE\GAME_END.txt'
    try:
        # Open the file containing end game commands
        with open(file_path, 'r', encoding='utf-8') as file:
            file_lines = file.readlines()

        for line in file_lines:
            # Assuming each command line starts with "CMD"
            if line.startswith("CMD"):
                # Extract command and potential delay
                command = line[line.index('A'):line.index('Z')+1] + '\n'
                # Send the command
                ser.write(command.encode('utf-8'))
                print(f"Sending: {command.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Completed end_game execution.")
    pass

if __name__ == "__main__":
    main()



