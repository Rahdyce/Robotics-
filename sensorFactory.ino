class sensors{
  private:
      int IRPin,trigPin,echoPin, sensorNumber;
  public:
    sensors(uint8_t IRPin){
      this -> IRPin = IRPin;
      pinMode(IRPin, INPUT);
    }
    sensors(uint8_t trigPin, uint8_t echoPin, int sensorNumber){

      this -> trigPin = trigPin;
      this -> echoPin = echoPin;
      this -> sensorNumber = sensorNumber;
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }
  /*void setColorAddress(String hexaKey){}
    //void setSonicDistancePins(int trigger,int echo){}
    //void setLaserDistance(int sda,int scl){}*/
  bool getLeftIR(int IRPin){
    return analogRead(IRPin);} 
  bool getRightIR(int IRPin){
    return analogRead(IRPin);} 
  bool getClawIR(int IRPin){
    return analogRead(IRPin);} 
  bool color(int lowColor, int highColor, int IRPin){
    int sensorValue = IRPin;
    if(lowColor<=IRPin && IRPin<=highColor){
      return true;}
    else{
      return false;
    }
  }
  int sonicDistanceSensor(int sensorNumber, bool rebel){
    int distance,duration,cm,inch,count=0;
    /*do{this.digitalWrite(trigPin, LOW);delayMicroseconds(5);this.digitalWrite(trigPin, HIGI);count++;}while(count<=2)*/
    pinMode(echoPin, INPUT);
    duration = pulseIn(echoPin, HIGH);
      return cm = (duration/2)/29.1;
    }
  //int laserDistanceSensor(int sensorNumber)

};
sensors frin(8);
void setup() {
  Serial.begin(9600);
  frin.getClawIR(8);
}

void loop() {

}
