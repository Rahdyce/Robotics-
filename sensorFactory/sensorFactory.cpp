/*
Used for sensors including UltraSonic and IR Color Sensors
*/

#include "sensorFactory.h"
#include "Adafruit_TCS34725.h"
#include "Wire.h"
Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

void sensorFactory::setIRPin(int irPin, int sensorNumber){
	this -> irPin = irPin;
	this -> sensorNumber = sensorNumber;
	pinMode(irPin, INPUT);
}
void sensorFactory::setUltraPin(int echoPin, int triggerPin,int sensorNumber){
	this -> echoPin = echoPin;
    this -> triggerPin = triggerPin;
	this -> sensorNumber = sensorNumber;
    pinMode(triggerPin, OUTPUT);
    pinMode(echoPin, INPUT);
}
void sensorFactory::setColorPin(int sdaPin, int sclPin){
    Wire.setSDA(sdaPin);
    Wire.setSCL(sclPin);
    Wire.begin();
  }
bool sensorFactory::getIRsensor(int irPin){
    return digitalRead(irPin);}
bool sensorFactory::getLeftIR(int irPin){
    return digitalRead(irPin);} 
bool sensorFactory::getRightIR(int irPin){
    return digitalRead(irPin);} 
bool sensorFactory::getClawIR(int irPin){
    return digitalRead(irPin);}

bool sensorFactory::greenLight(){
    uint16_t r, g, b, c, colorTemp, lux;
    tcs.getRawData(&r, &g, &b, &c);
    colorTemp = tcs.calculateColorTemperature(r, g, b);
    lux = tcs.calculateLux(r, g, b);
    Serial.print("Color Temp: "); Serial.print(colorTemp, DEC); Serial.print(" K - "); 
    Serial.print("Lux: "); Serial.print(lux, DEC); Serial.print(" - "); 
    Serial.print("R: "); Serial.print(r, DEC); Serial.print(" ");
    Serial.print("G: "); Serial.print(g, DEC); Serial.print(" ");
    Serial.print("B: "); Serial.print(b, DEC); Serial.print(" ");
    Serial.print("C: "); Serial.print(c, DEC); Serial.print(" ");
    if(g>(r*1.5)){
      return true;}
    else{
      return false;
    }
  }
int sensorFactory::sonicDistanceSensor(int echoPin, int triggerPin){
    int distance,duration,cm,inch,count=0;
    pinMode(triggerPin,OUTPUT);
    pinMode(echoPin, INPUT);

    digitalWrite(triggerPin,LOW);
    delayMicroseconds(2);
    digitalWrite(triggerPin,HIGH);
    delayMicroseconds(2);
    digitalWrite(triggerPin,LOW);
    duration = pulseIn(echoPin, HIGH);
    delay(100);
    return cm = (duration/2)/29.1;
    }