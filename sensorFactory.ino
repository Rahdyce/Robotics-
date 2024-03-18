#include <Wire.h>
#include <Adafruit_TCS34725.h>
class sensorFactory{
    Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);
    
  private:
    int irPin, triggerPin, echoPin, sensorNumber;
  public:
  void setIRPin(int irPin, int sensorNumber){
    this -> irPin = irPin;
    this -> sensorNumber = sensorNumber;
    pinMode(irPin, INPUT);
  }
  void setUltraPin(int echoPin, int triggerPin, int sensorNumber){
    this -> echoPin = echoPin;
    this -> triggerPin = triggerPin;
    this -> sensorNumber = sensorNumber;
    pinMode(triggerPin, OUTPUT);
    pinMode(echoPin, INPUT);
  }
  void setColorPin(int sdaPin, int sclPin){
      Wire.setSDA(sdaPin);
      Wire.setSCL(sclPin);
      Wire.begin();
  }
  bool getLeftIR(int irPin){
    return digitalRead(irPin);} 
  
  bool getRightIR(int irPin){
    return digitalRead(irPin);}
  
  bool getClawIR(int irPin){
    return digitalRead(irPin);}
  
  bool greenLight(){
    uint16_t r, g, b, c, colorTemp, lux;
    tcs.getRawData(&r, &g, &b, &c);
    colorTemp = tcs.calculateColorTemperature(r, g, b);
    lux = tcs.calculateLux(r, g, b);
    Serial.print("Color Temp: "); Serial.print(colorTemp, DEC); Serial.print(" K - "); 
    Serial.print("Lux: "); Serial.print(lux, DEC); Serial.print(" - "); 
    Serial.print("R: "); Serial.print(r, DEC); Serial.print(" ");
    Serial.print("G: "); Serial.print(g, DEC); Serial.print(" ");
    Serial.print("B: "); Serial.print(b, DEC); Serial.print(" ");
    Serial.print("C: "); Serial.print(c, DEC); Serial.println(" ");
    if(g>(r*1.5||b*1.5)){
      return true;}
    else{
      return false;}
  }
  int sonicDistanceSensor(int echoPin,int triggerPin){
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
    return cm=(duration/2)/29.1;
    }
};

void setup() {
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:

}
