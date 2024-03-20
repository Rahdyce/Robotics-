/*
  CommandFactory.h - Library for handling command transmission packets
  between Pico and Pi.
*/
#include "SensorFactory.h"
#include "Arduino.h"

SensorFactory::SensorFactory(void)
{
	this->IRLeft = 0;
	this->IRRight = 0;
	this->DISFront = 0; 
	this->DISRight = 0;
	this->DISBack = 0;
	this->CS = 0;
}

void SensorFactory::interpret(String str)
{
	int i = str.indexOf("-", 0);  //find first "-"
	int j = str.indexOf("-", 0);  //place holder
	static int vals[7] = { 0, 0, 0, 0, 0, 0, 0};   //array where the variables will be stored
	String str2 = str.substring(i + 1);        //chop the first "-"
	int index = 0;
	while (str2.length() > 2 && str2.indexOf("=", 0) > 0) {
		i = str2.indexOf("=", 0);      //find the loaction of "="
		j = str2.indexOf("-", 0);      //find the location of "-"
		vals[index] = str2.substring(i + 1, j).toInt();     //stoi my favorite function name string to int
		str2 = str2.substring(j + 1);                    //chop the string after "="
		index++;
	}
	// Interpret Pico Command String and update internal variables accordingly
	this->IRLeft = vals[0];
	this->IRRight = vals[1];
	this->DISFront = vals[2];
	this->DISRight = vals[3];
	this->DISBack = vals[4];
	this->CS = vals[5];
}


int SensorFactory::reader(int sel)
{
	switch (sel) {
	case 0:
		return this->IRLeft;
	case 1:
		return this->IRRight;
	case 2:
		return this->DISFront;
	case 3:
		return this->DISRight;
	case 4:
		return this->DISBack;
	case 5:
		return this->CS;
	}
	return -1;
}



void SensorFactory::writer(int sel, int value)
{
	switch (sel) {
	case 0:
		this->IRLeft = value;
		break;
	case 1:
		this->IRRight = value;
		break;
	case 2:
		this->DISFront = value;
		break;
	case 3:
		this->DISRight = value;
		break;
	case 4:
		this->DISBack = value;
		break;
	case 5:
		this->CS = value;
		break;
	}
}

String SensorFactory::generator(void)
{

	String command = String("A-IL=" + String(this->IRLeft) + "-IR=" + String(this->IRRight) + "-FD=" + String(this->DISFront) + "-RD=" + String(this->DISRight) + "-BD=" + String(this->DISBack) + "-CS=" + String(this->CS) + "-Z");
	return command;
}