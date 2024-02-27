#include "MotorFactory.h" 

// Create an instance of MotorFactory
MotorFactory factory;

void setup() {
  // set pins for servos 
  //factory.setservoPins(2, 4, 5, 6, 7, 9, 10); 
  factory.setmotorPins(6, 8, 13, 14); 
  
  factory.setServo("base", 90);
  factory.setServo("shoulder", 90);
  factory.setServo("elbow", 90);
  factory.setServo("wrist", 90);
  factory.setServo("swivel", 90);
  factory.setServo("claw", 90);
  factory.setServo("tray", 90);
}

void loop() {
  // Move servo "base" to 45 degrees
  factory.setServo("base", 45);
  delay(1500);

  // Move servo "shoulder" to 135 degrees
  factory.setServo("shoulder", 135);
  delay(1500);

  // Set drive motor 1 to full speed forward
  factory.setDrive("1", 255);
  delay(1500);

  // Set drive motor 2 to full speed reverse
  factory.setDrive("2", 0);
  delay(1500);

  // Stop both drive motors
  factory.setDrive("3", 127);
  delay(1500);
  
}
