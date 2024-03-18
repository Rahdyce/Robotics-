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
		void setServoPins(int base, int shoulder, int elbow, int wrist, int swivel, int claw, int tray, int relay);
		void setMotorPins(int leftp, int rightp, int leftn, int rightn, int lefts, int rights);
		void setServo(String servoname, int angle);
		void setServoI(int sel, int angle);
		void setDrive(int sel, int speed);
		void set(int sel, int val);
	private:
		int servoBasePin, servoShoulderPin, servoElbowPin, servoWristPin, servoSwivelPin, servoClawPin, servoTrayPin, relayPin;
		int leftPos, rightPos, leftNeg, rightNeg, leftSpeed, rightSpeed;
		Servo servoBase;
		Servo servoShoulder;
		Servo servoElbow;
		Servo servoWrist;
		Servo servoSwivel;
		Servo servoClaw;
		Servo servoTray;
};

#endif
