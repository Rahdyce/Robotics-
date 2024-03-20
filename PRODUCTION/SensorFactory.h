#pragma once
/*

*/
#ifndef SensorFactory_h
#define SensorFactory_h

#include "Arduino.h"

class SensorFactory
{
public:
	SensorFactory(void);
	String generator(void);
	void writer(int sel, int value);
	int reader(int sel);
private:
	int IRLeft;
	int IRRight;
	int DISFront;
	int DISRight;
	int DISBack;
	int CS;
};

#endif