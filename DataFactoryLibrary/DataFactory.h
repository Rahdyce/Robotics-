/*
	DataFactory.h - Library for handling Data control 
	in the IEEE 2024 Robot for Pi Pico
*/
#ifndef DataFactory_h
#define DataFactory_h

#include "Arduino.h"
class DataFactory 
{
  private:
    bool startingSignalColorSensorState;
    bool leftIRSensorState;
    bool rightIRSensorState;
    bool clawIRSensorState;
    int frontLeftDistanceReading;
    int frontRightDistanceReading;
    int backLeftDistanceReading;
    int backRightDistanceReading;
    int leftSideLeftDistanceReading;
    int leftSideRightDistanceReading;
    int rightSideLeftDistanceReading;
    int rightSideRightDistanceReading;
    bool runToggleState;

	public:
	String data();
	void interpret(String data);
	int read(String variable);
	int write(String variable, int value);
};
#endif
