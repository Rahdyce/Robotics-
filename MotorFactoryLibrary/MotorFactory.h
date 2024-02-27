/*
	MotorFactory.h - Library for handling motor function control in the IEEE 2024 Robot
	for Pi Pico
*/
#ifndef MotorFactory_h
#define MotorFactory_h

#include "Arduino.h"
#include <Servo.h>
class MotorFactory
{
	
	public:
		MotorFactory(void);
		void setservoPins(int base, int shoulder, int elbow, int wrist, int swivel, int claw, int tray);
		void setmotorPins(int leftmotor, int rightmotor, int leftspeed, int rightspeed);
		void setServo(String servoname, int angle);
		void setDrive(String name, int speed);
	private:
		int servoBasePin, servoShoulderPin, servoElbowPin, servoWristPin, servoSwivelPin, servoClawPin, servoTrayPin;
		int motorLeftPin, motorRightPin, motorLeftSpeedPin, motorRightSpeedPin;
		
		Servo servoBase, servoShoulder, servoElbow, servoWrist, servoSwivel, servoClaw, servoTray;
};

#endif
