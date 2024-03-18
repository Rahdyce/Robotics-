/*
  CommandFactory.h - Library for handling data transmission packets
  between Pico and Pi.
*/
#ifndef CommandFactory_h
#define CommandFactory_h

#include "Arduino.h"

class CommandFactory
{
	public:
		CommandFactory(void);
		String command(void);
		void interpret(String command);
		void writer(String argument, int value);
		void writer(int sel, int value);
		int reader(String argument);
		int reader(int sel);
	private:
		int LMSpeed;
		int RMSpeed;
		int baseAngle;
		int shoulderAngle;
		int elbowAngle;
		int wristAngle;
		int swivelAngle;
		int clawAngle;
		int trayDoor;
		int runStop;
		int sensorFactory;
};

#endif
