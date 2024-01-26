import subprocess
import os
import time

def capture_image(image_number):
    image_path = f'/images/image{image_number}.jpg'
    command = f'fswebcam -r 1280x720 --no-banner {image_path}'
    subprocess.run(command, shell=True)

def main():
    # Set the directory to store images
    image_directory = '/images'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(image_directory):
        os.makedirs(image_directory)

    # Set the initial image number
    image_number = 1

    try:
        while True:
            # Capture an image
            capture_image(image_number)
            
            # Increment image number
            image_number += 1

            # Wait for some time before capturing the next image (adjust as needed)
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nCapture stopped by user.")

if __name__ == "__main__":
    main()
