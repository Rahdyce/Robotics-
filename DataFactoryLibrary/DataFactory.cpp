/*
	DataFactory.h - Library for Data in the IEEE 2024 Robot
	for Pi Pico
*/
#include "DataFactory.h"
#include "Arduino.h"
  
  DataFactory::DataFactory(void)
  {
  
  }
  void DataFactory::String data()
  {
  String data() {
      String dataString = "A-CS=";
      // Concatenate internal variable values into a data string
      dataString += startingSignalColorSensorState ? "1" : "0";
        dataString+= "-IL=";
      dataString += leftIRSensorState ? "1" : "0";
        dataString+= "-IR=";
      dataString += rightIRSensorState ? "1" : "0";
        dataString+= "-IC=";
      dataString += clawIRSensorState ? "1" : "0";
        dataString+= "-FL=";
      dataString += String(frontLeftDistanceReading);
        dataString+= "-FR=";
      dataString += String(frontRightDistanceReading);
        dataString+= "-BL=";
      dataString += String(backLeftDistanceReading);
        dataString+= "-BR=";
      dataString += String(backRightDistanceReading);
        dataString+= "LL=";
      dataString += String(leftSideLeftDistanceReading);
        dataString+= "LR";
      dataString += String(leftSideRightDistanceReading);
        dataString+= "RL=";
      dataString += String(rightSideLeftDistanceReading);
        dataString+= "RR=";
      dataString += String(rightSideRightDistanceReading);
        dataString+= "-RT=";
      dataString += runToggleState ? "1" : "0";
        dataString+= "-Z";
      return dataString;
    }
  }
  void DataFactory:: void intepret(String data)
  {
   int len = data.length() / 3;
      int dashes[len];
      int equals[len];
      int dash = 0;
      int equal = 0;
      int recentDash = 0;
      int recentEquals = 0;
      bool runStop = true;
      int i = 0;
      int j = 0;
      while(runStop) {
        dash = data.indexOf('-',recentDash);
        equal = data.indexOf('=',recentEquals);
        if(dash > -1) {
          dashes[i] = dash;
          i++;
          recentDash = dash;
        }
        if(equal > -1) {
          equals[j] = equal;
          j++;
          recentEquals = equal;
        }
       if(equal < 0 && dash < 0) {
          runStop = false;
        }
      }
       int Dashes[i];
       int Equals[j];
       for(int k; k < i; k++) {
       Dashes[k] = dashes[k];
      }
      for(int l; l < j; l++) {
        Equals[l] = equals[l];
      }
      int numArgs = i - 1;
      int numVals = j - 1;
      String args[numArgs];
      String vals[numVals];
      for(int k; k < numArgs; k++) {
      args[k] = data.substring(Dashes[k],Equals[k]);
      vals[k] = data.substring(Equals[k],Dashes[k+1]);
      }
      
      // Interpret Pico Data String and update internal variables accordingly
      startingSignalColorSensorState = vals[0].toInt();
      leftIRSensorState = vals[1].toInt();
      rightIRSensorState = vals[2].toInt();
      clawIRSensorState = vals[3].toInt();
      frontLeftDistanceReading = vals[4].toInt();
      frontRightDistanceReading = vals[5].toInt();
      backLeftDistanceReading = vals[6].toInt();
      backRightDistanceReading = vals[7].toInt();
      leftSideLeftDistanceReading = vals[8].toInt();
      leftSideRightDistanceReading =vals[9].toInt();
      rightSideLeftDistanceReading = vals[10].toInt();
      rightSideRightDistanceReading =vals[11].toInt();
      runToggleState = vals[12].toInt();
    }
  void DataFactory:: int read(String variable)
  {
  // Read the value of the requested variable
      if (variable == "Starting Signal Color Sensor State") {
        return startingSignalColorSensorState;
      } else if (variable == "Left IR Sensor State") {
        return leftIRSensorState;
      } else if (variable == "Right IR Sensor State") {
        return rightIRSensorState;
      } else if (variable == "Claw IR Sensor State") {
        return clawIRSensorState;
      } else if (variable == "Front Left Distance Reading") {
        return frontLeftDistanceReading;
      } else if (variable == "Front Right Distance Reading") {
        return frontRightDistanceReading;
      } else if (variable == "Back Left Distance Reading") {
        return backLeftDistanceReading;
      } else if (variable == "Back Right Distance Reading") {
        return backRightDistanceReading;
      } else if (variable == "Left Side Left Distance Reading") {
        return leftSideLeftDistanceReading;
      } else if (variable == "Left Side Right Distance Reading") {
        return leftSideRightDistanceReading;
      } else if (variable == "Right Side Left Distance Reading") {
        return rightSideLeftDistanceReading;
      } else if (variable == "Right Side Right Distance Reading") {
        return rightSideRightDistanceReading;
      } else if (variable == "Run Toggle State") {
        return runToggleState;
      }
  }
  void DataFactory:: int write(String variable,int value)
  {
  // Write the value to the requested variable
      if (variable == "Starting Signal Color Sensor State") {
        startingSignalColorSensorState = value;
      } else if (variable == "Left IR Sensor State") {
        leftIRSensorState = value;
      } else if (variable == "Right IR Sensor State") {
        rightIRSensorState = value;
      } else if (variable == "Claw IR Sensor State") {
        clawIRSensorState = value;
      } else if (variable == "Front Left Distance Reading") {
        frontLeftDistanceReading = value;
      } else if (variable == "Front Right Distance Reading") {
        frontRightDistanceReading = value;
      } else if (variable == "Back Left Distance Reading") {
        backLeftDistanceReading = value;
      } else if (variable == "Back Right Distance Reading") {
        backRightDistanceReading = value;
      } else if (variable == "Left Side Left Distance Reading") {
        leftSideLeftDistanceReading = value;
      } else if (variable == "Left Side Right Distance Reading") {
        leftSideRightDistanceReading = value;
      } else if (variable == "Right Side Left Distance Reading") {
        rightSideLeftDistanceReading = value;
      } else if (variable == "Right Side Right Distance Reading") {
        rightSideRightDistanceReading = value;
      } else if (variable == "Run Toggle State") {
        runToggleState = value;
      }
      return value; // Return the updated value
    }
  }
