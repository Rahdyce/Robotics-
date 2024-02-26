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
}

void CommandFactory::interpret(String input)
{
    int len = input.length() / 3;
    int dashes[len];
    int equals[len];
    int dash = 0;
    int equal = 0;
    int recentDash = 0;
    int recentEquals = 0;
    bool runStop = true;
    int i = 0;
    int j = 0;
    while (runStop) {
        dash = input.indexOf('-', recentDash);
        equal = input.indexOf('=', recentEquals);
        if (dash > -1) {
            dashes[i] = dash;
            i++;
            recentDash = dash + 1;
        }
        if (equal > -1) {
            equals[j] = equal;
            j++;
            recentEquals = equal + 1;
        }
        if (equal < 0 && dash < 0) {
            runStop = false;
        }
    }

    int numArgs = i - 1;
    int numVals = j - 1;

    String args[numArgs];
    String vals[numVals];

    for (int k = 0; k < numArgs; k++) {
        args[k] = input.substring(dashes[k], equals[k]);
        vals[k] = input.substring(equals[k] + 1, dashes[k + 1]);
    }

    // Interpret Pico Command String and update internal variables accordingly
    this->LMSpeed = vals[0].toInt();
    this->RMSpeed = vals[1].toInt();
    this->baseAngle = vals[2].toInt();
    this->shoulderAngle = vals[3].toInt();
    this->elbowAngle = vals[4].toInt();
    this->wristAngle = vals[5].toInt();
    this->swivelAngle = vals[6].toInt();
    this->clawAngle = vals[7].toInt();
    this->trayDoor = vals[8].toInt();
}

int CommandFactory::reader(String variable)
{
	int sel = 0;
	int numIndexes = 9;
	String argnames[numIndexes] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor"};
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
	}
	return -1;
}

void CommandFactory::writer(String variable, int value)
{
	int sel = 0;
	int numIndexes = 9;
	String argnames[9] = {"LMSpeed","RMSpeed","baseAngle","shoulderAngle","elbowAngle","wristAngle","swivelAngle","clawAngle","trayDoor"};
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
	}
}

String CommandFactory::command(void)
{
	String dash = "-";
	String equals = "=";
	String command = String("A" + dash + "L" + equals + String(this->LMSpeed) + dash + "R" + equals + String(this->RMSpeed) + dash + "B" + equals + String(this->baseAngle) + dash + "S" + equals + String(this->shoulderAngle) + dash + "E" + equals + String(this->elbowAngle) + dash + "R" + equals + String(this->wristAngle) + dash + "W" + equals + String(this->swivelAngle) + dash + "C" + equals + String(this->clawAngle) + dash + "TD" + equals + String(this->trayDoor) + dash + "Z");
	return command;
}
