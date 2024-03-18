/*
	MotorFactory.h - Library for handling motor function control in the IEEE 2024 Robot
	for Pi Pico
*/
#define mini 500
#define maxi 2500
#include "MotorFactory.h"
#define clawhigh 93
#define clawlow 33
#define trayhigh 140
#define traylow 20
MotorFactory::MotorFactory(void)
{
	
}

void MotorFactory::setServoPins(int base, int shoulder, int elbow, int wrist, int swivel, int claw, int tray, int relay)
{
	  servoBasePin = base;
      servoShoulderPin = shoulder;
      servoElbowPin = elbow;
      servoWristPin = wrist;
      servoSwivelPin = swivel;
      servoClawPin = claw;
      servoTrayPin = tray;
	  relayPin = relay;
	  
	  servoBase.attach(servoBasePin,mini,maxi);
      servoShoulder.attach(servoShoulderPin,mini,maxi);
      servoElbow.attach(servoElbowPin,mini,maxi);
      servoWrist.attach(servoWristPin,mini,maxi);
      servoSwivel.attach(servoSwivelPin,mini,maxi);
      servoClaw.attach(servoClawPin,mini,maxi);
      servoTray.attach(servoTrayPin,mini,maxi);
}
void MotorFactory::setMotorPins(int leftp, int rightp, int leftn, int rightn, int lefts, int rights)
 {
    leftPos = leftp;
    rightPos = rightp;
    leftNeg = leftn;
    rightNeg = rightn;
	leftSpeed = lefts;
	rightSpeed = rights;
    pinMode(leftPos, OUTPUT);
    pinMode(rightPos, OUTPUT);
    pinMode(leftNeg, OUTPUT);
    pinMode(rightNeg, OUTPUT);
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
void MotorFactory::setServoI(int sel, int angle)
{
	switch (sel) {
		case 0:
			servoBase.write(angle);
			break;
		case 1:
			servoShoulder.write(angle);
			break;
		case 2:
			servoElbow.write(angle);
			break;
		case 3:
			servoWrist.write(angle);
			break;
		case 4:
			servoSwivel.write(angle);
			break;
		case 5:
			if(angle > clawhigh) {
				angle = clawhigh;
			} else if(angle < clawlow) {
				angle = clawlow;
			}
			servoClaw.write(angle);
			break;
		case 6:
			if(angle > trayhigh) {
				angle = trayhigh;
			} else if(angle < traylow) {
				angle = traylow;
			}
			servoTray.write(angle);
			break;
	}
}
void MotorFactory::setDrive(int sel, int speed)
{
	int aspeed = speed - 127; //offsetting
	int dir = aspeed > 0; // true for forward direction
	aspeed = abs(aspeed);
	aspeed = map(aspeed, 0, 127, 0, 255); //correcting for PWM range
	switch(sel)
	{
		case 1:
			if (dir) {
				digitalWrite(leftPos, HIGH);
				digitalWrite(leftNeg, LOW);
			} else {
				digitalWrite(leftPos, LOW);
				digitalWrite(leftNeg, HIGH);
			}
			analogWrite(leftSpeed,aspeed);
			break;
		case 2:
			if (dir) {
				digitalWrite(rightPos, HIGH);
				digitalWrite(rightNeg, LOW);
			} else {
				digitalWrite(rightPos, LOW);
				digitalWrite(rightNeg, HIGH);
			}
			analogWrite(rightSpeed,aspeed);
			break;
		case 3:
			if (dir) {
				digitalWrite(rightPos, HIGH);
				digitalWrite(rightNeg, LOW);
				digitalWrite(leftPos, HIGH);
				digitalWrite(leftNeg, LOW);
			} else {
				digitalWrite(rightPos, LOW);
				digitalWrite(rightNeg, HIGH);
				digitalWrite(leftPos, LOW);
				digitalWrite(leftNeg, HIGH);
			}
			analogWrite(leftSpeed,aspeed);
			analogWrite(rightSpeed,aspeed);
			break;
	}
}

void MotorFactory::set(int sel, int val)
{
	switch (sel) {
		case 0:
			setDrive(1, val);
			break;
		case 1:
			setDrive(2, val);
			break;
		case 2:
			setServoI(0, val);
			break;
		case 3:
			setServoI(1, val);
			break;
		case 4:
			setServoI(2, val);
			break;
		case 5:
			setServoI(3, val);
			break;
		case 6:
			setServoI(4, val);
			break;
		case 7:
			setServoI(5, val);
			break;
		case 8:
			setServoI(6, val);
			break;
		case 9:
			if(val > 0) {
				digitalWrite(relayPin, LOW);
			} else {
				digitalWrite(relayPin, HIGH);
			}
			break;
	}
}
