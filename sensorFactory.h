/*
Used for sensors including UltraSonic and IR Color Sensors
*/

#ifndef sensorFactory_h
#define sensorFactory_h

#include "Arduino.h"
#include "Adafruit_TCS34725.h"
#include "Wire.h"


class sensorFactory{
	private:
		int irPin, triggerPin, echoPin, sensorNumber;
	public:
		void setIRPin(int irPin, int sensorNumber);
		void setUltraPin(int echoPin, int triggerPin, int sensorNumber);
		void setColorPin(int sdaPin, int sclPin);
		bool getLeftIR(int irPin);
		bool getRightIR(int irPin);
		bool getClawIR(int irPin);
		bool greenLight();
		int sonicDistanceSensor(int echoPin, int triggerPin);
};
#endif