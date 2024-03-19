/*
  CommandFactory.h - Library for handling command transmission packets
  between Pico and Pi.
*/
#include "CommandFactory.h"
#include "Arduino.h"

CommandFactory::CommandFactory(void)
{
	this->LMSpeed = 0;
	this->RMSpeed = 0;
	this->baseAngle = 0;
	this->shoulderAngle = 0;
	this->elbowAngle = 0;
	this->wristAngle = 0;
	this->swivelAngle = 0;
	this->clawAngle = 0;
	this->trayDoor = 0;
	this->runStop = 0;
	this->sensorFactory = 0;
}

void CommandFactory::interpret(String str)
{
    int i = str.indexOf("-", 0);  //find first "-"
	int j = str.indexOf("-", 0);  //place holder
	static int vals[13] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};   //array where the variables will be stored
	String str2 = str.substring(i+1);        //chop the first "-"
	int index = 0;
	while (str2.length() > 2 && str2.indexOf("=", 0) > 0){
		i = str2.indexOf("=", 0);      //find the loaction of "="
		j = str2.indexOf("-", 0);      //find the location of "-"
		vals[index] = str2.substring(i+1, j).toInt();     //stoi my favorite function name string to int
		str2 = str2.substring(j+1);                    //chop the string after "="
		index ++;
	}
    // Interpret Pico Command String and update internal variables accordingly
    this->LMSpeed = vals[0];
    this->RMSpeed = vals[1];
    this->baseAngle = vals[2];
    this->shoulderAngle = vals[3];
    this->elbowAngle = vals[4];
    this->wristAngle = vals[5];
    this->swivelAngle = vals[6];
    this->clawAngle = vals[7];
    this->trayDoor = vals[8];
	this->runStop = vals[9];
	this->sensorFactory = vals[10];
}

int CommandFactory::reader(String variable)
{
	int sel = 0;
	int numIndexes = 11;
	String argnames[numIndexes] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor","runStop", "sensorFactory"};
	for(int i; i < numIndexes; i++) {
		if(variable.equals(argnames[i])) {
			sel = i;
			break;
		}
	}
	switch (sel) {
		case 0:
			return this->LMSpeed;
		case 1:
			return this->RMSpeed;
		case 2:
			return this->baseAngle;
		case 3:
			return this->shoulderAngle;
		case 4:
			return this->elbowAngle;
		case 5:
			return this->wristAngle;
		case 6:
			return this->swivelAngle;
		case 7:
			return this->clawAngle;
		case 8:
			return this->trayDoor;
		case 9:
			return this->runStop;
		case 10:
			return this->sensorFactory;
	}
	return -1;
}

int CommandFactory::reader(int sel)
{
	switch (sel) {
		case 0:
			return this->LMSpeed;
		case 1:
			return this->RMSpeed;
		case 2:
			return this->baseAngle;
		case 3:
			return this->shoulderAngle;
		case 4:
			return this->elbowAngle;
		case 5:
			return this->wristAngle;
		case 6:
			return this->swivelAngle;
		case 7:
			return this->clawAngle;
		case 8:
			return this->trayDoor;
		case 9:
			return this->runStop;
		case 10:
			return this->sensorFactory;
	}
	return -1;
}

void CommandFactory::writer(String variable, int value)
{
	int sel = 0;
	int numIndexes = 11;
	String argnames[11] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor","runStop", "sensorFactory"};
	for(int i; i < numIndexes; i++) {
		if(variable.equals(argnames[i])) {
			sel = i;
			break;
		}
	}
	switch (sel) {
		case 0:
			this->LMSpeed = value;
			break;
		case 1:
			this->RMSpeed = value;
			break;
		case 2:
			this->baseAngle = value;
			break;
		case 3:
			this->shoulderAngle = value;
			break;
		case 4:
			this->elbowAngle = value;
			break;
		case 5:
			this->wristAngle = value;
			break;
		case 6:
			this->swivelAngle = value;
			break;
		case 7:
			this->clawAngle = value;
			break;
		case 8:
			this->trayDoor = value;
			break;
		case 9:
			this->runStop = value;
			break;
		case 10:
			this->sensorFactory = value;
			break;
	}
}

void CommandFactory::writer(int sel, int value)
{
	switch (sel) {
		case 0:
			this->LMSpeed = value;
			break;
		case 1:
			this->RMSpeed = value;
			break;
		case 2:
			this->baseAngle = value;
			break;
		case 3:
			this->shoulderAngle = value;
			break;
		case 4:
			this->elbowAngle = value;
			break;
		case 5:
			this->wristAngle = value;
			break;
		case 6:
			this->swivelAngle = value;
			break;
		case 7:
			this->clawAngle = value;
			break;
		case 8:
			this->trayDoor = value;
			break;
		case 9:
			this->runStop = value;
			break;
		case 10:
			this->sensorFactory = value;
			break;
	}
}

String CommandFactory::command(void)
{
	//String dash = "-";
	//String equals = "=";
	String command = String("A-L=" + String(this->LMSpeed) + "-R=" + String(this->RMSpeed) + "-B=" + String(this->baseAngle) + "-S=" + String(this->shoulderAngle) + "-E=" + String(this->elbowAngle) + "-R=" + String(this->wristAngle) + "-W=" + String(this->swivelAngle) + "-C=" + String(this->clawAngle) + "-TD=" + String(this->trayDoor) + "-X=" + String(this->runStop) + "-SF=" + String(this->sensorFactory) + "-Z");
	//String command = String("A" + dash + "L" + equals + String(this->LMSpeed) + dash + "R" + equals + String(this->RMSpeed) + dash + "B" + equals + String(this->baseAngle) + dash + "S" + equals + String(this->shoulderAngle) + dash + "E" + equals + String(this->elbowAngle) + dash + "R" + equals + String(this->wristAngle) + dash + "W" + equals + String(this->swivelAngle) + dash + "C" + equals + String(this->clawAngle) + dash + "TD" + equals + String(this->trayDoor) + dash + "X" + equals + String(this->runStop) + dash + "SF" + equals + String(this->sensorFactory) + dash + "Z");
	return command;
}
