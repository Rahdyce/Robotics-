import serial
import os

# Your constants
COM_PORT = "COM3"
BAUD_RATE = 57600

def main():
    ser = None
    try:
        # Open the serial port
        ser = serial.Serial(COM_PORT, BAUD_RATE)
        print("Serial port opened successfully.")

        while not color_sensor_is_green(ser):
            pass  # Keep checking until green is detected

        # Once green is detected, proceed with the operations
        sweep_arm(ser)
        gap_cross(ser)
        end_game(ser)

    except serial.SerialException as e:
        print(f"Failed to open serial port {COM_PORT}: {e}")
    finally:
        # Close the serial port
        if ser and ser.is_open:
            ser.close()
            print("Serial port closed.")

    # Reboot the Nvidia Jetson
    os.system("sudo reboot")

def color_sensor_is_green(ser):
    # Implement the logic to check if the color sensor is green
    try:
        while True:
            # Check if data is available to read
            if ser.in_waiting > 0:
                data = ser.readline().decode('utf-8').strip()

                # Parse for the "-CS=" pattern and extract the status
                cs_index = data.find("-CS=")
                if cs_index != -1:
                    # Assuming the status value follows immediately after "-CS="
                    cs_value = data[cs_index + 4]
                    if cs_value == "1":
                        print("Color sensor detects green.")
                        return True
                    elif cs_value == "0":
                        print("Color sensor does not detect green.")
    except Exception as e:
        print(f"An error occurred while reading the color sensor status: {e}")
        # Returning False or handling the error as needed
        return False

def sweep_arm(ser):
    # Implement the sweep_arm function, using `ser` to communicate
    file_path=r'C:\Users\david\OneDrive\Documents\IEEE\SWEEP_ARM.txt'
    try:
        # Open the file containing waypoints
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
        print("Completed sweep_arm execution.")
    pass

def gap_cross(ser):
    # Implement the gap_cross function, using `ser` to communicate
    
    pass

def end_game(ser):
    # Implement the end_game function, using `ser` to communicate
    file_path=r'C:\Users\david\OneDrive\Documents\IEEE\GAME_END.txt.txt'
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
