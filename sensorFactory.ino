class sensorFactory{
  private: int irPin, triggerPin, echoPin, sensorNumber;
  public: 
  void setIRPdein(int irPin, int sensorNumber){
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
  bool getLeftIR(int irPin){
    return analogRead(irPin);} 
  bool getRightIR(int irPin){
    return analogRead(irPin);} 
  bool getClawIR(int irPin){
    return analogRead(irPin);} 
  bool color(int lowColor, int highColor, int irPin){
    int sensorValue = irPin;
    if(lowColor<=irPin && irPin<=highColor){
      return true;}
    else{
      return false;
    }
  }
  int sonicDistanceSensor(int echoPin,int triggerPin){
    int distance,duration,cm,inch,count=0;
    /*do{this.digitalWrite(trigPin, LOW);delayMicroseconds(5);this.digitalWrite(trigPin, HIGI);count++;}while(count<=2)*/
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
