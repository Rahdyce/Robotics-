#include <sensorFactory.h>
sensorFactory tsc;
void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);
  Serial.begin(9600);
  tsc.setColorPin(0,1);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(2, HIGH);
  if(tsc.greenLight()==true){
    Serial.println("Green light present");
  }
  else{
    Serial.println("Blue light present");
  }

}
