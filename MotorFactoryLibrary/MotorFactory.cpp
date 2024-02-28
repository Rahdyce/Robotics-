/*
	MotorFactory.h - Library for handling motor function control in the IEEE 2024 Robot
	for Pi Pico
*/
#include "MotorFactory.h"
MotorFactory::MotorFactory(void)
{
	
}

void MotorFactory::setservoPins(int base, int shoulder, int elbow, int wrist, int swivel, int claw, int tray)
{
	  servoBasePin = base;
      servoShoulderPin = shoulder;
      servoElbowPin = elbow;
      servoWristPin = wrist;
      servoSwivelPin = swivel;
      servoClawPin = claw;
      servoTrayPin = tray;
	  
	  servoBase.attach(servoBasePin);
      servoShoulder.attach(servoShoulderPin);
      servoElbow.attach(servoElbowPin);
      servoWrist.attach(servoWristPin);
      servoSwivel.attach(servoSwivelPin);
      servoClaw.attach(servoClawPin);
      servoTray.attach(servoTrayPin);
}
void MotorFactory::setmotorPins(int leftmotor, int rightmotor, int leftspeed, int rightspeed)
 {
    motorLeftPin = leftmotor;
    motorRightPin = rightmotor;
    motorLeftSpeedPin = leftspeed;
    motorRightSpeedPin = rightspeed;

    pinMode(motorLeftPin, OUTPUT);
    pinMode(motorRightPin, OUTPUT);
    pinMode(motorLeftSpeedPin, OUTPUT);
    pinMode(motorRightSpeedPin, OUTPUT);
}
void MotorFactory::setServo(String servoname, int angle)
{
if (servoname == "Base") {
        servoBase.write(angle);
      } else if (servoname == "Shoulder") {
        servoShoulder.write(angle);
      } else if (servoname == "Elbow") {
        servoElbow.write(angle);
      } else if (servoname == "Wrist") {
        servoWrist.write(angle);
      } else if (servoname == "Swivel") {
        servoSwivel.write(angle);
      } else if (servoname == "Claw") {
        servoClaw.write(angle);
      } else if (servoname == "Tray") {
        servoTray.write(angle);
      }
}
void MotorFactory:: setDrive(String name, int speed)
{
 // Set drive motor speeds based on name
      if (name == "1") {
        if (speed >= 0 && speed <= 255) {
          analogWrite(motorLeftPin, speed);
        }
      } else if (name == "2") {
        if (speed >= 0 && speed <= 255) {
          analogWrite(motorRightPin, speed);
        }
      } else if (name == "3") {
        analogWrite(motorLeftSpeedPin, 127);
        analogWrite(motorRightSpeedPin, 127);
      }
}
