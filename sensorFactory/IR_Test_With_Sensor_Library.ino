#include <sensorFactory.h>
sensorFactory IR0;

void setup() {
  // put your setup code here, to run once:
  IR0.setIRPin(13, 0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(IR0.getClawIR(13)==1){
    Serial.print(IRO.getClawIR);
    Serial.println(" Open");
  }
  else{
    Serial.print(IRO.getClawIR);
    Serial.println(" Close");
  }
}
