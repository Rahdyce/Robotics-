#include <sensorFactory.h>
sensorFactory ultra;
sensorFactory ir1;
sensorFactory ir2;
sensorFactory tsc;
void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);
  Serial.begin(9600);
  tsc.setColorPin(0,1);
  ultra.setUltraPin(15,14,0);
  ir1.setIRPin(17, 0);
  ir2.setIRPin(18, 1);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(2,HIGH);
  Serial.print("Ultra sonic value is: ");
  Serial.println(ultra.sonicDistanceSensor(15,14));
  if(ir1.getIRsensor(17)==1){
    Serial.println("ir1 is 1");}
  else{
    Serial.println("ir1 is 0");
  }
  if(ir2.getIRsensor(16)==1){
    Serial.println(" ir2 1");}
  else{
    Serial.println("ir2 is 0");
  }
    if(tsc.greenLight()==true){
    Serial.println("Green light present");
  }
  delay(1000);
}
